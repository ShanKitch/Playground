from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return "Go to http://localhost:500/play for the playground!"

@app.route('/play')
def level_one():
    return render_template("playground.html", times=3)

@app.route('/play/<times>')
def level_two(times):
    return render_template('playground.html', times=int(times))

@app.route('/play/<times>/<color>')
def level_three(times, color):
    return render_template('playground.html', times=int(times), color=color)

if __name__ == "__main__":
    app.run(debug = True)