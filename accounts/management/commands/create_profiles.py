from django.core.management.base import BaseCommand
from accounts.models import User
from accounts.models import Profile  

class Command(BaseCommand):
    help = 'Create profiles for users who do not have one.'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(profile__isnull=True)

        for user in users_without_profiles:
            Profile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Profile created for user: {user.username}'))

        self.stdout.write(self.style.SUCCESS('Profiles created for all users without a profile.'))
