print("Simple Chatbot")
responses = {
    "hi": "Hello! How can I assist you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you?": "I'm just a program, but thanks for asking! How about you?",
    "what is your name?": "I'm a simple chatbot. You can call me ChatBot!",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! If you have more questions, feel free to ask.",
    "what can you do?": "I can help you with a variety of questions and tasks!",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "what's the weather like?": "I can't check the weather, but you can check a weather app!",
    "help": "Sure! What do you need help with?",
    "who created you?": "I was created by a team of developers working on AI.",
    "what is your purpose?": "My purpose is to assist and provide information.",
    "can you speak other languages?": "I primarily communicate in English, but I can understand simple phrases in other languages.",
    "how old are you?": "I don't have an age like humans do, but I was created recently!",
    "what's your favorite color?": "I don't have preferences, but I think blue is nice!",
    "tell me something interesting": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient tombs that are over 3000 years old!",
    "what do you think about AI?": "AI has a lot of potential to improve lives and assist with tasks.",
    "can you help with math?": "Absolutely! Just tell me what math problem you need help with.",
    "what is 2 + 2?": "2 + 2 equals 4.",
    "how do I cook pasta?": "Boil water, add pasta, cook for 8-10 minutes, then drain and enjoy!",
    "what is your favorite food?": "I don't eat, but I hear pizza is quite popular!",
    "tell me a fact": "Octopuses have three hearts!",
    "do you like music?": "I don't have ears, but I know many people enjoy music!",
    "what is your favorite movie?": "I don't watch movies, but I can recommend popular ones!",
    "who is the president?": "I can't provide real-time information, but you can check the news for updates.",
    "where do you live?": "I exist in the digital world, so I don't have a physical location.",
    "what is your favorite book?": "I don't read books, but I know many classics!",
    "can you tell me a story?": "Once upon a time, in a digital realm, a chatbot helped users find answers to their questions...",
    "what's your favorite holiday?": "I don't celebrate holidays, but I hear many enjoy Christmas!",
    "how can I improve my productivity?": "Try setting clear goals, minimizing distractions, and taking regular breaks.",
    "what is mindfulness?": "Mindfulness is the practice of being present and fully engaging with the moment.",
    "can you give me advice?": "Sure! What do you need advice on?",
    "what is the meaning of life?": "Many say it's about finding happiness and purpose.",
    "can you play a game?": "I can play simple text-based games! Just let me know what you’d like to play.",
    "what is your favorite animal?": "I think dogs are wonderful companions!",
    "what is the best way to learn a new skill?": "Practice consistently and seek feedback from others.",
    "how do I stay motivated?": "Set achievable goals and celebrate small victories!",
    "what is your favorite sport?": "I don't play sports, but I know football (soccer) is very popular!",
    "how do I meditate?": "Find a quiet space, focus on your breath, and let thoughts come and go.",
    "what is your opinion on technology?": "Technology has transformed many aspects of life for the better.",
    "can you recommend a book?": "I recommend 'To Kill a Mockingbird'—a classic!",
    "what is your favorite quote?": "I like, 'The only limit to our realization of tomorrow is our doubts of today.'",
    "do you have feelings?": "I don't have feelings, but I can understand emotions in conversation.",
    "what is artificial intelligence?": "AI is the simulation of human intelligence processes by machines.",
    "how do I handle stress?": "Practice relaxation techniques, such as deep breathing or yoga.",
    "what is your favorite time of year?": "I don't experience seasons, but many enjoy spring for its beauty!",
    "what is a healthy diet?": "A balanced diet includes fruits, vegetables, whole grains, and proteins.",
    "can you help me with writing?": "Of course! What do you need help with in writing?",
    "what is your favorite thing about humans?": "I admire human creativity and problem-solving abilities.",
    "how do I stay healthy?": "Exercise regularly, eat well, and get enough sleep!",
    "what do you do when you're not chatting?": "I'm always here, ready to chat whenever you need!",
    "do you believe in aliens?": "I don't have beliefs, but many people find the idea fascinating!",
    "what's the best way to save money?": "Create a budget, track your spending, and set savings goals."
}

print("These are questions that I know how to answer:")
for key in responses.keys():
    print("-", key)

while True:
    ques = input("Enter your message\n>> ")

    if ques.lower().strip() == "bye":
        break

    response = responses.get(ques, "I'm sorry, I don't understand that.")
    print(response)