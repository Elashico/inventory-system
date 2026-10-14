# Full-Stack Application a simple inventory system

A full-stack application featuring a **FastAPI** backend and a **Frontend** interface.

Inspired by and built in reference to tutorials by [Telusko](https://www.youtube.com/@Telusko).

---

## Prerequisites
Make sure you have the following installed on your system:
* [Python](https://www.python.org/) (v3.8 or higher)
* [Node.js & npm](https://nodejs.org/)

---

## Getting Started

### 1. Backend Setup (FastAPI)

Open your terminal, navigate to your backend directory, and set up your Python environment:

```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment (named 'myenv')
python -m venv myenv

# Activate the virtual environment
# For Windows (Command Prompt):
myenv\Scripts\activate.bat

# For Windows (PowerShell):
myenv\Scripts\Activate.ps1

# For macOS / Linux:
source myenv/bin/activate

# Install required dependencies
pip install fastapi uvicorn

# Start the FastAPI backend server
uvicorn main:app --reload
```

### 2. Frontend Setup

Open a new terminal window, navigate to your frontend directory, install dependencies, and run the development server:

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the frontend development server
npm run dev

```

