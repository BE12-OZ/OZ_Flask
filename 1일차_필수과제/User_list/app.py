from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def user_list():
    users = [
        {"username": "춘식이", "name": "춘식이", "email": "cnstlrdl@example.com"},
        {"username": "빵빵이", "name": "빵빵이", "email": "qkdqkddl@example.com"},
        {"username": "라이언", "name": "라이언", "email": "fkdldjs@example.com"}
    ]
    return render_template('user_list.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)