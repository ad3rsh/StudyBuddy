from textblob import TextBlob
import random

# Pre-defined motivational and study tips
positive_responses = [
    "Awesome! Keep up the great work! 💪",
    "You're on fire! 🔥 Don't stop now.",
    "Love your energy! Stay focused and keep learning. 📚",
    "You're doing amazing. Keep pushing forward! 🚀"
]

neutral_responses = [
    "Staying consistent is key. 📆 Try setting a short study goal today.",
    "Take a 5-minute break, then get back to it with a fresh mind. ☕",
    "Even small steps count! What's your next task? 📝",
    "Try using the Pomodoro technique to stay productive. ⏱️"
]

negative_responses = [
    "It's okay to feel down. Take a short break and come back stronger. 💖",
    "Remember why you started. You’ve got this! 🌟",
    "Try switching subjects or tasks to refresh your brain. 🧠",
    "Every expert was once a beginner. Don’t give up. 🌱"
]

def get_response(sentiment):
    if sentiment > 0.2:
        return random.choice(positive_responses)
    elif sentiment < -0.2:
        return random.choice(negative_responses)
    else:
        return random.choice(neutral_responses)

def study_buddy_chat():
    print("📘 Study Buddy: Hi there! I’m your study companion. Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Study Buddy: 👋 Bye for now! Stay productive!")
            break

        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity

        response = get_response(sentiment)
        print(f"Study Buddy: {response}\n")

if __name__ == "__main__":
    study_buddy_chat()
