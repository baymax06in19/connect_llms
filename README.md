## IN PROGRESS......

## LLM — Large Language Model

The reason behind the recent major breakthrough of the term **AI** is **LLMs** ..... We will dive deep and completely understand and build our own LLM in the future in a separate branch. But for now, our main focus is on **how to use LLMs**.

---

### Why LLM?

LLM is powerful, right?  
So should we **build it** or **use it**?

For me, it’s both. First, we will **use them**, explore their capabilities, and gain hands-on experience with the “monster” we’re dealing with. Later, we will dive into the **core theories behind LLMs** and try building one from scratch.

---

### Since we are not building one now — how do we use an LLM?

That’s where **LLM providers** come into play.

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

Training requires massive computational resources. Only major companies or well-funded teams can build very large models. Smaller models exist (e.g., 300M parameter models), but they are far less capable. Larger models like **DeepSeek R1 with 671B parameters** require infrastructure similar to supercomputers.

What makes an LLM *good* is not only the number of parameters but also the **training process**, which differs across providers.More parameters give potential — but good training unlocks intelligence.

---

### Types of LLM Providers

We can categorize them into two groups:

#### ✔ Open-Source
They provide:

- Model weights  
- Training details  
- Licensing for modification or hosting  

Examples: Llama, DeepSeek, some Mistral models

#### ✔ Proprietary (Closed Source)
They do **not** share their training process or raw model files. You can only **use** them through APIs.

Examples: OpenAI ChatGPT models, Anthropic’s Claude

---

### Local vs Cloud Use

If the model is open source, we can **host it locally** — but this requires:

- Enough RAM / GPU
- Model being open source
<img src="images/cnt_llm_local.png" alt="LLM on premise" width="500">

Otherwise, we rely on **cloud-based usage**.
<img src="images/cnt_llm_cloud.png" alt="LLM Cloud Diagram" width="500">

---

### Two Main Usage Approaches

| Mode | Method | Description |
|------|--------|-------------|
| **On-host** | Ollama | Run models locally if hardware supports it |
| **On-cloud** | OpenAI, Anthropic, Ollama Cloud, etc. | Use hosted models through APIs |

---

We will explore both approaches.
