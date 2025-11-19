# CS2 Movie Review – OMDb API Demo

This example shows how to call the OMDb API from Python using the `requests` library.

The main file is:

- `test_omdb.py`

It expects a valid OMDb API key stored in the file.

---

## 1. Prerequisites

- Windows 10 or later  
- Python 3 installed and available as `py` or `python`
- Git (optional, but helpful)

---

## 2. Create (or reuse) the virtual environment

From a **Command Prompt** in this folder:

```bat
cd C:\Users\evertj\git\SwosuCsPythonExamples\CS1_CS2\CS2_Review
````

If the `movie_venv` folder does **not** exist yet, create it:

```bat
py -3 -m venv movie_venv
```

If `movie_venv` already exists (you can see it when you run `dir`), you can skip the creation step and just activate it.

---

## 3. Activate the virtual environment (Windows)

### Command Prompt (cmd.exe)

```bat
cd C:\Users\evertj\git\SwosuCsPythonExamples\CS1_CS2\CS2_Review
movie_venv\Scripts\activate
```

You should see something like this at the beginning of your prompt:

```text
(movie_venv) C:\Users\...
```

### PowerShell

```powershell
cd C:\Users\evertj\git\SwosuCsPythonExamples\CS1_CS2\CS2_Review
.\movie_venv\Scripts\Activate.ps1
```

> If PowerShell complains about execution policy, you can run it in Command Prompt instead, or ask your instructor how to temporarily relax the policy.

To **deactivate** the environment (both cmd and PowerShell):

```bat
deactivate
```

---

## 4. Install dependencies

With the virtual environment **activated**:

```bat
pip install requests
```

(If you later add a `requirements.txt` file, you can instead do `pip install -r requirements.txt`.)

---

## 5. Put your OMDb API key in the script

In `test_omdb.py`:

```python
API_KEY = "YOUR_OMDB_API_KEY_HERE"
```

Replace the string with your real key.

---

## 6. Run the script

With the virtual environment still **activated**:

```bat
python test_omdb.py
```

You should see:

* The API key printed with `repr`
* A JSON dictionary of movie information for “Inception”

---

## 7. Troubleshooting

* If you get `ModuleNotFoundError: No module named 'requests'`, make sure:

  * The virtual environment is activated (you see `(movie_venv)` in your prompt)
  * You ran `pip install requests` while the environment was active
* If `py` doesn’t work, try:

  ```bat
  python -m venv movie_venv
  ```

  instead of `py -3 -m venv movie_venv`.

