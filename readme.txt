Event Viewer AI Analysis Tool
This repository contains a suite of Python scripts designed to parse, analyze, and interact with Windows Event Viewer logs using AI techniques. The toolset includes a script for parsing event logs, a GUI for drag-and-drop functionality, an AI chatbot for querying log data, and a Flask server to host the chatbot interface.

Files Description
EventLogXMLToJsonParser.py: Parses XML Event Viewer logs and converts them to JSON format.
aiBot.py: Provides a GUI for drag-and-drop functionality to process Event Viewer logs.
aichat.py: An AI chatbot script that uses OpenAI's GPT-3.5 model to answer questions about the event logs.
app.py: A Flask application that serves as the backend for the AI chatbot.
requirements.txt: Lists all Python dependencies required for the scripts.
Setup Instructions
Clone the Repository:

bash
Copy code
git clone https://github.com/Chertus/EventViewerAI.git
cd EventViewerAI
Create and Activate a Virtual Environment (Optional but Recommended):

Windows:
Copy code
python -m venv venv
venv\Scripts\activate
macOS/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

Copy code
pip install -r requirements.txt
Set Up Environment Variables:

You need to set the OPENAI_API_KEY environment variable with your OpenAI API key.
Windows: set OPENAI_API_KEY=your_api_key
macOS/Linux: export OPENAI_API_KEY=your_api_key
Running the Scripts:

To parse event logs: python EventLogXMLToJsonParser.py <path_to_event_log>
To use the AI bot GUI: python aiBot.py
To start the Flask server for the AI chatbot: python app.py
Usage
EventLogXMLToJsonParser.py: Drag and drop an XML Event Viewer log file onto the script or run it from the command line with the file path as an argument.
aiBot.py: Run the script and use the GUI to drag and drop zip files containing event logs for processing.
aichat.py: This script is used by app.py to provide AI chatbot functionality.
app.py: Run this script to start a local server. Access the AI chatbot by navigating to http://localhost:5000 in your web browser.
Suggested Future Improvements
Enhanced AI Chatbot Capabilities: Improve the AI chatbot's ability to provide more accurate and context-aware responses.
Database Integration: Store processed log data in a database for more efficient querying and management.
User Authentication: Implement user authentication for the Flask server to restrict access and enhance security.
Automated Log Collection: Develop a feature for automated collection of Event Viewer logs from specified servers or systems.
Advanced Data Visualization: Integrate data visualization tools to provide graphical representations of log data and analysis results.