import os

from web.app import app as application


if __name__ == '__main__':
    application.config.from_object('web.config.{}'.format(os.environ.get('FLASK_CONFIG', 'development').capitalize()))
    application.run(host=application.config['HOST'], port=application.config['PORT'], debug=application.config['DEBUG'])
