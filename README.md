# Calculus Study and In-Class Notes

Welcome to the Calculus repository for UofM-Dearborn Fall 2024. This repository contains study materials, in-class notes, and homework assignments to help you succeed in your Calculus course.

## Repository Structure

The repository is organized into the following directories:

- **quiz-studying**: Contains Python scripts for solving calculus problems step-by-step, with detailed explanations and visualizations.
- **in-class**: Contains notes and examples discussed during class sessions.
- **homework**: Contains Jupyter notebooks and scripts for homework assignments.

## Requirements

- Python 3.13 or higher
- Core dependencies:
  - ipywidgets >=8.1.5
  - matplotlib >=3.9.3
  - numpy >=2.1.3
  - scipy >=1.14.1
  - sympy >=1.13.3

## Development Environment Setup

To install dependencies and set up your environment:

```sh
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh
# or
brew install uv

# Install dependencies
uv add -r requirements.txt

# Create and activate a new virtual environment
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

Make sure you have Python 3.13 or higher installed on your system.

## Usage

### Running Python Scripts

To run the Python scripts in the `quiz-studying` directory, navigate to the appropriate folder and execute the script using Python:

```sh
cd Calculus/quiz-studying/4.3
uv run 4.3-Q1.py
