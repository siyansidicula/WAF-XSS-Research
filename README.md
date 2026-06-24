# WAF XSS Filter Analysis Project

## Overview

This project demonstrates a basic Web Application Firewall (WAF) filtering system using Python and Flask.

The application analyzes user input and classifies it as **Allowed** or **Blocked** based on predefined security rules.

## Objective

- Understand the working of Web Application Firewalls
- Study basic XSS detection mechanisms
- Implement a simple input filtering system
- Analyze how filters identify suspicious patterns

## Technologies Used

- Python 3
- Flask
- Visual Studio Code

## Project Structure

```
WAF-XSS-Research/
│
├── app.py
├── analyzer.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Files Description

### app.py
A Flask-based web application that simulates a simple WAF filter.

### analyzer.py
A Python script that tests different inputs and generates an analysis report.

### requirements.txt
Contains the required Python packages.

## Installation

Clone the repository:

```bash
git clone <repository-link>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Running Analyzer

Execute:

```bash
python analyzer.py
```

## Sample Output

```
Input : Hello World
Status: ALLOWED

Input : <example>
Status: BLOCKED
Reason: Matched '<'
```

## Result

The project successfully demonstrates how a simple WAF filter can detect and block suspicious input patterns.

## Conclusion

Basic character-based filtering helps identify risky inputs, but stronger security methods like input validation, output encoding, and security policies are required for real-world protection.

## Author

Cyan
