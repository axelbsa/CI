import sys
import site
activate_this = '/var/www/flask_d3/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.stdout = sys.stderr
sys.path.insert(0, '/var/www/flask_d3/theapp')
sys.path.insert(0, '/var/www/flask_d3/theapp/uploads')

site.addsitedir('/var/www/flask_d3/theapp')
site.addsitedir('/var/www/flask_d3/theapp/uploads')

from flask_app import app as application
