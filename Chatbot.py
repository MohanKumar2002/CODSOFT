def chatbot_response(user_input):
    user_input = user_input.lower()  
    greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']
    farewell = ['bye', 'goodbye', 'see you later', 'see ya']
    gratitude = ['thank you', 'thanks', 'thanks a lot']
    inquiries = ['how are you?', 'what are you doing?', 'what can you do?']
    reference = ['who created you?' ]
    help_keywords = ['help', 'assist', 'support']
    if user_input in greetings:
        return "Hello there! How can I assist you?"
    elif user_input in farewell:
        return "Goodbye! Have a great day!"
    elif user_input in gratitude:
        return "You're welcome!"
    elif user_input in reference:
        return "I was created by Mohan."
    elif any(inquiry in user_input for inquiry in inquiries):
        return "I am just a simple chatbot created to assist you."
    elif any(keyword in user_input for keyword in help_keywords):
        return "Of course! How can I help you today?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"
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