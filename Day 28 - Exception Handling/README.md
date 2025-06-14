📌 Topic: Exception Handling in Python
Today I learned about handling exceptions in Python using the following keywords:

try

except

else

finally

These constructs help manage runtime errors gracefully and make the program more robust and user-friendly.

📘 Concepts Covered
Catching specific exceptions like FileNotFoundError, ZeroDivisionError, ValueError , JSONDecoderError

Using else to execute code only when no exceptions occur

Using finally to ensure certain code always runs (e.g., cleanup)

Writing clear, informative error messages

✅ Practical Application
I applied these concepts in the Password Manager app I built on Day 27. Here's how:

Handled FileNotFoundError when data.json doesn't exist

Managed JSONDecodeError if the JSON file is empty or malformed

Used try/except to prevent crashes and inform users via Tkinter message boxes

This made the app more stable and user-friendly.

📄 Resources
Notes and examples are documented in a separate file: day28_exception_handling.txt

🔗 Related Work
✅ Day 27 - Password Manager

🧠 Reflection
Learning how to handle exceptions properly made me more confident in building real-world Python apps. It’s a key step toward writing production-level code that doesn’t break easily.
