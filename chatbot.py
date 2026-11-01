
import re
import random

# Intents and responses
intents = {
    'greeting': {
        'patterns': ['hello', 'hi', 'hey'],
        'responses': ['Hello!', 'Hi there!', 'Hey!']
    },
    'farewell': {
        'patterns': ['bye', 'goodbye'],
        'responses': ['Goodbye!', 'Take care!']
    },
    'thanks': {
        'patterns': ['thanks', 'thank you'],
        'responses': ['Welcome!', 'Happy to help!']
    },
    'help': {
        'patterns': ['help me', 'need help'],
        'responses': ['Sure! How can I help?']
    }
}

# Preprocessing
def prosessing(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text.split()


#pattern matching

def match_intent(words):
    for intent, data in intents.items():
        for pattern in data['patterns']:
            if all(w in words for w in prosessing(pattern)):
                return intent
            
    return None

def chatbot():
    print("Chatbot: Hello! Type bye to exit.")
    
    while True:
        user = input("You: ")
        
        
        if user.lower().strip() == 'bye':
            print("Chatbot: Goodbye!")
            break
        
        
        intent = match_intent(prosessing(user))
        
        if intent:
            print("Chatbot:", random.choice(intents[intent]['responses']))
            
        else:
            print("Chatbot: Sorry, i dont understand.")
            
            
            
chatbot()
        
        
