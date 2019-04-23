from flask import Flask

from bac import registre_mdns

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, world"


if __name__ == '__main__':
    registre_mdns(3000)
    app.run(
        host='0.0.0.0',
        debug=True,
        port=3000
    )
