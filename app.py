from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return '<p>Hello,from <strong>Flask</strong></p>'
if __name__=="__main__":
    app.run(debug=True)