from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(email='mona@school.edu', name='Mona', password='password1')
        user2 = User.objects.create(email='octo@school.edu', name='Octo', password='password2')
        user3 = User.objects.create(email='fit@school.edu', name='Fit', password='password3')

        # Teams
        team1 = Team.objects.create(name='Team Alpha')
        team2 = Team.objects.create(name='Team Beta')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Activities
        Activity.objects.create(user=user1, activity_type='Running', duration=30, date=date(2025, 6, 1))
        Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date=date(2025, 6, 2))
        Activity.objects.create(user=user3, activity_type='Swimming', duration=60, date=date(2025, 6, 3))

        # Leaderboard
        Leaderboard.objects.create(team=team1, score=150)
        Leaderboard.objects.create(team=team2, score=100)

        # Workouts
        Workout.objects.create(user=user1, workout_type='Yoga', duration=40, date=date(2025, 6, 4))
        Workout.objects.create(user=user2, workout_type='Pilates', duration=50, date=date(2025, 6, 5))
        Workout.objects.create(user=user3, workout_type='HIIT', duration=35, date=date(2025, 6, 6))

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
