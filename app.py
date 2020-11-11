from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    room = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Worker %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        room = request.form['room']
        email = request.form['email']

        worker = Worker(name=name, surname=surname,
                        room=room, email=email)

        try:
            db.session.add(worker)
            db.session.commit()
            return "Good!"
        except:
            return "Error!"
    else:
        return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)
