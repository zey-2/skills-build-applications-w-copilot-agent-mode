import os
import sys
import django
from bson import ObjectId
import random

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

# Import models after Django setup
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.db import connection

print("Clearing existing data from all collections...")
# Clear existing collections using direct MongoDB connection
with connection.cursor() as cursor:
    cursor.db_conn["users"].delete_many({})
    cursor.db_conn["teams"].delete_many({})
    cursor.db_conn["activity"].delete_many({})
    cursor.db_conn["leaderboard"].delete_many({})
    cursor.db_conn["workouts"].delete_many({})

print("Creating test users...")
# Create users for Mergington High School
users = [
    User(id=ObjectId(), email="john.smith@mergington.edu", name="John Smith", age=16),
    User(id=ObjectId(), email="emma.jones@mergington.edu", name="Emma Jones", age=15),
    User(id=ObjectId(), email="michael.brown@mergington.edu", name="Michael Brown", age=17),
    User(id=ObjectId(), email="sophia.davis@mergington.edu", name="Sophia Davis", age=16),
    User(id=ObjectId(), email="james.wilson@mergington.edu", name="James Wilson", age=15),
]

# Save users individually
for user in users:
    user.save()
print(f"Added {len(users)} users to the database.")

print("Creating test teams...")
# Create teams
teams = [
    Team(id=ObjectId(), name="Speed Demons", members=[user.email for user in users[:2]]),
    Team(id=ObjectId(), name="Muscle Maniacs", members=[user.email for user in users[2:4]]),
    Team(id=ObjectId(), name="Fitness Fanatics", members=[users[4].email, users[0].email]),
]

# Save teams individually
for team in teams:
    team.save()
print(f"Added {len(teams)} teams to the database.")

print("Creating test activities...")
# Create activities
activities = [
    Activity(id=ObjectId(), user=users[0], type="Running", duration=30),
    Activity(id=ObjectId(), user=users[1], type="Walking", duration=45),
    Activity(id=ObjectId(), user=users[2], type="Cycling", duration=60),
    Activity(id=ObjectId(), user=users[3], type="Swimming", duration=40),
    Activity(id=ObjectId(), user=users[4], type="Weightlifting", duration=55),
]

# Save activities individually
for activity in activities:
    activity.save()
print(f"Added {len(activities)} activities to the database.")

print("Creating test leaderboard entries...")
# Create leaderboard entries
Leaderboard(id=ObjectId(), team=teams[0], points=100).save()
Leaderboard(id=ObjectId(), team=teams[1], points=85).save()
Leaderboard(id=ObjectId(), team=teams[2], points=95).save()
print("Added 3 leaderboard entries to the database.")

print("Creating test workouts...")
# Create workouts
workouts = [
    Workout(id=ObjectId(), name="Morning Cardio", description="30-minute cardio workout to kickstart your day."),
    Workout(id=ObjectId(), name="Core Crusher", description="Intense core workout to strengthen your abs and back."),
    Workout(id=ObjectId(), name="Full Body HIIT", description="High-intensity interval training for the entire body."),
    Workout(id=ObjectId(), name="Leg Day", description="Focus on building leg strength and endurance."),
    Workout(id=ObjectId(), name="Upper Body Blast", description="Strengthen your arms, chest, and back."),
]

# Save workouts individually
for workout in workouts:
    workout.save()
print(f"Added {len(workouts)} workouts to the database.")

print("\nTest data populated successfully!")