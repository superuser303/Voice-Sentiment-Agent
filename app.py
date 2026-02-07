from transformers import pipeline 
import speech_recognition as sr 
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
import gradio as gr

#Sentiment: HF pre-trained DistilBERT 
sentiment_pipeline = pipeline("sentiment-analysis", 
model="distilbert-base-uncased-finetuned-sst-2-english")
def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return {"sentiment": result['label'].lower(),
"confidence": f"{result['score']:.2f}"}

#Voice: Google STT (online, free) 
r = sr.Recognizer()
def Voice_to_text(audio_file):
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        try:
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Could not understand audio-try clearer speech"
        except sr.RequestError as e:
            return "API error-check quota or try later"

#Agent: Groq LLM + Langchain
llm = Groq(model="llama3-8b-8192", api_key="your_free_groq_key") # Groq API Key 
tools = [
    Tool(
        name="HFSentiment",
        func=analyze_sentiment,
        description="Analyze text sentiment using Hugging Face DistilBERT model"
    )
]
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

#Gradio Interface for Real-time Demo 
def run_voice_agent(audio, text_input=""):
    if audio: #Handle audio input (mic or upload)
        text = Voice_to_text(audio)
    else: #Fallback to text input 
        text=text_input or "NO input provider"
    if "error" in text.lower() or "could not understand" in text.lower():
        return text, "Agent failed: Try clearer input"
    
    response = agent.run(f"Analyze sentiment of:{text}.suggest an action if negative.")
    return text, response 

iface= gr.Interface(
    fn=run_voice_agent, 
    inputs=[
        gr.Audio(source="microphone", type="filepath", label="Speak of Upload Audio (WAV)"),
        gr.Textbox(label="Or Enter Text", placeholder="Type here if no audio")
    ],
    outputs=[
        gr.Textbox(label="Transcribed Text"),
        gr.Textbox(label="Agent Response")
    ],
    title="Voice-Sentiment Agent:Powered by Hugging Face Models",
    description="Real-time voice/text sentiment analysis with actionable responses. Built with HF DistilBERT, Google STT, and Groq/LangChain.",
    theme="huggingface"
)

if __name__=="__main__":
    iface.launch(server_name="0.0.0.0",server_port=7860)
   #HF Spaces default 
