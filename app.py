from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# User data (for demonstration purposes, replace with a database)
users = {'RomaKakade': 'Password@123', 'Rokakade': 'Password@123'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect(url_for('success'))
        else:
            return redirect(url_for('failure'))

    return render_template('login.html')

@app.route('/success')
def success():
    return 'Login successful!'

@app.route('/failure')
def failure():
    return 'Login failed.'

if __name__ == '__main__':
    app.run(debug=True)
