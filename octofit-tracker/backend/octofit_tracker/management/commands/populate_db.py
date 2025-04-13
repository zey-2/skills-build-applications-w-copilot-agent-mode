from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard entries, and workouts.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create test users
        self.stdout.write('Creating test users...')
        users = [
            User(id=ObjectId(), email="thundergod@mergington.edu", name="Thunder God", age=16),
            User(id=ObjectId(), email="metalgeek@mergington.edu", name="Metal Geek", age=15),
            User(id=ObjectId(), email="zerocool@mergington.edu", name="Zero Cool", age=17),
            User(id=ObjectId(), email="crashoverride@mergington.edu", name="Crash Override", age=16),
            User(id=ObjectId(), email="sleeptoken@mergington.edu", name="Sleep Token", age=15),
        ]
        
        # Save users individually to ensure proper ID assignment
        for user in users:
            user.save()
        
        # Create test teams
        self.stdout.write('Creating test teams...')
        teams = [
            Team(id=ObjectId(), name="Blue Team", members=[users[0].email, users[1].email]),
            Team(id=ObjectId(), name="Gold Team", members=[users[2].email, users[3].email, users[4].email]),
        ]
        
        # Save teams
        for team in teams:
            team.save()
            
        # Create test activities
        self.stdout.write('Creating test activities...')
        Activity(id=ObjectId(), user=users[0], type="Cycling", duration=60).save()
        Activity(id=ObjectId(), user=users[1], type="Crossfit", duration=120).save()
        Activity(id=ObjectId(), user=users[2], type="Running", duration=90).save()
        Activity(id=ObjectId(), user=users[3], type="Strength", duration=30).save()
        Activity(id=ObjectId(), user=users[4], type="Swimming", duration=75).save()
        
        # Create test leaderboard entries
        self.stdout.write('Creating test leaderboard entries...')
        Leaderboard(id=ObjectId(), team=teams[0], points=100).save()
        Leaderboard(id=ObjectId(), team=teams[1], points=90).save()
        
        # Create test workouts
        self.stdout.write('Creating test workouts...')
        workouts = [
            Workout(id=ObjectId(), name="Cycling Training", description="Training for a road cycling event"),
            Workout(id=ObjectId(), name="Crossfit", description="Training for a crossfit competition"),
            Workout(id=ObjectId(), name="Running Training", description="Training for a marathon"),
            Workout(id=ObjectId(), name="Strength Training", description="Training for strength"),
            Workout(id=ObjectId(), name="Swimming Training", description="Training for a swimming competition"),
        ]
        
        for workout in workouts:
            workout.save()
            
        self.stdout.write(self.style.SUCCESS('Successfully populated database with test data for the OctoFit Tracker application.'))