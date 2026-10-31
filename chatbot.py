
import re
import random

# Step 1: Create intents and responses
intents = {
    'greeting': {
        'patterns': ['hello', 'hi', 'hey', 'good morning',
                     'good evening', 'good afternoon'],
        'responses': ['Hello!', 'Hi there!', 'Greetings!',
                      'Good day!', 'Hey! How can I help you?']
    },

    'farewell': {
        'patterns': ['bye', 'goodbye', 'see you later',
                     'farewell', 'take care'],
        'responses': ['Goodbye!', 'Take care!',
                      'See you later!', 'Have a great day!']
    },

    'thanks': {
        'patterns': ['thank you', 'thanks',
                     'thank you so much', 'thanks a lot'],
        'responses': ['You are welcome!', 'Glad I could help!',
                      'Anytime!', 'No problem!']
    },

    'bot_name': {
        'patterns': ['what is your name', 'who are you',
                     'tell me your name'],
        'responses': ['I am your friendly chatbot!',
                      'You can call me Chatbot!']
    },

    'bot_purpose': {
        'patterns': ['what can you do', 'how can you help me',
                     'what do you do'],
        'responses': ['I can answer basic questions!',
                      'I am here to help you.']
    },

    'feeling': {
        'patterns': ['how are you', 'how are you doing',
                     'are you okay'],
        'responses': ['I am doing great!',
                      'I am feeling helpful today!']
    },

    'age': {
        'patterns': ['how old are you', 'what is your age'],
        'responses': ['I do not have an age like humans!',
                      'I am a chatbot, so I have no age.']
    },

    'weather': {
        'patterns': ['what is the weather',
                     'how is the weather today'],
        'responses': ['Please check your weather app!',
                      'I cannot access live weather data.']
    },

    'joke': {
        'patterns': ['tell me a joke', 'make me laugh'],
        'responses': ['Why did the computer go to the doctor? '
                      'Because it had a virus!',
                      'I would tell you a UDP joke, but you might not get it!']
    },

    'help': {
        'patterns': ['help me', 'i need help',
                     'can you help me'],
        'responses': ['Sure! How can I help you?',
                      'Of course! Tell me what you need.']
    }
}


# Step 2: Preprocess user input
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return tokens


# Step 3: Match user input with predefined patterns
def match_intent(processed_input, intents):
    for intent, intent_data in intents.items():
        for pattern in intent_data['patterns']:
            processed_pattern = preprocess(pattern)

            if all(word in processed_input
                   for word in processed_pattern):
                return intent

    return None


# Step 4: Generate response
def get_response(intent, intents):
    return random.choice(intents[intent]['responses'])


# Step 5: Run chatbot
def chatbot():
    print("Hello! I am Chatbot. Type bye to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() == 'bye':
            print("Chatbot: Goodbye!")
            break

        processed_input = preprocess(user_input)

        matched_intent = match_intent(processed_input, intents)

        if matched_intent:
            response = get_response(matched_intent, intents)
            print("Chatbot:", response)
        else:
            print("Chatbot: Sorry, I could not understand that.")


# Run the chatbot
chatbot()
