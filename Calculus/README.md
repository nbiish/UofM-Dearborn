# Calculus Study and In-Class Notes

Welcome to the Calculus repository for UofM-Dearborn Fall 2024. This repository contains study materials, in-class notes, and homework assignments to help you succeed in your Calculus course.

## Repository Structure

The repository is organized into the following directories:

- **quiz-studying**: Contains Python scripts for solving calculus problems step-by-step, with detailed explanations and visualizations.
    - `4.3/`: Problems related to section 4.3 of the course.
        - `4.3-Q1.py`
        - `4.3-Q4.py`
        - `4.3-Q7.py`
        - `4.3-Q8.py`

- **in-class**: Contains notes and examples discussed during class sessions.
    - `11-14-24/`: Notes from the class on November 14, 2024.
    - `11-21-24/`: Notes from the class on November 21, 2024.

- **homework**: Contains Jupyter notebooks and scripts for homework assignments.
    - `4.7.ipynb`

## Development Environment Setup

To install dependencies and set up your environment:

```sh
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

```sh
# Install dependencies
uv add -r requirements.txt

# Create and activate a new virtual environment
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

Make sure you have Python 3.8 or higher installed on your system.

## Usage

### Running Python Scripts

To run the Python scripts in the `quiz-studying` directory, navigate to the appropriate folder and execute the script using Python:

```sh
cd Calculus/quiz-studying/4.3
uv run 4.3-Q1.py
```
