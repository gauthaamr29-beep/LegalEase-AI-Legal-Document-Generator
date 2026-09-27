import os
from dotenv import load_dotenv

load_dotenv()

class GeminiDocumentGenerator:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise RuntimeError("GEMINI_API_KEY is not set in .env")

        import google.generativeai as genai
        genai.configure(api_key=self.api_key)
        self.genai = genai
        self.model = genai.GenerativeModel("gemini-1.5-pro")

    def generate_document(self, document_type, parties, terms, dates):
        prompt = f"""
Create a professional draft legal document.

Document type: {document_type}
Parties involved: {parties}
Terms and conditions: {terms}
Effective date: {dates}

Requirements:
- Use clear formal legal language.
- Include a title and logical sections.
- Reflect the supplied parties, dates, and terms.
- Do not invent personal facts that were not supplied.
- Return only the document text.
- Include a brief disclaimer that the output is an AI-generated draft
  and should be reviewed by a qualified legal professional before use.
"""
        response = self.model.generate_content(prompt)
        return response.text
