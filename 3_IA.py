import random
import os
import requests
import tkinter as tk
from tkinter import simpledialog, messagebox

class BasicAI:
    def __init__(self, responses_file='responses.txt'):
        self.responses_file = responses_file
        self.responses = self.load_responses()
        self.feedback_file = 'feedback.txt'
        self.feedback = self.load_feedback()

    def load_responses(self):
        if os.path.exists(self.responses_file):
            with open(self.responses_file, 'r') as file:
                return [line.strip() for line in file.readlines()]
        else:
            return [
                "Hola, ¿cómo estás?",
                "Estoy aquí para ayudarte.",
                "¿En qué puedo asistirte hoy?",
                "¡Que tengas un buen día!"
            ]

    def save_response(self, response):
        with open(self.responses_file, 'a') as file:
            file.write(response + '\n')
        self.responses.append(response)

    def load_feedback(self):
        if os.path.exists(self.feedback_file):
            with open(self.feedback_file, 'r') as file:
                return [line.strip() for line in file.readlines()]
        else:
            return []

    def save_feedback(self, feedback):
        with open(self.feedback_file, 'a') as file:
            file.write(feedback + '\n')
        self.feedback.append(feedback)

    def get_response(self, user_input):
        # Search Wikipedia for the user input
        search_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={user_input}&limit=1&format=json"
        response = requests.get(search_url)
        data = response.json()

        if data[1]:
            summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{data[1][0]}"
            summary_response = requests.get(summary_url)
            summary_data = summary_response.json()
            summary = summary_data.get('extract', 'No se encontró información.')
            return f"He encontrado algo sobre {data[1][0]}: {summary}"
        else:
            return random.choice(self.responses)

    def train(self):
        # Simple training mechanism based on feedback
        positive_feedback = [fb for fb in self.feedback if 'good' in fb]
        negative_feedback = [fb for fb in self.feedback if 'bad' in fb]

        if positive_feedback:
            self.responses.extend(positive_feedback)
        if negative_feedback:
            for fb in negative_feedback:
                if fb in self.responses:
                    self.responses.remove(fb)

    def interact(self):
        root = tk.Tk()
        root.withdraw()
        while True:
            user_input = simpledialog.askstring("Input", "You: ")
            if user_input is None:  # User closed the dialog
                break
            response = self.get_response(user_input)
            messagebox.showinfo("Response", f"AI: {response}")
            feedback = simpledialog.askstring("Feedback", "Was this response good or bad?")
            if feedback:
                self.save_feedback(feedback)
                self.train()

    def interact_with_another_ai(self, other_ai, iterations=10):
        for _ in range(iterations):
            user_input = random.choice(self.responses)
            response = other_ai.get_response(user_input)
            feedback = random.choice(["good", "bad"])
            self.save_feedback(feedback)
            self.train()
            other_ai.save_feedback(feedback)
            other_ai.train()

if __name__ == "__main__":
    ai1 = BasicAI(responses_file='responses1.txt')
    ai2 = BasicAI(responses_file='responses2.txt')
    ai1.interact_with_another_ai(ai2, iterations=10)
    ai1.interact()