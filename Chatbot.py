def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for easier comparison
    # Define some rules and responses
    greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']
    farewell = ['bye', 'goodbye', 'see you later', 'see ya']
    gratitude = ['thank you', 'thanks', 'thanks a lot']
    inquiries = ['how are you?', 'what are you doing?', 'what can you do?']
    reference = ['who created you?' ]
    weather_keywords = ['weather', 'temperature', 'forecast']
    joke_keywords = ['joke', 'funny']
    love_keywords = ['love', 'like', 'adore', 'affection']
    hate_keywords = ['hate', 'dislike', 'detest']
    help_keywords = ['help', 'assist', 'support']
    
    # Check user input against predefined rules and generate responses accordingly
    if user_input in greetings:
        return "Hello there! How can I assist you today?"
    elif user_input in farewell:
        return "Goodbye! Have a great day!"
    elif user_input in gratitude:
        return "You're welcome!"
    elif user_input in reference:
        return "I was created by Mohan."
    elif any(inquiry in user_input for inquiry in inquiries):
        return "I am just a simple chatbot created to assist you. Feel free to ask me anything!"
    elif any(keyword in user_input for keyword in weather_keywords):
        return "I'm sorry, I can't provide weather information at the moment."
    elif any(keyword in user_input for keyword in joke_keywords):
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif any(keyword in user_input for keyword in love_keywords):
        return "Love is a beautiful thing!"
    elif any(keyword in user_input for keyword in hate_keywords):
        return "Hate is a strong word. Let's focus on positivity instead."
    elif any(keyword in user_input for keyword in help_keywords):
        return "Of course! How can I help you today?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

# Main function to run the chatbot
def main():
    print("Welcome! I am a simple chatbot. You can start chatting with me.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
