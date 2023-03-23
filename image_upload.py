import json
import streamlit as st
import pandas as pd
from snowflake.snowpark import Session

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

# Uses Streamlit's "st.file_uploader()" to allow the user to upload an image file.
uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False, label_visibility='hidden')
# Once uploaded it then vv
if uploaded_file is not None:
  # Converts image base64 string into hex 
  bytes_data_in_hex = uploaded_file.getvalue().hex()

  # Generates new image file name
  file_name = 'img_' + str(uuid.uuid4())

  # Write image data in Snowflake table
  df = pd.DataFrame({"FILE_NAME": [file_name], "IMAGE_BYTES": [bytes_data_in_hex]})
  session.write_pandas(df, "IMAGES")