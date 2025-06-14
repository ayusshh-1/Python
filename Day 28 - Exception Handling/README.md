## 📌 Topic: Exception Handling in Python

Today I learned about handling exceptions in Python using the following keywords:

- `try`
- `except`
- `else`
- `finally`

These constructs help manage runtime errors gracefully and make the program more robust and user-friendly.

---

## 📘 Concepts Covered

- Catching specific exceptions like `FileNotFoundError`, `ZeroDivisionError`, `ValueError`, `JSONDecodeError`
- Using `else` to run code only if no exception occurs
- Using `finally` to always run a cleanup block (regardless of error)

---

## ✅ Practical Application

I implemented these concepts in the **Password Manager** project that I created on **Day 27**.

### Enhancements:
- Handled missing `data.json` using `try-except`
- Managed cases where JSON is empty or corrupted
- Provided user-friendly alerts using Tkinter

---

## 📄 Resources

- Notes and examples: [`day28_exception_handling.txt`](./day28_exception_handling.txt)

---

## 🔗 Related Project

- 🔐 [Day 27 - Password Manager](../Day%2027%20-%20Password%20Manager)

---

## 🧠 Reflection

Understanding exception handling has helped me write cleaner and more resilient Python programs. This will definitely make future projects easier to debug and maintain.
