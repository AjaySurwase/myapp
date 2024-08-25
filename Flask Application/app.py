from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    # Expose the app on all interfaces
    app.run(host='0.0.0.0', port=80, debug=True)
