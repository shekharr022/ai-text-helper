# AI Text Helper

A simple web app built with **Python** and **Streamlit** that uses the **OpenAI API** to summarize or rewrite text.  
Perfect for quick text edits, study notes, or improving writing.


---

## Features
- **Summarize text** into concise points  
- **Rewrite text** to improve clarity or tone  
- Easy-to-use web interface  
- Runs in your browser – no installation needed for the user

---

## Tech Stack
- **Python**
- **Streamlit** – for the web interface
- **OpenAI API** – for text generation
- **python-dotenv** – for handling API keys

---

## Project Structure
ai-text-helper/
│── app.py # Main Streamlit app
│── requirements.txt # Python dependencies
│── .env # API key (not uploaded to GitHub)


---

## Installation & Usage

### Clone the repository
```bash
git clone https://github.com/yourusername/ai-text-helper.git
cd ai-text-helper

python -m venv venv
venv\Scripts\activate    # On Windows
# source venv/bin/activate   # On Mac/Linux

pip install -r requirements.txt
OPENAI_API_KEY=sk-your_api_key_here
streamlit run app.py
