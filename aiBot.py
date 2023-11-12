import json
import pandas as pd
import os
from openai import ChatCompletion
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def analyze_logs(file_path):
    logs = pd.read_json(file_path)
    categorized_logs = categorize_logs(logs)
    enriched_logs = enrich_data_with_gpt(categorized_logs)
    save_to_json(enriched_logs, 'enriched_logs.json')
    show_gui(enriched_logs)

def categorize_logs(logs):
    logs['Category'] = logs.apply(determine_category, axis=1)
    return logs

def determine_category(log):
    # Example categorization logic
    if 'error' in log['Message'].lower():
        if 'application' in log['Source'].lower():
            return 'Application Errors'
        elif any(word in log['Message'].lower() for word in ['access', 'security', 'authentication']):
            return 'Security and Access Issues'
        elif 'network' in log['Message'].lower():
            return 'Network Problems'
        elif any(word in log['Message'].lower() for word in ['hardware', 'disk', 'memory']):
            return 'Hardware Malfunctions'
        else:
            return 'System Errors'
    else:
        return 'Performance Issues'

def enrich_data_with_gpt(logs):
    openai_api_key = os.getenv('OPENAI_API_KEY')
    gpt = ChatCompletion(api_key=openai_api_key)

    for index, log in logs.iterrows():
        query = formulate_query(log)
        try:
            response = gpt.create(prompt=query, model="gpt-3.5-turbo", max_tokens=100)
            logs.at[index, 'gpt_response'] = response.choices[0].message.content
        except Exception as e:
            logs.at[index, 'gpt_response'] = f"Error: {e}"

    return logs

def save_to_json(data, file_name):
    data.to_json(file_name, orient='records', lines=True, indent=4)

def formulate_query(log):
    return f"What are the potential causes and solutions for this error? \n\nError Details: {log['Message']}"

def show_gui(logs):
    root = tk.Tk()
    root.title("Event Log Analysis")
    create_visualizations(root, logs)
    root.mainloop()

def create_visualizations(root, logs):
    # Example: Bar chart for issues per category
    category_counts = logs['Category'].value_counts()
    fig, ax = plt.subplots()
    category_counts.plot(kind='bar', ax=ax)
    ax.set_title("Issues per Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Count")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Example usage
analyze_logs('event_logs.json')
