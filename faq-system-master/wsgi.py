import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/faq-system'
if path not in sys.path:
    sys.path.append(path)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'faq_project.settings'

# Set the secret key and debug mode for production
os.environ['SECRET_KEY'] = 'your-secret-key-here'
os.environ['DEBUG'] = 'False'

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
