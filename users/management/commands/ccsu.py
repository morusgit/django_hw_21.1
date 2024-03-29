from django.core.management.base import BaseCommand
from users.models import User
import os


#class Command(BaseCommand):
#    def handle(self, *args, **options):
#        user = User.objects.create(
#            email=os.getenv('DEFAULT_EMAIL'),
#            first_name='Admin',
#            last_name='Adminsky',
#            is_superuser=True,
#            is_staff=True,
#            is_active=True
#        )
#        user.set_password(os.getenv('DEFAULT_PW'))
#        user.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email= os.getenv('EMAIL_ADMIN'),
            first_name='admin',
            last_name='admin2',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password(os.getenv('PASSWORD_ADMIN'))
        user.save()
