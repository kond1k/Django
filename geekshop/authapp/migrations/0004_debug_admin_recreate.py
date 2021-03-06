
from django.conf import settings
from django.db import migrations, transaction


def forwards_func(apps, schema_editor):
    if settings.DEBUG:
        # Only in DEBUG mode!
        try:
            from authapp.models import ShopUser

            with transaction.atomic():
                superuser = ShopUser.objects.create_superuser("admin", "root@google.com", "admin", age=33)
                superuser.save()
        except Exception as exp:
            print(f"Cann't create super user for debug. {exp}")


def reverse_func(apps, schema_editor):
    if settings.DEBUG:
        # Only in DEBUG mode!
        try:
            from authapp.models import ShopUser

            with transaction.atomic():
                ShopUser.objects.all().delete()
        except Exception as exp:
            print(f"Cann't delete super user for debug. {exp}")


class Migration(migrations.Migration):

    dependencies = [("authapp", "0003_user_model_extend")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
