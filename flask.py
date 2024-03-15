from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake database to store user information
users = {
    'user1': {'email': 'user1@example.com', 'password': 'password1'},
    'user2': {'email': 'user2@example.com', 'password': 'password2'}
}

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Here you can add code to validate email and password
        # For simplicity, let's just add the user to our fake database
        username = 'user{}'.format(len(users) + 1)
        users[username] = {'email': email, 'password': password}
        return redirect(url_for('login'))
    return render_template('signup.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        for username, user_info in users.items():
            if user_info['email'] == email and user_info['password'] == password:
                # Here you can add code for session management
                return redirect(url_for('profile', username=username))
        return render_template('login.html', error='Invalid email or password')
    return render_template('login.html')

# Profile page
@app.route('/profile/<username>')
def profile(username):
    user_info = users.get(username)
    if user_info:
        return render_template('profile.html', username=username, email=user_info['email'])
    return 'User not found'

# Forget password page
@app.route('/forgetpassword')
def forget_password():
    return render_template('forgetpassword.html')

# Schedule medication page
@app.route('/sche_med')
def schedule_med():
    return render_template('sche_med.html')

if __name__ == '__main__':
    app.run(debug=True)
