import os.path

from c2p2 import app


rel = lambda p: os.path.join(os.path.dirname(os.path.realpath(__file__)), p)


if __name__ == '__main__':
    app.run(source_folder=rel('..'))
