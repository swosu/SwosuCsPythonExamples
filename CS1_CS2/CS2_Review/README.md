# CS2 Movie Review — OMDb API Demo

This example shows how to call the OMDb API from Python using the `requests` library and the [OMDb API](https://www.omdbapi.com/).

Main file:

- `test_omdb.py`

It expects a valid OMDb API key stored in the file.

---

## 1. Prerequisites

- Windows 10 or later  
- Python 3 installed and available as `py` or `python`  
- (Optional) Git, if you want to clone/update the repo

---

## 2. Open the project folder

Open **Command Prompt** and run:

```bat
cd C:\Users\evertj\git\SwosuCsPythonExamples\CS1_CS2\CS2_Review
````

You can run `dir` here and you should see:

* `movie_venv` (virtual environment folder)
* `test_omdb.py`
* `README.md`

If `movie_venv` is missing, you’ll create it in the next step.

---

## 3. Create the virtual environment (first time only)

If the `movie_venv` folder does **not** exist, create it:

```bat
python -m venv movie_venv
```

> **Note:** This command is *quiet* when it succeeds.
> If there’s no error message and the `movie_venv` folder appears when you run `dir`, it worked.

If `movie_venv` already exists, you can skip this creation step.

---

## 4. Activate the virtual environment (every time you work)

### Command Prompt (cmd.exe)

From inside the project folder:

```bat
cd C:\Users\evertj\git\SwosuCsPythonExamples\CS1_CS2\CS2_Review
movie_venv\Scripts\activate.bat
```

If activation worked, your prompt will change to something like:

```text
(movie_venv) C:\Users\evertj\git\SwosuCsPythonExamples\CS1_CS2\CS2_Review>
```

That `(movie_venv)` at the front means **“you are inside the virtual environment now.”**

### PowerShell (optional)

If you are using PowerShell instead of Command Prompt:

```powershell
cd C:\Users\evertj\git\SwosuCsPythonExamples\CS1_CS2\CS2_Review
.\movie_venv\Scripts\Activate.ps1
```

> If PowerShell complains about scripts / execution policy, just use Command Prompt instead, or talk to your instructor.

### Deactivate when done

To leave the virtual environment:

```bat
deactivate
```

---

## 5. Install dependencies (first time in this venv)

With the virtual environment **activated** (`(movie_venv)` in the prompt):

```bat
pip install requests
```

If you ever need to update `pip` inside this environment, you can do:

```bat
python -m pip install --upgrade pip
```

---

## 6. Put your OMDb API key in the script

In `test_omdb.py`, near the top:

```python
API_KEY = "YOUR_OMDB_API_KEY_HERE"
```

Replace the string with your real OMDb API key, for example:

```python
API_KEY = "7ad6b576"
```

(Do **not** commit your real key to a public repo if this is going on GitHub for students.)

---

## 7. Run the script

Make sure the virtual environment is **activated**:

```text
(movie_venv) C:\Users\...
```

Then run:

```bat
python test_omdb.py
```

You should see something like:

```text
API_KEY repr: '7ad6b576'
{'Title': 'Inception', 'Year': '2010', 'Rated': 'PG-13', ... 'Response': 'True'}
```

If you see a big dictionary with info about *Inception*, everything is working.

---

## 8. Quick “Every Time” Checklist for Students

When you come back to this project on another day:

1. Open **Command Prompt**

2. Go to the folder:

   ```bat
   cd C:\Users\evertj\git\SwosuCsPythonExamples\CS1_CS2\CS2_Review
   ```

3. Activate the venv:

   ```bat
   movie_venv\Scripts\activate.bat
   ```

4. Run the script:

   ```bat
   python test_omdb.py
   ```

5. When finished, optionally:

   ```bat
   deactivate
   ```

---

## 9. Troubleshooting

* **`ModuleNotFoundError: No module named 'requests'`**

  * Make sure you see `(movie_venv)` in your prompt.
  * Then run:

    ```bat
    pip install requests
    ```

* **`python` or `py` not recognized**

  * Python might not be on your PATH.
  * Reinstall Python and check “Add Python to PATH” during setup, or ask for help.

* **Virtual environment creation seems to “do nothing”**

  * This is normal.
  * Run `dir` and look for the `movie_venv` folder.
  * If it exists and there was no error message, it worked.

