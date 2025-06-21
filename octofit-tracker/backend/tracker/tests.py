from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@example.com', name='Test User', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(email='team@example.com', name='Team User', password='testpass')
        team = Team.objects.create(name='Team A')
        team.members.add(user)
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email='activity@example.com', name='Activity User', password='testpass')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, date='2025-06-21')
        self.assertEqual(activity.activity_type, 'Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(email='leader@example.com', name='Leader User', password='testpass')
        team = Team.objects.create(name='Team B')
        team.members.add(user)
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email='workout@example.com', name='Workout User', password='testpass')
        workout = Workout.objects.create(user=user, workout_type='Yoga', duration=45, date='2025-06-21')
        self.assertEqual(workout.workout_type, 'Yoga')
