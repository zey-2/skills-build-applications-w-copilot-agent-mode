# This script populates the database with test data for users, teams, activities, leaderboard entries, and workouts.
import os
import sys
import django
from bson import ObjectId
from datetime import timedelta

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

# Import models after Django setup
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

print("Clearing existing data from all collections...")
# Clear existing data using Django ORM
User.objects.all().delete()
Team.objects.all().delete()
Activity.objects.all().delete()
Leaderboard.objects.all().delete()
Workout.objects.all().delete()

print("Creating test users...")
# Create users for Mergington High School with superhero usernames
users = [
    User(id=ObjectId(), email="thundergod@mergington.edu", name="Thunder God", age=16),
    User(id=ObjectId(), email="metalgeek@mergington.edu", name="Metal Geek", age=15),
    User(id=ObjectId(), email="zerocool@mergington.edu", name="Zero Cool", age=17),
    User(id=ObjectId(), email="crashoverride@mergington.edu", name="Crash Override", age=16),
    User(id=ObjectId(), email="sleeptoken@mergington.edu", name="Sleep Token", age=15),
]

# Save users individually
for user in users:
    user.save()
print(f"Added {len(users)} users to the database.")

print("Creating test teams...")
# Create teams
teams = [
    Team(id=ObjectId(), name="Blue Team", members=[users[0].email, users[1].email]),
    Team(id=ObjectId(), name="Gold Team", members=[users[2].email, users[3].email, users[4].email]),
]

# Save teams individually
for team in teams:
    team.save()
print(f"Added {len(teams)} teams to the database.")

print("Creating test activities...")
# Create activities with various types
activities = []
Activity(id=ObjectId(), user=users[0], type="Cycling", duration=60).save()
Activity(id=ObjectId(), user=users[1], type="Crossfit", duration=120).save()
Activity(id=ObjectId(), user=users[2], type="Running", duration=90).save()
Activity(id=ObjectId(), user=users[3], type="Strength", duration=30).save()
Activity(id=ObjectId(), user=users[4], type="Swimming", duration=75).save()
print("Added 5 activities to the database.")

print("Creating test leaderboard entries...")
# Create leaderboard entries
Leaderboard(id=ObjectId(), team=teams[0], points=100).save()
Leaderboard(id=ObjectId(), team=teams[1], points=90).save()
print("Added 2 leaderboard entries to the database.")

print("Creating test workouts...")
# Create workouts with training descriptions
workouts = [
    Workout(id=ObjectId(), name="Cycling Training", description="Training for a road cycling event"),
    Workout(id=ObjectId(), name="Crossfit", description="Training for a crossfit competition"),
    Workout(id=ObjectId(), name="Running Training", description="Training for a marathon"),
    Workout(id=ObjectId(), name="Strength Training", description="Training for strength"),
    Workout(id=ObjectId(), name="Swimming Training", description="Training for a swimming competition"),
]

# Save workouts individually
for workout in workouts:
    workout.save()
print(f"Added {len(workouts)} workouts to the database.")

print("\nTest data populated successfully!")