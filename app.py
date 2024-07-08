from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__, template_folder='templates')
notes = []

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    note = request.form.get('note')
    if note:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes.append({'text': note, 'timestamp': timestamp})
    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    if 0 <= note_id < len(notes):
        del notes[note_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    if request.method == 'POST':
        new_note = request.form.get('note')
        if new_note:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            notes[note_id] = {'text': new_note, 'timestamp': timestamp}
        return redirect(url_for('index'))
    else:
        note = notes[note_id]
        return render_template('edit.html', note=note['text'], note_id=note_id)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
