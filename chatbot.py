import re
from datetime import datetime

def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        # Exit
        if user_input == 'exit':
            print("Chatbot: Goodbye! 👋")
            break

        # Greetings
        elif re.search(r"\b(hi|hello|hey|good morning|good evening)\b", user_input):
            print("Chatbot: Hi there! How can I help you today?")

        # Identity
        elif re.search(r"\b(who are you|what are you)\b", user_input):
            print("Chatbot: I'm a basic rule-based chatbot built with Python.")

        # Time
        elif re.search(r"\b(time)\b", user_input):
            now = datetime.now().strftime("%H:%M")
            print(f"Chatbot: The current time is {now}.")

        # Weather (placeholder)
        elif re.search(r"\b(weather|temperature)\b", user_input):
            print("Chatbot: I can't access real weather, but it's always sunny in here ☀️!")

        # Help
        elif re.search(r"\b(help|support|assist)\b", user_input):
            print("Chatbot: You can ask me about time, greetings, or who I am!")

        # Fallback
        else:
            print("Chatbot: I'm not sure I understand. Can you try saying that differently?")

# Run chatbot
chatbot()