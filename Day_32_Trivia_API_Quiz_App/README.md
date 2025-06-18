🧠 Trivia API Quiz App
A simple and interactive quiz application built using Python and Tkinter. This app fetches trivia questions from an API and presents them with a graphical interface, allowing users to test their knowledge in a fun way.
![image](https://github.com/user-attachments/assets/3118c231-a450-43f2-ba50-8a50690f5a7c)

🚀 Features
Fetches quiz questions using the Open Trivia API

Clean and user-friendly GUI using Tkinter

Displays current score and tracks progress

Visual feedback:

✅ Correct answers turn the question area green

❌ Wrong answers turn it red

Uses OOP principles with organized class-based design
📁 Project Structure
Day 34 Trivia API Quiz App/
│
├── images/
│   ├── true.png         # Image shown when the user selects 'True'
│   └── false.png        # Image shown when the user selects 'False'
│
├── data.py              # Handles loading quiz data from the API
├── main.py              # Entry point for the app
├── question_model.py    # Defines the Question class
├── quiz_brain.py        # Contains quiz logic (checking answers, tracking score)
└── ui.py                # Handles the GUI with Tkinter

🔧 Requirements
Python 3.x

requests library (for API fetching)

Install the requests module:
pip install requests

▶️ How to Run
Clone this repository:
  git clone https://github.com/your-username/trivia-quiz-app.git
  cd trivia-quiz-app

Run the main script:
  python main.py

📚 Learnings
This app was built as part of the 100 Days of Code - Python Bootcamp by Angela Yu (Day 34). It emphasizes:

API data handling

Class inheritance

GUI development with Tkinter

Event-driven programming


