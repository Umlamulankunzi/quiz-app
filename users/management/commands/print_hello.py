from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints Hello, World!'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Hello, World!'))
