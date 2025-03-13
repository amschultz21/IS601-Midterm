# Calculator REPL Application

A robust, interactive calculator application implemented in Python that leverages several design patterns (Facade, Command, Factory, Singleton, and Strategy) for flexibility and scalability. The application also incorporates advanced logging and plugin mechanisms, enabling dynamic command loading and efficient history management via Pandas.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage Examples](#usage-examples)
- [Architectural Decisions](#architectural-decisions)
  - [Design Patterns](#design-patterns)

## Overview

This Calculator REPL application provides an interactive command-line interface for performing basic arithmetic operations (addition, subtraction, multiplication, division) with advanced features including:
- **Dynamic Plugin Loading:** Easily extend the application by adding new commands (plugins).
- **History Management:** Stores calculation history using Pandas with options to load, save, clear, and delete records.
- **Multiprocessing:** Commands are executed on separate cores for enhanced performance.
- **Logging:** Detailed logging of user interactions and errors for debugging and audit purposes.
- **Design Patterns:** Uses the Facade, Command, Factory, Singleton, and Strategy patterns to achieve a modular, scalable design.

## Features

- **Interactive REPL Interface:**  
  - Execute arithmetic operations and view results in real time.
  - Display a dynamic menu for available commands.
- **Plugin Support:**  
  - Auto-load plugins from the `calculator/plugins` directory.
  - Easily add new operations without modifying core code.
- **History Management:**  
  - Utilize a Pandas DataFrame to manage and persist calculation history.
  - Options to view, save, clear, and delete history records.
- **Multiprocessing Execution:**  
  - Offload command execution to separate processes, improving performance.
- **Robust Logging:**  
  - Log system events, errors, and user interactions in a structured format.
- **Design Patterns:**  
  - **Facade:** Simplifies complex Pandas data manipulations via a `HistoryFacade`.
  - **Command:** Encapsulates operations as command objects.
  - **Factory Method:** Creates commands dynamically based on user input.
  - **Singleton:** Ensures a single instance of the Calculator for centralized history management.
  - **Strategy:** Provides flexibility in history management approaches.

## Setup Instructions

### Prerequisites

- Python 3.10 or later.
- [Pip](https://pip.pypa.io/en/stable/installation/).

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/IS601-Midterm.git
   cd IS601-Midterm

2. **Install Dependencies**
    pip install -r requirements.txt

3. **Create .env File**

## Usage Examples

### Running the REPL
1. python -m calculator.repl 

### Running Tests
1. pytest
2.  pytest --pylint
3. pytest --pylint --cov

## Architectural Decisions

### Design Patterns
1. Facade Pattern
2. Command Pattern
3. Factory Method
4. Singleton Pattern
5. Strategy Pattern


