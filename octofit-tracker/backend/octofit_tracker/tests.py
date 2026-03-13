from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelSmokeTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')

    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', members=['Test'])
        self.assertEqual(team.name, 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test', activity='Run', duration=10)
        self.assertEqual(activity.activity, 'Run')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(user='Test', score=123)
        self.assertEqual(lb.score, 123)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', suggested_for=['Test'])
        self.assertEqual(workout.name, 'Test Workout')
