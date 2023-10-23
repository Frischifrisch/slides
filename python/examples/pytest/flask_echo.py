from flask import Flask, request
eapp = Flask(__name__)

@eapp.route("/")
def hello():
    return '''
<form action="/echo" method="GET">
<input name="text">
<input type="submit" value="Echo">
</form>
'''

@eapp.route("/echo")
def echo():
    if answer := request.args.get('text'):
        return f"You said: {answer}"
    else:
        return "Nothing to say?"


if __name__ == "__main__":
    eapp.run()
