# Simple Flask website

## Getting started

1. From the Flask Website folder, set up a Python virtual environment:

  ```bash
  python3 -m venv .venv
  ```

2. Activate virtual environment:

  Note that you'll need to do this every time you open a new terminal.

  ```bash
  source .venv/bin/activate
  ```

  Note: If you need to deactivate the virtual environment in the current terminal, you can run `deactivate`

3. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

4. Run app:

  ```bash
  ./website.py
  # Or, to run with flask and/or specify a port:
  flask --app=website run --host=0.0.0.0 --port=80
  ```

5. Browse to http://localhost:5000
