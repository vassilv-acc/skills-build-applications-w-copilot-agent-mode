from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from django.conf import settings
from pymongo import MongoClient

# Sample data
USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
]

TEAMS = [
    {"name": "Marvel", "members": ["Iron Man", "Captain America", "Black Widow"]},
    {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
]

ACTIVITIES = [
    {"user": "Superman", "activity": "Flight", "duration": 60},
    {"user": "Batman", "activity": "Martial Arts", "duration": 45},
    {"user": "Iron Man", "activity": "Suit Training", "duration": 30},
]

LEADERBOARD = [
    {"user": "Superman", "score": 100},
    {"user": "Iron Man", "score": 90},
    {"user": "Batman", "score": 80},
]

WORKOUTS = [
    {"name": "Strength Training", "suggested_for": ["Superman", "Wonder Woman"]},
    {"name": "Agility Drills", "suggested_for": ["Batman", "Black Widow"]},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index("email", unique=True)

        # Insert data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
