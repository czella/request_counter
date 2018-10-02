from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

def read_txt(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        lines = [element.rstrip().split(',') for element in lines]
        print(lines)
    return dict(lines)

def write_txt(file_name, requests):
    with open(file_name, 'w') as f:
        for key, value in requests.items():
            f.write('{0},{1}\n'.format(key, value))
    return

@app.route('/')
def index():
    counts = read_txt('request_counts.txt')
    return 'Hello counter is {}'.format(counts)


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def increment_counter():
    counts = read_txt('request_counts.txt')
    if request.method in counts.keys():
        counts[request.method] = int(counts[request.method])
        counts[request.method] += 1
    else:
        counts.update({request.method: 1})
    write_txt('request_counts.txt', counts)
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
