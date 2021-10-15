from bottle import Bottle, request

app = Bottle()

@app.route('/success')
def success():
    return

@app.route('/fail')
def fail():
    raise RuntimeError("There is an error!")

app.run(host='localhost', port=8080)