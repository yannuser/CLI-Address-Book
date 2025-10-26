# CLI Address Book (Python)

A simple **command-line address book** built in Python to practice key software engineering concepts such as  **object-oriented programming (OOP)** ,  **file I/O** ,  **JSON serialization** , and  **exception handling** .

---

## Features

* Add, search, delete, and list contacts
* Case-insensitive name and email search
* Data persistence using JSON
* Graceful exception handling (file not found, bad JSON, etc.)
* Clean modular OOP structure (`Contact` + `AddressBook`)
* Simple CLI user interface

---

## Learning Goals

* Apply OOP principles (encapsulation, modular design)
* Work with JSON read/write for persistent storage
* Implement error handling in real-world scenarios
* Structure a small CLI program with multiple files

---

## 🧩 Project Structure

```
address_book/
├── contact.py          # Contact class (data model)
├── address_book.py     # AddressBook class (manager)
├── main.py             # CLI interface
└── contacts.json       # Auto-generated JSON storage file
```

---

## ⚙️ How to Run

1. **Clone this repository:**

   ```bash
   git clone https://github.com/<your-username>/address_book.git
   cd address_book
   ```
2. **Run the app:**

   ```bash
   python main.py
   ```
3. **Follow the on-screen menu** to add, search, or delete contacts.

   Your data will be automatically saved to `contacts.json`.

---

## Requirements

* Python 3.10+
* No external libraries required (uses only built-in modules)

---

## License

This project is open source.
