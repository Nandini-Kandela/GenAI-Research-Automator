import time    
import PyPDF2       
from google import genai
import os

# 1. Setup the NEW AI Client (Paste your API key here)
client = genai.Client(api_key="YOUR_API_KEY_HERE")

# 2. Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print(f" ERROR: I cannot find '{pdf_path}'. Check the file name!")
        return None
        
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        # Read the first 3 pages
        for page_num in range(min(3, len(reader.pages))):
            text += reader.pages[page_num].extract_text()
    return text

# 3. Ask the AI to Summarize using the new syntax
def summarize_paper(text):
    prompt = f"""
    You are an expert AI research assistant. Read the following academic text and extract:
    1. Core Objective (1 sentence)
    2. Methodology Used (Bullet points)
    3. Key Results (Bullet points)
    
    Here is the text:
    {text}
    """
    
    # Using the brand new Google GenAI syntax and the 2.5-flash model
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite-preview',
        contents=prompt
    )
    return response.text

# --- RUN THE PIPELINE ---
pdf_name = "sample_paper.pdf"

print("Extracting text...")
paper_text = extract_text_from_pdf(pdf_name)

if paper_text:
    print("Generating AI Summary... (this might take a few seconds)")
    try:
        summary = summarize_paper(paper_text)
        print("\n================ FINAL SUMMARY ================\n")
        print(summary)
        print("\n===============================================")
    except Exception as e:
        print(f"\n AI Error: {e}")
