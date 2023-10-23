from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
     <form action="/echo" method="POST">
         <input name="text">
         <input type="submit" value="Echo">
     </form>
     '''

@app.route("/echo", methods=['POST'])
def echo():
    if user_text := request.form.get('text', ''):
        return f"You said: {user_text}"
    return "Nothing to say?"

