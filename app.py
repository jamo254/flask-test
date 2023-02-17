from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
  app.run(host='0.0.0.0')

@app.route('/')
def login_form():
   return render_template("index.html")


