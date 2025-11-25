# Step 1: Import the 'os' module to access environment variables
import os

# Step 2: Get your OpenAI API key from your system environment variables
# Make sure you have set it like this in your terminal before running the script:
# export OPENAI_API_KEY="your_api_key_here"
api_key = os.getenv("OPENAI_API_KEY")

# Step 3: Import the OpenAI client library
from openai import OpenAI

# Step 4: Create a client object that will let us talk to the OpenAI API
#  OpenAI SDKs are configured to automatically read your API key from the system environment so no need to pass the API key to authenticate else: client = OpenAI(api_key=api_key)
client = OpenAI()

# Step 5: Ask the OpenAI model to generate a response
response = client.responses.create(
    model="gpt-5-nano", # This is the model we are using
    input="Write a one-sentence bedtime story about a unicorn."
)

# Step 6: Print the result from the model
# The text output is stored in 'response.output_text'
print(response.output_text)
