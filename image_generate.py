import json
import uuid
import base64
import openai
import os
import streamlit as st
import pandas as pd
from snowflake.snowpark.session import Session
from dotenv import load_dotenv
load_dotenv()


# Function that create's a new or get existing Snowpark session
def create_session():
   if "snowpark_session" not in st.session_state:
      session = Session.builder.configs(json.load(open("connection.json"))).create()
      st.session_state['snowpark_session'] = session
   else:
      session = st.session_state['snowpark_session']
   return session

# Calling the Snowpark session function
session = create_session()

# Retrieve OpenAI key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Add text box for entering text
text_input = st.text_input("Enter description of your favorite animal 👇")
if text_input:
   response = openai.Image.create(
      prompt=text_input,
      n=1,
      size="512x512",
      response_format="b64_json"
   )

  # Convert image base64 string into hex
   image_bytes = response['data'][0]['b64_json']
   bytes_data_in_hex = base64.b64decode(image_bytes).hex()

  # Generate new image file name
   file_name = 'img_' + str(uuid.uuid4())

  # Decode base64 image data and generate image file that can be used to display on screen 
   decoded_data = base64.b64decode((image_bytes))
   with open(file_name, 'wb') as f:
      f.write(decoded_data)

  # Write image data in Snowflake table
   df = pd.DataFrame({"FILE_NAME": [file_name], "IMAGE_BYTES": [bytes_data_in_hex]})
   session.write_pandas(df, "IMAGES")