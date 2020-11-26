from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Hello world!'

    def handle(self, *args, **options):
        self.stdout.write("Hello there!")