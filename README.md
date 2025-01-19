# schwab-trader

1. Make sure `python3`, `pip3`, and `git` are installed on your machine
2. Clone this repo
3. In the project folder `schwab-trader`, create a venv with `python3 -m venv .venv`
4. If you are using Visual Studio Code and have the Python extension installed, you can open a terminal and the venv should be activated (you will see `.venv` before your name in the terminal); if it's not activated, or if you're in an external terminal, run `source .venv/bin/activate` to activate it
5. Install relevant packages with `pip3 install -r requirements.txt`
6. Create `.env` file and fill in the values for keys `APP_KEY`, `APP_SECRET`, and `TOKEN_PATH`
7. Change the `webdriver` in `main.py` to use the browser you want (default is Firefox)
8. Run the app with `python3 main.py`
