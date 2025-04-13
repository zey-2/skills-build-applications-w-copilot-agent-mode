import os
import django
import random
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Clear existing data using raw MongoDB commands
with connection.cursor() as cursor:
    cursor.db_conn["users"].delete_many({})
    cursor.db_conn["teams"].delete_many({})
    cursor.db_conn["activity"].delete_many({})
    cursor.db_conn["leaderboard"].delete_many({})
    cursor.db_conn["workouts"].delete_many({})

# Create test users
users = [
    User(email=f'user{i}@example.com', name=f'User {i}', age=random.randint(13, 18)) for i in range(1, 6)
]

# Save users individually to ensure they are persisted in the database
for user in users:
    user.save()

# Create test teams
teams = [
    Team(name=f'Team {i}', members=[user.email for user in users[:3]]) for i in range(1, 3)
]

# Save teams individually to ensure they are persisted in the database
for team in teams:
    team.save()

# Create test activities
Activity(user=users[0], type='Running', duration=30).save()
Activity(user=users[1], type='Walking', duration=20).save()
Activity(user=users[2], type='Cycling', duration=40).save()

# Save leaderboard entries individually to ensure related objects are saved
Leaderboard(team=teams[0], points=100).save()
Leaderboard(team=teams[1], points=80).save()

# Create test workouts
workouts = [
    Workout(name='Push-ups', description='Do 20 push-ups'),
    Workout(name='Sit-ups', description='Do 30 sit-ups'),
]
Workout.objects.bulk_create(workouts)

print("Test data populated successfully!")