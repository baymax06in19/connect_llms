## IN PROGRESS......

## LLM — Large Language Model

The reason behind the recent major breakthrough of the term *AI* is AI is the rise of LLMs....We will dive deep and completely understand and build our own LLM in the future in a separate branch. But for now, our main focus is on **how to use LLMs**.

---

### Why LLM?

LLM is powerful, right?  
So should we **build it** or **use it**?

For me, it’s both. First, we will *use them*, explore their capabilities, and gain hands-on experience with the “monster” we’re dealing with. Later, we will dive into the *core theories behind LLMs* and try building one from scratch.

---

### Since we are not building one now — how do we use an LLM?

That’s where *LLM providers* come into play.

LLM providers are companies, organizations, or projects that develop, train, host, or serve large language models.

Examples:

- **OpenAI** — GPT-5, o1, Codex, Whisper  
- **Anthropic** — Claude 3 (Opus, Sonnet, Haiku)  
- **Google DeepMind** — Gemini  
- **Meta** — Llama  
- **Microsoft** — Phi  
- **xAI** — Grok  
- **Mistral AI**  
- **MiniMax (China)** — MiniMax-M2 (GGUF community ports)  
- **DeepSeek**  
- **Hugging Face**

…and many more.

---

### Why can't everyone build one?

Training requires massive computational resources. Only major companies or well-funded teams can build very large models. Smaller models exist (e.g., 300M parameter models), but they are far less capable. Larger models like *DeepSeek R1 with 671B parameters* require massive processing power

What makes an LLM *good* is not only the number of parameters but also the *training process*, which differs across providers.More parameters give potential — but good training unlocks intelligence.

---

### Types of LLM Providers

We can categorize LLM into two groups:

#### Open-Source
They provide:

- Model weights  
- Training details  
- Licensing for modification or hosting  

Examples: Llama, DeepSeek, some Mistral models

#### Proprietary (Closed Source)
They do *not* share their training process or raw model files. You can only *use* them (through APIs).

Examples: OpenAI ChatGPT models, Anthropic’s Claude

---

### Local vs Cloud Use

If the model is open source, we can *host it locally* — but this requires:

- Enough hardware resources
- Model being open source
<img src="images/cnt_llm_local.png" alt="LLM on premise" width="300">

Otherwise, we rely on *cloud-based usage*.
<img src="images/cnt_llm_cloud.png" alt="LLM Cloud Diagram" width="500">

---

### Two Main Usage Approaches

| Mode | Method | Description |
|------|--------|-------------|
| **On-host** | Ollama | Run models locally if hardware supports it |
| **On-cloud** | OpenAI, Anthropic, Ollama Cloud, etc. | Use hosted models through APIs |

We will next explore both approaches.
**On-cloud**
<summary><h3>Open-ai</h3></summary>

<br>
Follow the official OpenAI documentation using the link below:  
<a href="https://platform.openai.com/docs/quickstart?language=python">OpenAI Platform Quickstart (Python)</a>

---
#### 🔹 Step 01 — Create an API Key  
<img src="images/openai-1.png" width="400">

#### 🔹 Step 02 — Create a Secret Key  
<img src="images/openai-2.png" width="400">

#### 🔹 Step 03 — Name the Key  
<img src="images/openai-3.png" width="300">

#### 🔹 Step 04 — Copy and Store the Key Securely  
<img src="images/openai-4_1.png" width="300">

---

Now that you have generated your API key, you can start interacting with GPT.

Reference implementation:  
<a href="https://github.com/baymax06in19/connect_llms/blob/main/code/connect_openai.py">connect_openai.py</a>

```python
# Step 1: Import the 'os' module to access environment variables
import os

# Step 2: Retrieve the OpenAI API key from environment variables
# Ensure it is set before running the script:
# export OPENAI_API_KEY="your_api_key_here"
api_key = os.getenv("OPENAI_API_KEY")

# Step 3: Import the OpenAI client
from openai import OpenAI

# Step 4: Initialize the OpenAI client
# The SDK automatically reads the API key from the environment
client = OpenAI()

# Step 5: Send a request to the model
response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

# Step 6: Print the model output
print(response.output_text)
```
For the first time, you may be able to generate responses using smaller models for free — depending on your account credits or trial eligibility.

You can check the official pricing and free-tier details here:
<a href="https://platform.openai.com/docs/pricing">API Pricing - OpenAI</a>


<summary><h3>Claude</h3></summary>

<br>

Follow the official Claude API Overview documentation using the link below:  
<a href="https://platform.claude.com/docs/en/api/overview">Claude API Overview documentation</a>

---

#### 🔹 Step 01 — Create an API Key  
<img src="images/claude-api1.png" width="400">

#### 🔹 Step 02 — Create a Secret Key  
<img src="images/claude-api2.png" width="400">

#### 🔹 Step 03 — Name the Key  

#### 🔹 Step 04 — Copy and Store the Key Securely  


---

Now that you have generated your API key, you can start interacting with models.

Reference implementation:  
<a href="https://github.com/baymax06in19/connect_llms/blob/main/code/conncet_claude.py">connect_claude.py</a>

```python
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
if response.content:
    print(response.content[0].text)

```
Since the account has no available credits, you might see an error like "Your credit balance is too low."
This is normal and confirms that the code is working correctly.

You can check the official pricing and free-tier details here:
<a href="https://platform.claude.com/docs/en/about-claude/pricing">API Pricing - Claude</a>

<summary><h3>Google Gemini</h3></summary>

<br>

Follow the official Google Gemini API documentation using the link below:  
[]()
<a href="https://ai.google.dev/gemini-api/docs/api-key">Google Gemini API Overview</a>

---
#### 🔹 Step 01 — Create or view the gemini API key

#### 🔹 Step 02 — Create API key

#### 🔹 Step 03 — Name your key

#### 🔹 Step 04 — Copy and Store the Key Securely  
---

Now that you have generated your API key, you can start interacting with Gemini models.

Reference implementation:  
<a href="https://github.com/baymax06in19/connect_llms/blob/main/code/connect_gemini.py">connect_gemini.py</a>


```python
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
```

For the first time, you may be able to generate responses using smaller models for free — depending on your account credits or trial eligibility.

You can check the official pricing and free-tier details here:  
<a href="https://ai.google.dev/gemini-api/docs/pricing">API Pricing - Google Gemini</a>

<summary><h3>Ollama Cloud</h3></summary>

<br>

Follow the official Ollama Cloud documentation using the link below:  

<a href="https://docs.ollama.com/cloud#python">Ollama-Cloud Docs</a>

---
#### 🔹 Step 01 — Create or view the gemini API key

#### 🔹 Step 02 — Create API key

#### 🔹 Step 03 — Name your key

#### 🔹 Step 04 — Copy and Store the Key Securely  
---

Now that you have generated your API key, you can start interacting with Ollama models.

```python
# Step 1: Import the 'os' module to access environment variables
import os

# Step 2: Import the Ollama client library
from ollama import Client

# Step 3: Create a Client object to communicate with the Ollama API
# The API key is passed via the Authorization header
client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": "Bearer " + ollama_api_key
    }
)

# Step 4: Define the chat messages to send to the model
messages = [
    {
        "role": "user",
        "content": "Why is the sky blue?"
    }
]

# Step 5: Send the chat request to the model with streaming enabled
# The response will arrive in small parts (tokens/chunks)
for part in client.chat(
    model="gpt-oss:120b",
    messages=messages,
    stream=True
):
    # Step 6: Print each streamed chunk as it arrives
    print(part["message"]["content"], end="", flush=True)
```
Upto a limit, you will be able to generate responses using  models for free.

You can check the official pricing and free-tier details here:  


**On-host**

## Ollama — On-Host LLM Setup

Ollama allows you to run and experiment with LLMs locally on your machine. Below is a structured guide to getting started.

---

### Step 01: Install Ollama

Download and install Ollama for macOS from the official link:
<a href="https://ollama.com/download/mac">Ollama Installation</a>

---

### Step 02: Verify Installation

After installation, open a terminal and run:
```bash
ollama
```

### Step 03: Directly Call a Model

You can run a model locally using:

```bash
ollama run deepseek-r1:1.5b
ollama run <model_id>
```

to find any model id please visit,
<a href="https://ollama.com/search">Ollama Models</a>

> As mentioned previously, running Ollama locally requires sufficient system resources. If you don’t have enough RAM, you won’t be able to run larger models.
---
### Step 04: Host LLMs on a Server

You can host LLMs on a server and use them in your code.



