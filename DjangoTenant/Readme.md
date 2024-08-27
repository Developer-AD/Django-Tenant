Migrations : 

    <!-- This is for Shared App -->
    1. py manage.py makemigrations
    2. py manage.py migrate_schemas --shared

    <!-- This is for Client App -->
    1. py manage.py makemigrations
    2. py manage.py migrate_schemas