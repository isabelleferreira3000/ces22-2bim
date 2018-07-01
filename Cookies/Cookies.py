from flask import Flask, make_response, request

app = Flask(__name__)


@app.route("/set")
def setcookies():
    resp = make_response('Setting cookie!')
    resp.set_cookie('framework', 'flask')
    return resp


@app.route("/get")
def getcookies():
    framework = request.cookies.get('framework')
    return 'The framework is ' + framework


if __name__ == '__main__':
    app.run(debug=True)
