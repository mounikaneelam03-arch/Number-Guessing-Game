from flask import Flask, render_template, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['message'] = "I'm thinking of a number between 1 and 100."
        session['msg_type'] = 'info' # info, success, error, warning

    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['attempts'] += 1
            
            if guess < session['number']:
                session['message'] = f"Too low! {guess} is smaller than the number."
                session['msg_type'] = 'warning'
            elif guess > session['number']:
                session['message'] = f"Too high! {guess} is larger than the number."
                session['msg_type'] = 'warning'
            else:
                session['message'] = f"Congratulations! You guessed the number {session['number']} in {session['attempts']} attempts!"
                session['msg_type'] = 'success'
                # Prepare for new game but show success message first
                # We can handle "Play Again" via a separate route or button that clears session
        except ValueError:
            session['message'] = "Please enter a valid number."
            session['msg_type'] = 'error'

    return render_template('index.html', 
                           message=session.get('message'), 
                           msg_type=session.get('msg_type'), 
                           attempts=session.get('attempts'))

@app.route('/reset')
def reset():
    session.pop('number', None)
    session.pop('attempts', None)
    session.pop('message', None)
    session.pop('msg_type', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
