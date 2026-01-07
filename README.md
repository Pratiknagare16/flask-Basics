# 🚀 Study Flask - Your First Web Server

A progressive learning repository for students to master Flask basics step-by-step.

---

## 📖 What is Flask?

Flask is a **micro-framework** for Python. Think of it as a toolbox that provides just the essentials to build a website. Unlike static HTML, Flask allows you to:
- Create dynamic web pages
- Use Python logic in your HTML (via Jinja2 templates)
- Handle user requests and send responses

---

## 🎯 Learning Objectives

By completing all parts, you will understand:

- ✅ Virtual Environments (`venv`) - Creating isolated project environments
- ✅ App Routing - Using `@app.route()` to map URLs to functions
- ✅ Jinja2 Templates - Passing Python variables to HTML
- ✅ The Request-Response Cycle - How browsers and servers communicate
- ✅ Dynamic Routing - Creating flexible URL patterns

---

## 🛠️ Initial Setup (Do This First!)

### Step 1: Open Terminal in VS Code
Navigate to this project folder.

### Step 2: Create Virtual Environment
```bash
python -m venv venv
```

### Step 3: Activate Virtual Environment

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal line.

### Step 4: Install Flask
```bash
pip install flask
```

### Step 5: Create .gitignore File
Create a `.gitignore` file in the root folder with the following content:
```
venv/
__pycache__/
*.pyc
.env
```

---

## 📂 Repository Structure

```
study-flask/
├── README.md           # You are here!
├── part-1/             # Hello Flask - The Basics
├── part-2/             # Templates - Rendering HTML
├── part-3/             # Jinja2 - Passing Variables
├── part-4/             # Dynamic Routes - Multiple Pages
└── part-5/             # Mini Project - Personal Website
```

---

## 📚 Parts Overview

| Part | Topic | What You'll Learn |
|------|-------|-------------------|
| **Part 1** | Hello Flask | Minimal Flask app, `@app.route`, running the server |
| **Part 2** | Templates | `templates/` folder, `render_template()` function |
| **Part 3** | Jinja2 Variables | Passing data from Python to HTML with `{{ }}` |
| **Part 4** | Dynamic Routes | Multiple routes, URL parameters with `<variable>` |
| **Part 5** | Mini Project | Build a complete personal website with Flask |

---

## 🚀 How to Run Each Part

1. Make sure your virtual environment is activated (you see `(venv)`)
2. Navigate to the part folder:
   ```bash
   cd part-1
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your browser and go to: `http://localhost:5000`
5. Press `Ctrl+C` in terminal to stop the server

---

## 📤 Submission Checklist

After completing all parts, submit:

1. **Screenshot 1:** Terminal showing `(venv)` activated and Flask server running
2. **Screenshot 2:** Browser at `localhost:5000` showing your website
3. **Screenshot 3:** Your `app.py` code highlighting the `@app.route`

**Caption:** "Successfully launched my first Python server! My personal website is now being served by Flask."

---

## 💡 Tips for Success

- Always activate `venv` before running any Flask app
- If you see an error, read it carefully - Python errors are helpful!
- Use `debug=True` during development to see live changes
- Press `Ctrl+C` to stop the server before running a different part

---

## 🔗 Quick Reference

```python
# Minimal Flask App Structure
from flask import Flask          # Import Flask
app = Flask(__name__)            # Create app instance

@app.route('/')                  # Define route (URL path)
def home():                      # Function that handles the route
    return "Hello Flask!"        # Response sent to browser

if __name__ == '__main__':
    app.run(debug=True)          # Start the server
```

---

Happy Learning! 🎉
