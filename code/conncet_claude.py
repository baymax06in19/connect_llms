# Step 1: Import the 'os' module to access environment variables
import os

# Step 2: Get your Anthropic API key from your system environment variables
# Make sure you have set it like this in your terminal before running the script:
# export ANTHROPIC_API_KEY="your_api_key_here"
api_key = os.getenv("ANTHROPIC_API_KEY")
#ANTHROPIC_API_KEY = "sk-ant-a***" 


# Step 3: Import the Anthropic client library
from anthropic import Anthropic

# Step 4: Create a client object that will let us talk to the Anthropic API
# The Anthropic SDK automatically uses your API key from your system environment
client = Anthropic(api_key=api_key)

# Step 5: Send a request to the model
response = client.messages.create(
    model="claude-3-haiku-20240307",  # You can change this to any available Claude model
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

# Step 6: Print the output text from the model's response
print(response.content[0].text)
