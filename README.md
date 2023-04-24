# Image Recognition App with Python, Snowflake Snowpark, OpenAI DALL-E 2, and PyTorch
This is an image recognition app that utilizes the Snowflake Snowpark, PyTorch, Streamlit, and OpenAI's DALL-E 2 to perform two functions:

1. Detect what an uploaded image is showing and display it in text.
2. Generate an image of a given animal when its name is typed in.

## Installation
To install the required packages, run the following command:

```
conda create --name snowpark-img-rec -c https://repo.anaconda.com/pkgs/snowflake python=3.8
conda activate snowpark-img-rec
conda install -c https://repo.anaconda.com/pkgs/snowflake snowflake-snowpark-python pandas notebook cachetools
pip install openai 
pip install uuid 
pip install streamlit
```

This app also requires a Snowflake account with access to Snowpark. Follow the instructions in the Snowflake documentation to set up your Snowpark environment.

## Usage
To use the app, follow these steps:

Start the Streamlit server by running the following command in your terminal:
```
streamlit run image_upload.py
streamlit run image_generate.py
```

Open the app in your browser by navigating to http://localhost:8501.

To detect what an uploaded image is showing, click on the "Upload Image" button and select an image from your computer. Click the "Submit" button to see the text description of the image.

To generate an image of an animal, type the name of the animal into the input box and click the "Generate" button. The app will use OpenAI DALL-E 2 to generate an image of the animal and display it on the screen.

## Credits
This app was created using the following technologies:

Python
PyTorch
OpenAI DALL-E 2
Streamlit
Snowflake Snowpark
