from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

counts = {}


@app.route('/')
def index():
    return 'Hello counter is {}'.format(counts)


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def increment_counter():
    global counts
    if request.method in counts.keys():
        counts[request.method] += 1
    else:
        counts.update({request.method: 1})
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
