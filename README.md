# BookBot

BookBot is a Python utility that analyzes the contents of a book and generates a report showing:

- Total word count  
- Frequency of each alphabetic character (case-insensitive)  
- Sorted character frequency in descending order  

This project is ideal for practicing file I/O, dictionary manipulation, sorting, and modular design in Python.

---

## How It Works

BookBot reads a `.txt` file, processes its contents, and prints a formatted report to the console. It uses three modules:

- `main.py`: Orchestrates the workflow and prints the final report  
- `stats.py`: Contains logic for word counting and character frequency analysis  
- `book_text.py`: Handles reading the book file from disk  

---

## Requirements

- Python 3.10 or later  
- A `.txt` file placed inside a `books/` directory  

No external libraries are required.

---

## How to Run

1. Clone or download this repository  
2. Place your `.txt` file inside the `books/` folder  
3. Update the `path` variable in `main.py` if needed  
4. Run the script:

```bash
python main.py
