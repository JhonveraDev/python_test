from flask import Flask
app = Flask(__name__)

@app.route('/')
def code():
    return 'Hola Flask Route for Platzi'

if __name__ == '__main__':
    app.run()
    