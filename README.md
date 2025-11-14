# AI_Agent

A Python-based AI agent framework that allows you to build, configure and run autonomous tasks via large language models (LLMs).  
This project provides core functionality for prompt handling, function/tool integration, modular components, and a simple test harness.


## Features

- Modular configuration file (`config.py`) for easy customization of system prompts, tools and agent behaviour.  
- A central entry point (`main.py`) which orchestrates the agent’s loop of thinking, calling functions/tools and returning responses.  
- Support for external prompts (`prompts.py`) so you can maintain and tailor system/user prompts easily.  
- Simple test harness (`tests.py`) to validate behaviour and ensure components work as expected.  
- Pre-defined tool modules or example functions (in the `functions` folder) to demonstrate how the agent can interact with external logic.  
- Lightweight dependencies and a `pyproject.toml` to manage the Python environment & packaging.

## Getting Started

### Prerequisites  
- Python 3.8+  
- (Optional) Virtual environment (venv or conda)  
- Required packages installed (see `pyproject.toml` for details)  

### Installation  
```bash
git clone https://github.com/Noaht8/AI_Agent.git
cd AI_Agent
python3 -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
pip install --upgrade pip
pip install .
```

## Project Structure
.
├── README.md
├── __pycache__
│   ├── call_function.cpython-312.pyc
│   ├── config.cpython-312.pyc
│   └── prompts.cpython-312.pyc
├── calculator
│   ├── README.md
│   ├── calculator.py
│   ├── lorem.txt
│   ├── main.py
│   ├── pkg
│   │   ├── __pycache__
│   │   │   ├── calculator.cpython-312.pyc
│   │   │   └── render.cpython-312.pyc
│   │   ├── calculator.py
│   │   ├── morelorem.txt
│   │   └── render.py
│   └── tests.py
├── call_function.py
├── config.py
├── functions
│   ├── __pycache__
│   │   ├── get_file_content.cpython-312.pyc
│   │   ├── get_files_info.cpython-312.pyc
│   │   ├── run_python_file.cpython-312.pyc
│   │   └── write_file.cpython-312.pyc
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── main.py
├── pkg
├── prompts.py
├── pyproject.toml
├── tests.py
└── uv.lock
