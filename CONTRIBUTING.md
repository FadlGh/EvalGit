# Contributing to EvalGit

EvalGit is open source and community-friendly. Whether you're fixing a bug, adding a feature, improving documentation, or suggesting ideas — you're welcome here.

---

## 🚧 Local Setup

1. Clone the repo and install in editable mode:

    ```bash
    git clone https://github.com/FadlGh/EvalGit.git
    cd EvalGit
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -e .
    ```

2. Install dev dependencies (if any):

    ```bash
    pip install -r requirements.txt
    ```

---

## 🧪 Testing

For now, testing is CLI-based. Run:

```bash
evalgit log --model testmodel --gt test_gt.json --pred test_pred.json --dataset dummy --notes "test run" --report
evalgit show
evalgit delete --key model_name --value testmodel
```

Add formal test cases under `tests/` (use `pytest` or `unittest`).

---

## 🗂 Project Structure

```
evalgit/
├── core/               # Main logic (log, db, report handlers)
test_data/
```

---

## ✅ Pull Request Guidelines

- One feature or fix per PR
- Descriptive commit messages:
  - Use prefixes to describe commits: fix, refactor, feat, etc.
  - e.g. `fix: handle empty DB case`
- Link issues in your PR description
- Add docstrings for public functions/classes
- Avoid large unrelated refactors

---

## 💡 Tips

- Use `platformdirs` for any file paths — never hardcode.
- All data (DB, reports) lives in the user data directory.
- Handle missing files or bad inputs gracefully in CLI.
- Keep CLI subcommands discoverable and consistent.

---

## 🗨️ Questions or Suggestions?

- Open an [Issue](https://github.com/FadlGh/EvalGit/issues)
- Or email: [fadl2009gh@gmail.com](mailto:fadl2009gh@gmail.com)

Thanks for contributing!
