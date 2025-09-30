# PDF Q&A with LLM (Gemini API)

This project allows you to upload your own PDF (e.g., a book, paper, or notes) and then ask questions about its content using Google Gemini LLM.  

---

## 🚀 Features
- Extracts text from your PDF.  
- Uses **Gemini API** to answer your questions.  
- Simple setup with **uv** for environment management.  

---

## 📦 Setup Instructions

### 1. Install `uv`
`uv` is a fast Python package manager and environment tool. Install it with:

```bash
pip install uv
```

Or see the official guide: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)

---

### 2. Create Virtual Environment
```bash
uv venv
source .venv/bin/activate   # On Linux / Mac
.venv\Scripts\activate      # On Windows
```

---

### 3. Install Dependencies
```bash
uv pip install -r requirements.txt
```

---

### 4. Get a Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/).  
2. Sign in with your Google account.  
3. Generate a new **API Key**.  
4. Copy the key and set it in your environment:

```bash
export GEMINI_API_KEY="your_api_key_here"   # Linux / Mac
setx GEMINI_API_KEY "your_api_key_here"     # Windows
```

---

### 5. Add Your PDF
In the code, locate **line 63**:

```python
pdf_reader = PDFExtractor("poem.pdf")
```

Replace `"poem.pdf"` with your own file name, for example:

```python
pdf_reader = PDFExtractor("my_book.pdf")
```

Make sure your file is in the project directory.  

---

### 6. Run the Project
```bash
python main.py
```

---

## 📝 Usage
After running, you can ask questions about your PDF, such as:  
- *"Summarize chapter 2."*  
- *"What are the main arguments?"*  
- *"Who are the key characters?"*  

---

## ⚡ Notes
- Only one PDF is processed at a time.  
- Responses depend on both the extracted text and Gemini model context limits.  
