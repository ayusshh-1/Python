🚴 Day 35 – Pixela Habit Tracker (Using Python)
Today I built a simple habit tracking tool using the Pixela API, which allows users to record and visualize their daily progress (e.g., kilometers cycled). This tool interacts with the Pixela service using HTTP requests to:

Create a user account

Define a graph (e.g., for cycling)

Post daily activity data (as "pixels")

Update or delete entries

📌 Features
✅ Create a new Pixela user
✅ Define a graph for a specific activity (e.g., cycling)
✅ Add today's data (e.g., kilometers cycled)
✅ Update today's data if needed
✅ Delete today's data if entered incorrectly

🧠 Concepts Practiced
Python requests library for making API calls (POST, PUT, DELETE)

Using Python's datetime to get today's date

REST API structure

JSON data formatting

Handling user input

Basic token-based authentication

🔧 How to Use
Step 1: Install the required library
pip install requests
Step 2: Replace the following variables in the code:
TOKEN = "your_custom_token_here"        # 8-128 characters
USER_NAME = "your_pixela_username"      # Must be unique on Pixela
Graph_id = "your_graph_id"              # e.g., "cyclinggraph"
graph_name = "Your graph name here"     # e.g., "Cycling Tracker"
Step 3: Run the Script
When you run it:

It will create your Pixela user (if not already created)

Create a graph

Ask you how many kilometers you cycled today

Post that data

Optionally update or delete today's entry

🔗 Pixela Graph Preview
You can view your activity graph here:
https://pixe.la/v1/users/<YOUR_USERNAME>/graphs/<GRAPH_ID>.html
Example:
https://pixe.la/v1/users/ayush123/graphs/cyclinggraph.html

📷 Output Example
Enter the km you cycled today: 6.4
{"message":"Success!","isSuccess":true}

🏁 Final Thoughts
Today’s project was a fun way to interact with APIs and track real-life activities using simple Python scripts. It’s a great example of how tech can be used for self-discipline and daily motivation.


