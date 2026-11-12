# AI Resume & ATS Matcher

Upload a resume (PDF), paste a job description, and get an ATS-style report:
a match score, missing keywords and three actionable tips. Built with Python,
Streamlit, pypdf and any OpenAI-compatible AI provider (Groq by default).

## Run it locally

1. Install Python 3.10+ (tick "Add Python to PATH" on Windows) and VS Code.
2. Open this folder in VS Code, then open the terminal (Terminal > New Terminal).
3. Create and activate a virtual environment, then install the packages:
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
   pip install -r requirements.txt
   ```
4. Get a free API key from https://console.groq.com
5. Create a folder called `.streamlit`, copy `secrets.toml.example` into it,
   rename the copy to `secrets.toml`, and paste your key in.
   (`secrets.toml` is in `.gitignore`, so it is never uploaded to GitHub.)
6. Start the app:
   ```
   streamlit run app.py
   ```

## Using a different provider

Any OpenAI-compatible provider works. Change `LLM_BASE_URL`, `LLM_MODELS` and
`LLM_API_KEY` in your secrets, with no code changes. Running a local model with
Ollama is also possible (base URL `http://localhost:11434/v1`).

## Deploy

Push to GitHub, create an app on Streamlit Community Cloud, and add the same
settings under the app's Secrets.

## How it works

1. Extract text from the PDF with pypdf.
2. Build a prompt that treats resume and job text as data, not instructions.
3. Call the AI model, falling back to the next model if one is unavailable.
4. Show the report.

## Privacy

Resume text is sent to the AI provider you configure and is not stored by this app.

## What I would improve next

- Structured (JSON) output with a proper score display
- Support for scanned PDFs (OCR)
- Rate limiting and basic tests
