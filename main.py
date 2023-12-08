# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re

def simple_chatbot(user_input):
    # Define patterns and responses
    patterns = {
        'greeting': re.compile(r'\b(?:hi|hello|hey)\b', re.IGNORECASE),
        'goodbye': re.compile(r'\b(?:bye|goodbye)\b', re.IGNORECASE),
        'age_question': re.compile(r'\b(?:how old are you|your age)\b', re.IGNORECASE),
        'default': re.compile(r'.*')
    }

    responses = {
        'greeting': 'Hello! How can I help you?',
        'goodbye': 'Goodbye! Have a great day!',
        'age_question': "I'm just a computer program, so I don't have an age.",
        'default': "I'm sorry, I didn't understand that."
    }

    # Match user input to patterns
    for pattern_key, pattern in patterns.items():
        if re.search(pattern, user_input):
            return responses[pattern_key]

    # Default response for unmatched input
    return responses['default']

# Interactive chat with the user
print("Hello! This is a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Goodbye! Chatbot session ended.")
        break

    response = simple_chatbot(user_input)
    print("Bot:", response)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
