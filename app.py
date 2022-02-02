from flask import Flask
from routes import users
app = Flask(__name__)

app.add_url_rule('/users/create',view_func=users.create,methods=["POST"])
@app.route('/')
def index():
    return 'main.html'

if __name__ == '__main__':
    app.run(debug=True)