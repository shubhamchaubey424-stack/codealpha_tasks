"""
TASK 4: Basic Chatbot
A simple rule-based chatbot using if-elif, functions, loops, and input/output.
"""

def get_response(user_input):
    """Takes user input and returns a predefined reply based on rules."""
    text = user_input.lower().strip()

    if text == "hello" or text == "hi":
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "bye":
        return "Goodbye!"
    elif text == "":
        return "Please type something."
    else:
        return "Sorry, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."


def chatbot():
    """Main loop that keeps the chatbot running until the user says bye."""
    print("Chatbot: Hi! I'm a simple chatbot. Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Chatbot:", reply)

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    chatbot()
