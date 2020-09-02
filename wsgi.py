from init_env import init_env

init_env()

from app import app

if __name__ == '__main__':
    app.run()
