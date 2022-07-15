import uuid, random, os
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.dialects.sqlite
from flask import Flask, flash, request, redirect,render_template, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'files'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Word(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(20), unique=True, nullable=False)
    def __repr__(self):
        return f"Word('{self.id}','{self.word}')"


@app.route('/')
@app.route('/home')
def root():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/record')
def record():
    words = Word.query.all()
    return render_template('recording.html', title='Record', word=random.choice(words).word)


@app.route('/save-record', methods=['POST'])
def save_record():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    print("avoiee")
    file_name = file.filename+'_'+str(uuid.uuid4()) + ".mp3"
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    return '<h1>Success</h1>'


if __name__ == '__main__':
    app.run(debug=True)
