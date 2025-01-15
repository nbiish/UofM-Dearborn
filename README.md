# UofM-Dearborn Course Notes

Welcome to my UofM-Dearborn coursework repository. This repository contains course materials, lecture notes, and study materials organized by semester and subject.

## Repository Structure

The repository is organized by semester and course:

- **2024 Fall**
  - **Calculus**
    - `in-class/`: Detailed lecture notes and examples
    - `uv.lock`: Dependency lock file
  
- **2025 Winter**
  - **Historical Geology**
    - `lecture/`: Weekly lecture notes and materials

## Requirements

### Calculus Course

Core Python dependencies:
- matplotlib >=3.9.3
- numpy >=2.1.3
- scipy >=1.14.1
- sympy >=1.13.3
- ipywidgets >=8.1.5
- ipykernel (dev dependency)

### Development Setup

The project uses `uv` for Python dependency management with dependencies specified in `uv.lock`:

```sh
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh
# or
brew install uv

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows

# Install dependencies from uv.lock
uv pip sync
```

## Course Materials

### Calculus

The Calculus materials include detailed examples and explanations for topics like:
- Antiderivatives and integration
- Power rule applications
- Exponential and trigonometric functions
- Initial value problems

### Historical Geology

Weekly lecture notes covering:
- Earth's geological history
- Plate tectonics
- Formation of the universe
- Geological principles and theories
