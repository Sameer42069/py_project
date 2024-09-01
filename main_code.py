from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def web():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    user_ip = request.remote_addr
    print(f"Name entered: {name}")
    print(f"IP address: {user_ip}")
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)

