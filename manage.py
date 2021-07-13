from flask_script import Server, Manager
from app.app import app


manager = Manager(app)

server = Server(host="0.0.0.0", port=5000)


@manager.command
def runserver():
    app.run(debug=True, host="0.0.0.0", port=5000, use_reloader=True)


if __name__ == "__main__":
    manager.run()
