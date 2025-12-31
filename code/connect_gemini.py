# Step 1: Import the 'os' module to access environment variables
import os

# Step 2: Get your Google Gemini API key from your system environment variables
# Make sure you have set it like this in your terminal before running the script:
# export GEMINI_API_KEY="your_api_key_here"
api_key = os.getenv("GEMINI_API_KEY")

# Step 3: Import the Google Gemini client library
from google import genai

# Step 4: Create a client object that will let us talk to the Gemini API
# The client automatically uses the API key we pass
client = genai.Client()

# Step 5: Send a request to the model
response = client.models.generate_content(
    model="gemini-2.5-flash",        # You can choose another Gemini model if needed
    contents="Explain how AI works in a few words"
)

# Step 6: Print the output text from the model's response
print(response.text)
