from flask import Flask, render_template, request, redirect, session, flash, url_for
import pyrebase  # ✅ still works since pyrebase4 uses same name
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key'

firebaseConfig = {
    "apiKey": "AIzaSyDFF0ahXjBe_cRI1zduwcKmY4SKaDfAUaA",
  "authDomain": "notecloud-32840.firebaseapp.com",
  "databaseURL": "https://notecloud-32840-default-rtdb.firebaseio.com/",
  "projectId": "notecloud-32840",
  "storageBucket": "notecloud-32840.appspot.com",
  "messagingSenderId": "946455754786",
  "appId": "1:946455754786:web:c05b8aecf34a65eb44f27b"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()

# Load Firebase config
with open("firebase_config.json") as f:
    firebase_config = json.load(f)

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()


@app.route('/', methods=['GET'])
def home():
    if 'user' in session:
        return redirect('/dashboard')
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    action = request.form['action']

    try:
        if action == "signup":
            auth.create_user_with_email_and_password(email, password)
            flash("✅ Account created! You can now log in.")
            return redirect('/')
        elif action == "login":
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = user['localId']
            session['email'] = email
            return redirect('/dashboard')
    except Exception as e:
        flash("❌ Error: " + str(e).split("]")[-1].strip())
        return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    flash("👋 Logged out successfully.")
    return redirect('/')


@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user' not in session:
        return redirect('/')
    user_id = session['user']
    email = session['email']
    notes_data = db.child("notes").child(user_id).get()
    notes = []
    if notes_data.each():
        for note in notes_data.each():
            notes.append({
                'id': note.key(),
                'title': note.val().get('title'),
                'content': note.val().get('content'),
                'timestamp': note.val().get('timestamp')
            })
    return render_template('dashboard.html', email=email, notes=notes)


@app.route('/add-note', methods=['POST'])
def add_note():
    if 'user' not in session:
        return redirect('/')
    user_id = session['user']
    title = request.form['title']
    content = request.form['content']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {'title': title, 'content': content, 'timestamp': timestamp}
    db.child("notes").child(user_id).push(note)
    flash("✅ Note added.")
    return redirect('/dashboard')


@app.route('/delete-note/<note_id>', methods=['POST'])
def delete_note(note_id):
    if 'user' not in session:
        return redirect('/')
    user_id = session['user']
    db.child("notes").child(user_id).child(note_id).remove()
    flash("🗑️ Note deleted.")
    return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True)
