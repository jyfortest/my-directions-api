from flask import Flask
from routes.directions import directions_bp

app = Flask(__name__)

app.register_blueprint(directions_bp)

if __name__ == '__main__' :
  app.run(debug=True)
