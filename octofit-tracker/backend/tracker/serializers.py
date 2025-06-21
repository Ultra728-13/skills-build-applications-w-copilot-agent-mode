from rest_framework import serializers

# User Serializer
class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    # Add other user fields as needed

# Team Serializer
class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField())

# Activity Serializer
class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    date = serializers.DateField()

# Leaderboard Serializer
class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    team_id = serializers.CharField()
    score = serializers.IntegerField()

# Workout Serializer
class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    workout_type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    date = serializers.DateField()
