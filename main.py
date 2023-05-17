from flask import Flask, render_template, request
app = Flask(__name__)
list_of_operations = []

@app.route('/')
def main():
    list_of_operations.clear()
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)