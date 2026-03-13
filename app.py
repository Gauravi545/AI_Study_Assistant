from flask import request, Flask, render_template
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import nltk
import fitz
import os

nltk.download('punkt')  # fixed

app = Flask(__name__)

text = ""  # store PDF text globally

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def uploadFile():
    global text

    if 'file' not in request.files:
        return "Not a file"
    file = request.files['file']

    if file.filename == "":
        return "Please select a file"
    
    path = os.path.join("uploads", file.filename)
    file.save(path)

    # Extract text
    doc = fitz.open(path)
    text = "".join([page.get_text() for page in doc])
    
    return "File uploaded successfully. <a href='/summary'>Generate Summary</a>"

@app.route("/summary")
def generate_summary():
    global text
    if not text:
        return "No file uploaded yet."

    sentences_count = 8  # number of sentences in summary
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, sentences_count)
    
    summary_text = " ".join([str(sentence) for sentence in summary])
    return render_template("text.html", summary=summary_text)

if __name__=="__main__":
    app.run(debug=True)