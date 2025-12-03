from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Získáme jméno hostitele (v kontejneru je to ID kontejneru)
    hostname = os.uname()[1]
    return f'Ahoj! Bezim v Docker kontejneru s ID: {hostname}'

if __name__ == '__main__':
    # host='0.0.0.0' je kriticke pro Docker!
    # Pokud by zde bylo 127.0.0.1, aplikace by byla dostupna jen uvnitr kontejneru,
    # ale my bychom se na ni zvenku (z prohlizece) nedostali.
    app.run(host='0.0.0.0', port=5000)