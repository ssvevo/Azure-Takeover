from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Takeover POC By SagarYadav8742"
