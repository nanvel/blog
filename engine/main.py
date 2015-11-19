import os.path

from c2p2 import app
from c2p2 import settings


rel = lambda p: os.path.join(os.path.dirname(os.path.realpath(__file__)), p)


if __name__ == '__main__':
	settings.SOURCE_FOLDER = rel('..')
    app.run()
