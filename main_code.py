import flask
from flask import request,Flask, render_template
main_code=Flask(__name__)
@main_code.route('/')
def web():
    return render_template('index.html')
@main_code.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    user_ip = request.remote_addr
    print(f"Name entered: {name}")
    print(f"IP address{user_ip}")
    return f"Hello, {name}!"

if __name__ == '__main__':
    main_code.run(debug=True)
