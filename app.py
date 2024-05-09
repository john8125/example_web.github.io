
from flask import Flask, render_template
from gevent.pywsgi import WSGIServer
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login_1")
def index_1():
    return render_template("login_20230614.html")

@app.route("/content")
def index_2():
    return render_template("content.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
    #app.debug = True
    #app.run()