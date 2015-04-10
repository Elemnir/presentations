from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('test.html', r=request)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
