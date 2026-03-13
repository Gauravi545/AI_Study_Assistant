# AI_Study_Assistant
Your personal study assistant which inputs your notes pdf and generates useful summaries, important points and quizzes for you.

# AI Study Assistant

A web-based application that allows users to upload PDFs, extract text, and generate concise summaries using **LexRank extractive summarization**. Perfect for quickly reviewing study materials, notes, or research papers.  

---

## Features

- Upload PDF files directly via a web interface.  
- Extract text from all pages using **PyMuPDF**.  
- Generate a concise **summary** with the **LexRank algorithm** (via Sumy).  
- Clean, responsive UI with styled pages for both upload and summary.  
- Option to upload another PDF without restarting the app.  

---

## Demo

**Upload Page:**  
![Upload Page](screenshots/upload.png)  

**Summary Page:**  
![Summary Page](screenshots/summary.png)  

*(Replace with actual screenshots if available)*

---

## Technologies Used

- **Python 3.9+**  
- **Flask** – Web framework  
- **PyMuPDF (fitz)** – PDF text extraction  
- **Sumy** – LexRank summarization  
- **NLTK** – Tokenization  
- **HTML, CSS** – Frontend UI  

---

## Installation & Setup

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd AI_Study_Assistant


.\env\Scripts\Activate.ps1