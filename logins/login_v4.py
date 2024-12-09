# claude version with sqlalchemy
from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

# User model
class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    password = db.Column(db.String(80), nullable=False)

LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html>
<body>
    <form method="POST">
        <input type="email" name="email" placeholder="Email" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <input type="submit" value="Login">
    </form>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        user = User.query.filter_by(
            email=request.form['email'], 
            password=request.form['password']
        ).first()
        message = "Login successful!" if user else "Invalid credentials"
    return render_template_string(LOGIN_TEMPLATE, message=message)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Create admin user if doesn't exist
        if not User.query.filter_by(email='admin@example.com').first():
            admin = User(email='admin@example.com', password='admin123')
            db.session.add(admin)
            db.session.commit()
    app.run(debug=True)