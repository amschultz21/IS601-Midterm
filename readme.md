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
    - pip install -r requirements.txt

3. **Create .env File**

## Usage Examples

### Running the REPL
1. python -m calculator.repl 

### Running Tests
1. pytest
2. pytest --pylint
3. pytest --pylint --cov

## Architectural Decisions

### Design Patterns
1. Facade Pattern
    - The HistoryFacade class simplifies interactions with Pandas for managing calculation history.
    - Implementation: calculator/history_facade.py
    - Description: Instead of exposing direct DataFrame manipulations, the facade provides clear methods (add_record, save, load, clear, delete_last) to simplify history management.
2. Command Pattern
    - The Command class encapsulates a calculation as an object that stores the operands and the operation.
    - Implementation: calculator/commands.py
    - Description: This pattern allows executing, storing, and reusing operations in a structured way.
3. Factory Method
    - The CommandFactory dynamically generates command objects based on user input.
    - Implementation: calculator/command_factory.py
    - Description: This allows new commands (operations) to be added with minimal changes to the core REPL.
4. Singleton Pattern
    - The Calculator class ensures only one instance manages history at a time.
    - Implementation: calculator/calculator.py
    - Description: This prevents inconsistencies in calculation history and ensures centralized management.
5. Strategy Pattern
    - Allows switching between different history management strategies (CSV-based now, but extendable to databases).
    - Implementation: calculator/history_facade.py
    - Description: By abstracting history management, different strategies (e.g., SQL-based storage) can be implemented without affecting the core calculator logic.

## Environment Variables

### Environment Variables

1. Implementation
    - calculator/repl.py
2. Description
    - The environment variable ENVIRONMENT is used to differentiate between development and production modes.
3. Code Example
    - import os
    - from dotenv import load_dotenv

    - load_dotenv()  # Load environment variables from .env file

    - environment = os.getenv("ENVIRONMENT", "development")  # Default to 'development'
    - print(f"Running in {environment} mode")
4. Usage
    - .env file contains ENVIRONMENT = local, this preents sensitive settings from being commited to the repository.

## Logging

### Logging
1. Implementation
    - calculator/repl.py
2. Description
    - Logs are stored in calculator.log, ensuring detailed records of calculations and errors.
3. Code
    - import logging

    - logging.basicConfig
        - filename="calculator.log",
        - level=logging.DEBUG,
        - format="%(asctime)s - %(levelname)s - %(message)s"
     - logging.info("Calculator started in interactive mode.")
4. Impact
    - Helps in debugging and tracking user actions.
    - Maintains an audit trail of operations.

## LBYL/EAFP

### Look Before You Leap
1. Implementation
    - calculator/calculator.py
2. Usage
    - Ensures division is not attempted when the divison is zero.

### Easier to Ask for Forgiveness than Permission
1. Implementation
    - calculator/repl.py
2. Usage
    - Instead of checking the validity of the input before each operation, the program assumes it's valid and catches errors if they occur.