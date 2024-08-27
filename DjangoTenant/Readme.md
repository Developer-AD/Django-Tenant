Migrations : 

    <!-- This is for Shared App -->
    1. py manage.py makemigrations
    2. py manage.py migrate_schemas --shared

    <!-- This is for Client App -->
    1. py manage.py makemigrations
    2. py manage.py migrate_schemas

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'djangoTenantDB', # Database Name
        'USER': 'scott',          # User Role
        'PASSWORD': 'tiger',      # User Definition. 
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
