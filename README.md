# Multilingual FAQ System

A Django-based FAQ management system with multilingual support, WYSIWYG editor, and caching functionality.

## Features

- Multilingual support (English, Hindi, Bengali)
- Real-time search functionality
- WYSIWYG editor for rich text formatting
- Caching system for improved performance
- Responsive and modern UI
- Admin interface for content management

## Tech Stack

- Python 3.13
- Django 5.1.5
- Django CKEditor 6.7.2
- Deep Translator 1.11.4
- Bootstrap 5.3
- Font Awesome 6.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Rakhi991/faq-system.git
cd faq-system
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
SECRET_KEY=your-secret-key
DEBUG=True
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
faq_project/
├── faqs/                   # Main app directory
│   ├── models.py          # FAQ model with multilingual support
│   ├── views.py           # View logic and API endpoints
│   ├── admin.py           # Admin interface customization
│   └── tests.py           # Unit tests
├── templates/             # HTML templates
│   ├── base.html         # Base template with common elements
│   └── home.html         # FAQ listing and search interface
├── static/               # Static files (CSS, JS, images)
├── requirements.txt      # Project dependencies
└── manage.py            # Django management script
```

## API Endpoints

- `GET /`: Home page with FAQ listing
- `GET /?lang=<language_code>`: Get FAQs in specific language
- `GET /admin/`: Admin interface for content management

## Caching

The system uses Django's caching framework to improve performance:
- FAQ translations are cached for 1 hour
- Cache is automatically invalidated when content is updated

## Testing

Run the test suite:
```bash
python manage.py test
```

Coverage report:
```bash
coverage run --source='.' manage.py test
coverage report
```

## Code Style

This project follows PEP 8 style guide. Check code style:
```bash
flake8 .
```

## Deployment to PythonAnywhere

1. Sign up for a free account at [PythonAnywhere](https://www.pythonanywhere.com/)

2. Open a Bash console in PythonAnywhere and clone your repository:
```bash
git clone https://github.com/Rakhi991/faq-system.git
```

3. Create a virtual environment and install dependencies:
```bash
cd faq-system
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Configure your web app in PythonAnywhere:
   - Go to the Web tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Choose Python version (3.13)
   - Set the following paths:
     - Source code: /home/yourusername/faq-system
     - Working directory: /home/yourusername/faq-system
     - Virtual environment: /home/yourusername/faq-system/venv

5. Configure WSGI file:
   - Click on the WSGI configuration file link
   - Replace the contents with:
```python
import os
import sys

path = '/home/yourusername/faq-system'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'faq_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

6. Create .env file in your project directory:
```bash
cd /home/yourusername/faq-system
echo "SECRET_KEY=your-secret-key" > .env
echo "DEBUG=False" >> .env
```

7. Collect static files:
```bash
python manage.py collectstatic
```

8. Run migrations and create superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
```



Your FAQ system should now be live at: yourusername.pythonanywhere.com

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Admin Dashboard
![Screenshot 2025-02-01 031412](https://github.com/user-attachments/assets/ed562536-9e87-4842-9c21-ff43bec0974f)
## Frontend UI
![Screenshot 2025-02-01 031447](https://github.com/user-attachments/assets/dca2f571-c8ee-48c4-bd5c-c2d0c93d0690)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Rakhi

## Acknowledgments

- Thanks to the Django community for the excellent framework
- Bootstrap team for the UI components
- CKEditor team for the rich text editor
