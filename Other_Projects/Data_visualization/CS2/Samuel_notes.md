# Git Workflow Cheat Sheet (Samuel Dudgeon)

## What You Did (Summary)
You:
1. Verified Git was installed.
2. Navigated to your Git project directory (`SwosuCsPythonExamples`).
3. Pulled the latest changes from the `main` branch.
4. Switched to the `dev` branch.
5. Merged `main` into `dev`.
6. Pushed changes to the remote `dev` branch.
7. Fetched and checked out a new branch called `data_viz_9`.
8. Created and committed a new Python file: `CS2_9_Samuel.py`.
9. Set up your Git username and email.
10. Pushed the commit to the `data_viz_9` branch on GitHub.
11. Merged `data_viz_9` into `dev` and pushed the update.

---

## Git Commands Cheat Sheet

### 📁 Navigate to Git Repo
```bash
cd git
cd SwosuCsPythonExamples
```

### 🔄 Pull Latest Changes
```bash
git pull
```

### 🔀 Switch Branches
```bash
git checkout dev
```

### 🔁 Merge Branches
```bash
git merge --no-ff main
```

### ⬆️ Push Changes to Remote
```bash
git push
```

### 🌿 List All Branches
```bash
git branch -a
```

### ⬇️ Fetch New Branches From Remote
```bash
git fetch
```

### 💡 Checkout New Branch Locally
```bash
git checkout data_viz_9
```

### 📝 Create/Edit a File (e.g., Hello World)
```bash
notepad CS2_9_Samuel.py
```

### ➕ Stage Changes
```bash
git add .
```

### 🧾 Commit Changes
```bash
git commit -m "add in hello world test."
```

### 👤 Set Git Username and Email
```bash
git config --global user.name "Samuel Dudgeon"
git config --global user.email "samuelld1050@gmail.com"
```

### ⬆️ Push New Branch
```bash
git push
```

### 🔁 Merge Feature Branch Into Dev
```bash
git checkout dev
git merge --no-ff data_viz_9
```

### ✅ Final Push to Dev
```bash
git push
```

---

## Notes
- `'code' is not recognized` means VS Code's command line is not set up in PATH. Use Notepad or set up VS Code CLI later.
- Always `git pull` before starting new work to ensure you're working with the latest changes.
- Feature branches (like `data_viz_9`) help isolate work.
- Merging with `--no-ff` preserves branch history.

Let me know if you'd like this cheat sheet as a downloadable file.

