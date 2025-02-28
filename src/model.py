import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI 

class Model:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def google_gemini(transcript, prompt, extra=""):
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")
        try:
            response = model.generate_content(prompt + extra + transcript)
            return response.text
        except Exception as e:
            response_error = "⚠️ There is a problem with the API key or with python module."
            return response_error, e
    
    
    @staticmethod
    def openai_chatgpt(transcript, prompt, extra="", model="gpt-3.5-turbo"):
        load_dotenv()
        client = OpenAI(api_key=os.getenv("OPENAI_CHATGPT_API_KEY"))
        message = [{"role": "system", "content": prompt + extra + transcript}]
        try:
            completion = client.chat.completions.create(model=model, messages=message)
            text = completion.choices[0].message.content
            return text
        except Exception as e:
            response_error = "⚠️ There is a problem with the API key or with python module."
            return response_error, e
