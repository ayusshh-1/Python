🧠 Day29 Capstone Project – Hindi-English Flash Card App
This is a language learning flash card application built with Python and Tkinter as part of the 100 Days of Code challenge. The app is specifically designed to help Hindi speakers learn English vocabulary in an interactive and visual way.

🚀 Features
🗂 Displays a random Hindi word from the dataset.

⏱ Automatically flips the flash card to reveal the English translation after 3 seconds.

✅ Click “Known” to remove the word from future practice (it won’t repeat).

❌ Click “Don’t Know” to save the word pair in a text file for later revision.

🎯 Purpose
This tool is intended to help Hindi-speaking learners improve their English vocabulary by actively recalling translations and tracking difficult words for review.

📋 How to Use
Before You Start:

⚠️ Manually clear the contents of not_known_words.txt before each session for accurate progress tracking.

Start Learning:

A Hindi word appears on the front of a flash card.

After 3 seconds, the card flips to reveal the English meaning.

Respond with Buttons:

✅ Known: Removes the word from the list.

❌ Don’t Know: Saves the Hindi-English word pair to not_known_words.txt.

🗃️ Project Structure
Day29 Capstone Project- Flash Card/

├── Data/

│   ├── Hindi_Words.csv           # Dataset with Hindi-English word pairs

│   └── not_known_words.txt       # Stores words the user didn’t know (should be cleared before each run)

├── images/

│   ├── card_back.png             # Flash card back image

│   ├── card_front.png            # Flash card front image


│   ├── right.png                 # Tick button (Known)
│   └── wrong.png                 # Cross button (Don't Know)

└── main.py                       # Main Python application

💡 Requirements
Python 3.x

pandas library

tkinter (built-in with Python)
Install dependencies (if needed):
pip install pandas

▶️ How to Run
Make sure you are in the project directory and run:
python main.py




