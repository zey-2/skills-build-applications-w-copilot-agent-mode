import os
import django
import random
import pymongo
from datetime import datetime, timedelta
from bson import ObjectId

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

# Connect to MongoDB directly to ensure proper data insertion
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']

# Clear existing collections
db.users.delete_many({})
db.teams.delete_many({})
db.activity.delete_many({})
db.leaderboard.delete_many({})
db.workouts.delete_many({})

print("Cleared existing data from all collections.")

# Create and insert test users
users = [
    {
        "_id": ObjectId(),
        "email": "john.smith@merington.edu",
        "name": "John Smith",
        "age": 16,
        "grade": 10,
        "fitness_level": "Intermediate"
    },
    {
        "_id": ObjectId(),
        "email": "emma.jones@merington.edu",
        "name": "Emma Jones",
        "age": 15,
        "grade": 9,
        "fitness_level": "Beginner"
    },
    {
        "_id": ObjectId(),
        "email": "michael.brown@merington.edu",
        "name": "Michael Brown",
        "age": 17,
        "grade": 11,
        "fitness_level": "Advanced"
    },
    {
        "_id": ObjectId(),
        "email": "sophia.davis@merington.edu",
        "name": "Sophia Davis",
        "age": 16,
        "grade": 10,
        "fitness_level": "Intermediate"
    },
    {
        "_id": ObjectId(),
        "email": "james.wilson@merington.edu",
        "name": "James Wilson",
        "age": 15,
        "grade": 9,
        "fitness_level": "Beginner"
    }
]

db.users.insert_many(users)
print(f"Added {len(users)} users to the database.")

# User references by email for easier team creation
user_ids = {user['email']: user['_id'] for user in users}

# Create and insert test teams
teams = [
    {
        "_id": ObjectId(),
        "name": "Speed Demons",
        "members": [user_ids["john.smith@merington.edu"], user_ids["emma.jones@merington.edu"]],
        "created_at": datetime.now(),
        "team_motto": "Faster than lightning!"
    },
    {
        "_id": ObjectId(),
        "name": "Muscle Maniacs",
        "members": [user_ids["michael.brown@merington.edu"], user_ids["sophia.davis@merington.edu"]],
        "created_at": datetime.now(),
        "team_motto": "No pain, no gain!"
    },
    {
        "_id": ObjectId(),
        "name": "Fitness Fanatics",
        "members": [user_ids["james.wilson@merington.edu"], user_ids["john.smith@merington.edu"]],
        "created_at": datetime.now(),
        "team_motto": "Fit for life!"
    }
]

db.teams.insert_many(teams)
print(f"Added {len(teams)} teams to the database.")

# Team references by name for easier leaderboard creation
team_ids = {team['name']: team['_id'] for team in teams}

# Create and insert test activities
activities = []
activity_types = ["Running", "Walking", "Cycling", "Swimming", "Weightlifting", "Yoga", "HIIT"]

for user in users:
    # Generate 3-5 random activities per user
    for _ in range(random.randint(3, 5)):
        today = datetime.now()
        random_days_ago = random.randint(0, 14)  # Activities within the last two weeks
        activity_date = today - timedelta(days=random_days_ago)
        
        activities.append({
            "_id": ObjectId(),
            "user_id": user["_id"],
            "type": random.choice(activity_types),
            "duration": random.randint(15, 120),  # Duration in minutes
            "calories_burned": random.randint(100, 800),
            "date": activity_date,
            "notes": f"Felt {'great' if random.random() > 0.5 else 'tired'} today!"
        })

db.activity.insert_many(activities)
print(f"Added {len(activities)} activities to the database.")

# Create and insert test leaderboard data
leaderboard = []
for team in teams:
    leaderboard.append({
        "_id": ObjectId(),
        "team_id": team["_id"],
        "points": random.randint(50, 500),
        "rank": 0,  # Will be calculated based on points
        "last_updated": datetime.now()
    })

# Sort by points and assign ranks
sorted_leaderboard = sorted(leaderboard, key=lambda x: x["points"], reverse=True)
for i, entry in enumerate(sorted_leaderboard):
    entry["rank"] = i + 1

db.leaderboard.insert_many(leaderboard)
print(f"Added {len(leaderboard)} leaderboard entries to the database.")

# Create and insert test workouts
workouts = [
    {
        "_id": ObjectId(),
        "name": "Morning Cardio",
        "description": "30-minute cardio workout to kickstart your day.",
        "difficulty": "Beginner",
        "estimated_calories": 250,
        "exercises": ["Jumping Jacks", "High Knees", "Butt Kicks", "Mountain Climbers"]
    },
    {
        "_id": ObjectId(),
        "name": "Core Crusher",
        "description": "Intense core workout to strengthen your abs and back.",
        "difficulty": "Intermediate",
        "estimated_calories": 300,
        "exercises": ["Plank", "Russian Twists", "Bicycle Crunches", "Leg Raises"]
    },
    {
        "_id": ObjectId(),
        "name": "Full Body HIIT",
        "description": "High-intensity interval training for the entire body.",
        "difficulty": "Advanced",
        "estimated_calories": 450,
        "exercises": ["Burpees", "Push-ups", "Squats", "Mountain Climbers", "Plank Jacks"]
    },
    {
        "_id": ObjectId(),
        "name": "Leg Day",
        "description": "Focus on building leg strength and endurance.",
        "difficulty": "Intermediate",
        "estimated_calories": 350,
        "exercises": ["Squats", "Lunges", "Calf Raises", "Wall Sits", "Box Jumps"]
    },
    {
        "_id": ObjectId(),
        "name": "Upper Body Blast",
        "description": "Strengthen your arms, chest, and back.",
        "difficulty": "Intermediate",
        "estimated_calories": 300,
        "exercises": ["Push-ups", "Pull-ups", "Dips", "Shoulder Press", "Bicep Curls"]
    }
]

db.workouts.insert_many(workouts)
print(f"Added {len(workouts)} workouts to the database.")

# Verify data insertion
users_count = db.users.count_documents({})
teams_count = db.teams.count_documents({})
activities_count = db.activity.count_documents({})
leaderboard_count = db.leaderboard.count_documents({})
workouts_count = db.workouts.count_documents({})

print("\nData population summary:")
print(f"- Users: {users_count}")
print(f"- Teams: {teams_count}")
print(f"- Activities: {activities_count}")
print(f"- Leaderboard entries: {leaderboard_count}")
print(f"- Workouts: {workouts_count}")

print("\nTest data populated successfully!")