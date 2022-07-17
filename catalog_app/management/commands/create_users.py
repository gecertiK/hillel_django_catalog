from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Create random users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('total_users', choices=range(1, 10 + 1), type=int,
                            help='The number of users that will be created')

    def handle(self, *args, **options):
        fake = Faker()
        total_users = options['total_users']
        users = []
        for create_users in range(total_users):
            users.append(User(username=fake.user_name(), email=fake.email(safe=False),
                              password=make_password(fake.password())))
        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'It`s successfully created {total_users} users'))
