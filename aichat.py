import json
import pandas as pd
from openai import ChatCompletion
import os

class AIChatBot:
    def __init__(self, data_file, openai_api_key):
        self.data = pd.read_json(data_file, lines=True)
        self.gpt = ChatCompletion(api_key=openai_api_key)

    def ask_question(self, question):
        relevant_data = self.find_relevant_data(question)
        gpt_query = self.create_gpt_query(question, relevant_data)
        response = self.gpt.create(prompt=gpt_query, model="gpt-3.5-turbo", max_tokens=150)
        return response.choices[0].message.content

    def find_relevant_data(self, question):
        # Implement logic to find data relevant to the question
        # Placeholder logic - refine based on your data structure
        relevant_data = self.data[self.data['Message'].str.contains(question, case=False)]
        return relevant_data

    def create_gpt_query(self, question, relevant_data):
        # Combine the question with relevant data to create a GPT-3.5 query
        # Placeholder logic - refine as needed
        context = relevant_data['Message'].str.cat(sep=' ')
        return f"{question}\n\nContext: {context}"

# Example usage
if __name__ == "__main__":
    openai_api_key = os.getenv('OPENAI_API_KEY')
    chatbot = AIChatBot('enriched_logs.json', openai_api_key)
    question = input("Ask me anything about the event logs: ")
    answer = chatbot.ask_question(question)
    print(answer)
