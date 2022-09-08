release: python3 microibm/manage.py makemigrations
release: python3 microibm/manage.py migrate
web: gunicorn microibm.microibm.wsgi