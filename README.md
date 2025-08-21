# BookBot

BookBot is a Python utility that analyzes the contents of a book and generates a report showing:

- Total word count  
- Frequency of each alphabetic character (case-insensitive)  
- Sorted character frequency in descending order  

This project is ideal for practicing file I/O, dictionary manipulation, sorting, and modular design in Python.

---

## How It Works

BookBot reads a `.txt` file passed as a command-line argument, processes its contents, and prints a formatted report to the console. It uses three modules:

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
3. Run the script from the command line, passing the path to the book file:

```bash
python main.py books/frankenstein.txt
```

---

## Sample Output
<img width="846" height="240" alt="image" src="https://github.com/user-attachments/assets/3393993b-7704-44af-b4ae-b4471f12f366" />
