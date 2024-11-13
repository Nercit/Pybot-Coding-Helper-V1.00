


import random
import time
import openai
from difflib import SequenceMatcher
# Set your OpenAI API key
openai.api_key = "ipa-key-here"

class PyBot:
    def __init__(self, name="PyBot"):
        self.name = name
        self.user_name = None
        self.skill_level = None
        self.context = {}  # Store context of the conversation
        self.memory = {}  # Memory to store questions and answers
        self.responses = {
            "greet": [
                "Hello, coder! How can I help you today?",
                "Hi there! I'm PyBot, your coding assistant. What do you need help with?",
                "Hey, what’s up? How’s the code going?"
            ],
            "bye": [
                "Goodbye, coder! Keep up the great work!",
                "See you later! Happy coding!",
                "Take care, coder! I’ll be here when you need me."
            ],
            "error": [
                "It looks like there’s an error. Let me help with that!",
                "Oops, an error! No worries, I’ve got your back!"
            ],
            "motivation": [
                "You’re doing amazing! Keep going!",
                "Every coder has challenges, but you’ve got this!",
                "You’re on the right track. Keep pushing forward!"
            ],
            "help": [
                "Of course! What do you need help with? Feel free to ask me anything!",
                "I’m here to help! What do you need assistance with today?"
            ],
            "explain": [
                "Got it! Let me explain that concept for you.",
                "Sure! I’ll explain that as simply as possible."
            ]
        }

    def greet_user(self):
        """Personalized greeting based on the time of day."""
        hour = time.localtime().tm_hour
        if 5 <= hour < 12:
            return f"Good morning, {self.user_name}! How can I assist you today?"
        elif 12 <= hour < 18:
            return f"Good afternoon, {self.user_name}! Ready to tackle some coding challenges?"
        else:
            return f"Good evening, {self.user_name}! How’s the coding going?"

    def ask_name(self):
        """Ask for the user's name to personalize conversations."""
        if not self.user_name:
            self.user_name = input("Hi! What's your name, coder? ")
            print(f"Nice to meet you, {self.user_name}! I'm PyBot, your coding assistant.")
    
    def ask_skill_level(self):
        """Ask for the user's coding skill level."""
        if not self.skill_level:
            self.skill_level = input("What is your coding skill level? (beginner/intermediate/advanced): ").lower()
            print(f"Awesome, {self.user_name}! I’ll tailor my help to your skill level of {self.skill_level}.")

    def add_to_memory(self, question, answer):
        """Store the question and answer in memory."""
        self.memory[question] = answer

    def check_memory(self, question):
        """Check if the question is already in memory and provide an answer."""
        for stored_question in self.memory:
            if self.is_similar(question, stored_question):
                return self.memory[stored_question]
        return None

    def is_similar(self, question1, question2):
        """Check if two questions are similar using sequence matching."""
        return SequenceMatcher(None, question1.lower(), question2.lower()).ratio() > 0.7  # 70% similarity

    def get_gpt_response(self, prompt):
        """Get response from GPT-3 (OpenAI) based on the user's question."""
        try:
            # Use OpenAI GPT model to generate a response
            response = openai.Completion.create(
                engine="text-davinci-003",  # You can change to another engine if needed
                prompt=prompt,
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return "Sorry, I couldn't process your request right now. Please try again later."

    def handle_conversation(self, user_input):
        """Handle user inputs with responses."""
        # Check memory first
        memory_answer = self.check_memory(user_input)
        if memory_answer:
            return f"I remember you asked something similar earlier: {memory_answer}"

        # Ask GPT for a dynamic response to any coding question
        gpt_response = self.get_gpt_response(f"Answer this coding question: {user_input}")
        self.add_to_memory(user_input, gpt_response)  # Store in memory for future reference
        return gpt_response

    def run(self):
        """Main interaction loop."""
        self.ask_name()
        self.ask_skill_level()

        print(self.greet_user())

        while True:
            user_input = input(f"{self.user_name}: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print(random.choice(self.responses["bye"]))
                break

            print(f"{self.name}: {self.handle_conversation(user_input)}\n")

if __name__ == "__main__":
    pybot = PyBot()
    pybot.run()
