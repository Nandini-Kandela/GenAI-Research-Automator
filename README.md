# GenAI Literature Review Automator 

## About The Project
As a student, I noticed that reading and summarizing dozens of dense research papers is one of the most time-consuming parts of academic research. I built this Generative AI pipeline to solve that exact problem. 

This Python-based tool acts as an AI research assistant. It automatically reads academic PDFs, extracts the core text, and uses a Large Language Model (LLM) to instantly generate a structured summary of the paper's objective, methodology, and key results.

## Key Features
* **Automated Document Processing:** Uses `PyPDF2` to programmatically extract text from standard research paper PDFs.
* **Intelligent Summarization:** Integrates with Google's latest `gemini-2.0-flash` model via the new `google-genai` SDK to understand complex academic language.
* **Pro-Level Error Handling:** Includes built-in auto-retry logic. If the AI servers are overloaded, the script automatically pauses and retries, ensuring the script doesn't crash during heavy traffic.
* **Structured Output:** Forces the LLM to output clean, readable data (Core Objective, Methodology, Key Results) rather than a giant wall of text.

## How It Works
1. Place any research paper in the directory and name it `sample_paper.pdf`.
2. The script extracts the first few pages (typically containing the Abstract and Introduction).
3. The AI processes the text and prints a highly accurate, structured summary directly to the terminal.

## Built With
* **Language:** Python
* **Document Parsing:** PyPDF2
* **AI Engine:** Google GenAI SDK (Gemini 2.0 Flash)

## Future Improvements
This is currently a Minimum Viable Product (MVP) command-line tool. My future plans for this project include:
* Wrapping the script in a **Streamlit** web application for a drag-and-drop user interface.
* Adding batch-processing capabilities so a user can upload an entire folder of 20+ PDFs and export the summaries to a single Pandas DataFrame / CSV file.

---
*Created by Nandini Kandela*
