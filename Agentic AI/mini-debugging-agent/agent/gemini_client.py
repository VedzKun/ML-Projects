import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class GeminiDebugAgent:
    def __init__(self):
        self.model= genai.GenerativeModel('gemini-2.5-flash')
    def _call_gemini(self, prompt:str) -> str:
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 2048,
            }
        )
        return response.text
    def debug(self, error: str, code: str) -> str:
        prompt = f"""
        You are an Expert Python Debugger Agent.

ERROR MESSAGE:
{error}

CODE SNIPPET:
{code}

Follow these steps carefully and respond in this exact format:

1. **Error Type:**
    Identify the exact error type (eg. IndexError, TypeError, NameError and so on)

2.**Cause Analaysis:**
    Explain in simple terms why this error happened.

3. **Fix Suggestions:**
    - Provide the corrected code snippet.
    - Highlight the changes made.
    - Explain why this fix works.

4.**Corrected Code:**
    '''python
    #the corrected code enter here
    '''
    
    Be clear educational and concise
        """
        return self._call_gemini(prompt)
