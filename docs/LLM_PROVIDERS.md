# Supported LLM Providers

The chatbot supports multiple LLM providers. Configure via `.env` file.

## Quick Start

Set `LLM_PROVIDER` in your `.env`:

```bash
LLM_PROVIDER=openai  # or: google, glm
```

## 1. OpenAI (Default)

**Models:** GPT-4o, GPT-4, GPT-3.5-turbo

```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o
```

Get API key: https://platform.openai.com/api-keys

## 2. Google Gemini

**Models:** gemini-1.5-pro, gemini-1.5-flash, gemini-2.0-flash-exp

```bash
LLM_PROVIDER=google
GOOGLE_API_KEY=AIza...
GOOGLE_MODEL=gemini-1.5-pro
```

Get API key: https://aistudio.google.com/app/apikey

## 3. GLM (Zhipu AI / 智谱AI)

**Models:** glm-4, glm-4-flash, glm-4-plus

```bash
LLM_PROVIDER=glm
GLM_API_KEY=your-glm-api-key
GLM_MODEL=glm-4
GLM_BASE_URL=https://open.bigmodel.cn/api/paas/v4/
```

Get API key: https://open.bigmodel.cn/

## Advanced: Mix Multiple Providers

You can programmatically use different providers for different agents:

```python
from app.llm_config import LLMConfig

# Use Gemini for Supervisor (fast routing)
supervisor_llm = LLMConfig.get_llm(provider="google", model="gemini-1.5-flash")

# Use GPT-4o for Sales (better quality)
sales_llm = LLMConfig.get_llm(provider="openai", model="gpt-4o")

# Use GLM for support (cost-effective)
support_llm = LLMConfig.get_llm(provider="glm", model="glm-4")
```
