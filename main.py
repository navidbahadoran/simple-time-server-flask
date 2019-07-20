from flask import Flask
import os
import time

app = Flask(__name__)


@app.route('/')
def show_epoch():
    return str(time.time())


if __name__ == '__main__':
    port = os.environ.get('PORT', 6732)
    app.run(host='0.0.0.0', port=port)

