# Scenario_1

## Overview ✅
A sample workspace demonstrating Git branching workflows and containing example files in multiple languages (HTML, C++, Java, Python) with accompanying documentation.

## Project Structure 📁

### Main Branch Files 🔧
* **`index.html`** — Interactive HTML page (open in a browser)
* **`main.cpp`** — C++ implementation of the Two Sum algorithm (O(n) complexity)
  - Compile: `g++ main.cpp -o main`
  - Run: `./main` (Linux/Mac) or `.\main` (Windows)
* **`Main.java`** — Java program to find the second largest element without sorting
  - Compile: `javac Main.java`
  - Run: `java Main`
* **`script.py`** — Python script with functionality
  - Run: `python script.py`
* **`notes.txt`** — Plain-text project notes
* **`info.txt`** — File descriptions and documentation
* **`.git/`** — Git metadata (hidden folder for version control)

## Branch Information 🌿

### `new-feature` Branch
- **Purpose**: Calculator implementation
- **Changes**: Enhanced `script.py` with calculator functionality
- **Features**: Basic arithmetic operations (add, subtract, multiply, divide)

### `nf-1` Branch
- **Base Branch**: `new-feature`
- **Purpose**: Timetable feature
- **Changes**: Replaced `index.html` content with weekly timetable
- **Features**: Responsive HTML table with styled schedule

## Getting Started 🚀

### Clone the Repository
```bash
