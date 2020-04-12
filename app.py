from TodoApp import app
import os

if __name__ == '__main__':
    os.environ["FLASK_DEBUG"] = "true"
    app.run()
