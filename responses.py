# responses.py


import random


# Motivational messages
motivational_messages = [
    "You're doing great! Keep it up ",
    "Believe in yourself! ",
    "Every day is a new opportunity ",
    "Keep going, success is near ",
    "Your efforts are paying off! "
]


# Daily quotes
daily_quotes = [
    "Quote of the day: Dream big!",
    "Quote of the day: Keep learning.",
    "Quote of the day: Smile often "
]


# Mini challenges
mini_challenges = [
    "Take a deep breath and smile ",
    "Write down one thing you're grateful for today ",
    "Stretch for 30 seconds "
]


# Function to get a random motivational message
def get_motivation():
    return random.choice(motivational_messages)


# Function to get daily quotes
def get_daily_quotes():
    return daily_quotes


# Function to get a random challenge
def get_challenge():
    return random.choice(mini_challenges)

