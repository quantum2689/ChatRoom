from flask import Flask, request, render_template, redirect, url_for
from tinydb import TinyDB, Query

app = Flask(__name__, template_folder="template")

# Initialize TinyDB
db = TinyDB('db.json')

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "GET":
        # Fetch all messages from TinyDB
        msgs = db.all()
        return render_template("index.html", msgs=msgs, main=url_for('main'))
    if request.method == "POST":
        new_msg = request.form['msg']
        if new_msg:
            # Insert the new message into TinyDB
            db.insert({'msg': new_msg})
        return redirect(url_for('main'))
    return render_template('index.html', msgs=msgs, main=url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)

