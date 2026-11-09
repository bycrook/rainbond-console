from django.db import migrations


class Migration(migrations.Migration):
    """Bridge migration.

    The upstream repository ships 0004_teamhelmreleasesource.py which depends on
    0003_platformfeatureflag, but that file is not published. Keep the chain
    intact so a fresh SQLite/MySQL database can be initialised.
    """

    dependencies = [
        ("console", "0002_auto_20260129_2056"),
    ]

    operations = []
