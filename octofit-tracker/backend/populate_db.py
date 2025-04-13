import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Create test users
users = [
    User(email=f'user{i}@example.com', name=f'User {i}', age=random.randint(13, 18)) for i in range(1, 6)
]
User.objects.bulk_create(users)

# Create test teams
teams = [
    Team(name=f'Team {i}', members=[user.email for user in users[:3]]) for i in range(1, 3)
]
Team.objects.bulk_create(teams)

# Create test activities
activities = [
    Activity(user=users[0], type='Running', duration=30),
    Activity(user=users[1], type='Walking', duration=20),
    Activity(user=users[2], type='Cycling', duration=40),
]
Activity.objects.bulk_create(activities)

# Create test leaderboard entries
leaderboards = [
    Leaderboard(team=teams[0], points=100),
    Leaderboard(team=teams[1], points=80),
]
Leaderboard.objects.bulk_create(leaderboards)

# Create test workouts
workouts = [
    Workout(name='Push-ups', description='Do 20 push-ups'),
    Workout(name='Sit-ups', description='Do 30 sit-ups'),
]
Workout.objects.bulk_create(workouts)

print("Test data populated successfully!")