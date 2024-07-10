from flask import Flask,request,render_template , redirect, url_for
# YOU CAN'T USE THIS APP AS A PROUDCTION APP
app = Flask(__name__,template_folder="template")



msgs = []

@app.route("/",methods=["POST","GET"])
def main():
    if request.method == "GET":
        return render_template("index.html",msgs=msgs, main=url_for('main'))
    if request.method == 'POST':
        new_msg = request.form['msg']
        if new_msg:
            msgs.append(new_msg)
        return redirect(url_for('main'))
    return render_template('chart.html', msgs=msgs, main=url_for('main'))

app.run(debug=True)
