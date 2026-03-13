from flask import request, Flask, render_template
import fitz
import os
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/upload", methods=["POST"])
def uploadFile():
    if 'file' not in request.files:
        return "Not a file"
    file = request.files['file']

    if file.filename=="":
        return "Please select a file"
    
    path = os.path.join("uploads", file.filename)
    file.save(path)
   # return "File uploaded successfully"

    doc=fitz.open(path)
    text="".join([page.get_text() for page in doc])  #extract text from all pages and concatenate with empty string
    return render_template("text.html", extracted_text=text)



if __name__=="__main__":
    app.run(debug=True)