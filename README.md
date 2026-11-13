AI Resume & ATS Matcher

Upload a resume (PDF), paste a job description, and get an ATS-style report: a match score, missing keywords and three actionable tips. Built with Python, Streamlit, pypdf and any OpenAI-compatible AI provider (Groq by default).

Live demo: [add your Streamlit link here after deploying]

Run it locally
Install Python (tested on Python 3.15 on Windows; tick "Add Python to PATH") and VS Code.
Open this folder in VS Code, then open the terminal (Terminal > New Terminal).
Create and activate a virtual environment, then install the packages:
py -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux (use python3 -m venv venv to create it)
pip install -r requirements.txt

If PowerShell blocks the activate script, run this once and try again:

Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
Get a free API key from https://console.groq.com
Create a folder called .streamlit, copy secrets.toml.example into it, rename the copy to secrets.toml, and paste your key in. (secrets.toml is in .gitignore, so it is never uploaded to GitHub.) It needs two lines:
toml
LLM_API_KEY = "paste-your-key-here"
LLM_MODELS = "openai/gpt-oss-120b,openai/gpt-oss-20b"

LLM_BASE_URL is optional. It defaults to Groq.

Start the app:
streamlit run app.py
Check which models your key can use
python list_models.py

This lists the models your API key can access. I wrote it after getting a 404 from a model name that did not exist for my key.

Using a different provider

Any OpenAI-compatible provider should work. Change LLM_BASE_URL, LLM_MODELS and LLM_API_KEY in your secrets, with no code changes. I have only tested Groq. A local model with Ollama (base URL http://localhost:11434/v1) should also work in theory, but I have not tried it; the app needs LLM_API_KEY to be set, so use any placeholder text there.

Deploy

Push to GitHub, create an app on Streamlit Community Cloud (main file app.py), and paste the two secrets above into the app's Secrets box. If you can choose a Python version in Advanced settings, pick 3.12 or 3.13.

How it works
Extract the text from the PDF with pypdf (text layer only, so no OCR).
Cut each input to 8,000 characters to keep requests small, and warn if the job description is under 30 words.
Build a prompt that treats the resume and job text as data, not instructions.
Call the AI model. If a model is missing, too large for the request or rate limited, try the next one. Network and server errors are retried with growing delays.
Show the report.
Limitations
Only text-based PDFs work. Scanned PDFs have no text layer, so the app stops with a message.
A very short job description can make the model invent requirements. The app warns about this and the prompt tells the model not to invent any, but the warning is based on word count only.
The score is an AI estimate, not a real ATS result, and it can vary slightly between runs.
No automated tests yet.
Privacy

Resume text is sent to the AI provider you configure and is not stored by this app. Do not paste anything you would not want sent to that provider.

What I would improve next
Structured (JSON) output with a proper score display
Support for scanned PDFs (OCR)
Rate limiting and basic tests
Try to build independently as I'm learning how to code

I built this with help from Claude and Gemini. I tested it, fixed the problems I found (a hard-coded token, wrong model names, invented requirements from short job descriptions) and can explain how each part works.

