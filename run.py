import init_env
from app import app
import os

if __name__ == '__main__':
    app.run(host=os.environ.get('APP_HOST'), port=os.environ.get('APP_PORT'))
