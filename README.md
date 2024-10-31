# Django Password Reset Project

This is a Django project that includes a password reset functionality with custom styled templates for setting and confirming new passwords.

## Features
- Password reset email functionality
- Custom HTML templates for password reset flow
- Secure password setting and confirmation

## Prerequisites
- Python 3.x
- Django 3.x or higher
- A configured SMTP email service for sending password reset emails

## Installation
```bash
1) Step 1: Clone the Repository
Clone this repository to your local machine:
git clone https://github.com/your-username/LoginAuth.git
cd LoginAuth

2) Step 2: Create and Activate a Virtual Environment
Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3) Step 3: Install Dependencies
Install the required packages using pip:
pip install -r requirements.txt

4) Step 4: Set Up the Database
Run migrations to set up the database:
python manage.py migrate

5) Step 5: Configure Email Settings
To enable password reset emails, configure your email settings in settings.py. Replace your_email@example.com and your_password with your own email credentials. Here’s a sample setup for Gmail:
# settings.py

# Email configuration for password reset
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'your_password'  # Replace with your email password

6) Step 6: Run the Development Server
Start the Django development server:
python manage.py runserver
