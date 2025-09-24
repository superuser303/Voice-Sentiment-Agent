# Voice-Sentiment Agent: Real-Time HF-Powered NLP Demo

Real-time voice/text sentiment analysis using Hugging Face's DistilBERT (pre-trained DL model), Google STT, and Groq/LangChain agent for actions. Built online in Colab, deployed on HF Spaces. Latency: ~3-5s.

## Demo
[![HF Spaces](https://huggingface.co/spaces/hf-space-badge?repository=superuser303/voice-sentiment-hf-models)](your-space-url)

![Demo GIF](assets/demo.gif)

## Features
| Feature | Tech | Why Awesome |
|---------|------|-------------|
| Sentiment | HF DistilBERT | Pre-trained DL, 90%+ acc on SST-2 |
| Voice STT | Google API | Free, real-time transcription |
| Agent | Groq LLM + LangChain | Autonomous actions (e.g., "Negative? Suggest reply") |
| Deploy | HF Spaces | Browser mic, zero setup |

## Setup
1. Clone: `git clone https://github.com/superuser303/voice-sentiment-hf-models`
2. Install: `pip install -r requirements.txt`
3. Run: `python app.py` (or view on HF Spaces)

## Colab Build
[Open in Colab](link-to-your-notebook)

Built with ❤️ for ML interviews—extends my n8n-Task-Agent for agentic DL.