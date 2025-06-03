# EvalGit

EvalGit is a CLI tool to track, version, and report machine learning evaluation metrics locally. It helps you organize evaluation results per model version in a reproducible, Markdown-friendly format.

## 🚀 Features

- Log evaluation metrics via CLI

- Store results locally in SQLite (~/.evalgit)

- Export reports in Markdown

- Query and delete specific logs easily
  

## 📦 Installation

```
pip install evalgit
```

Or install directly from source (development mode):

```
git clone https://github.com/FadlGh/EvalGit.git

cd EvalGit

pip install -e .
```

## 🛠️ Usage

### Log a new evaluation

`evalgit log --model mymodel --gt path/to/groundtruth.json --pred path/to/predictions.json --dataset mydataset --notes "first run" --report`

### Show all evaluations

`evalgit show`

### Show specific evaluation

`evalgit show --key model_name --value mymodel`

### Delete a specific evaluation

`evalgit delete --key model_name --value mymodel`

### Delete all evaluations

`evalgit delete`

## 📁 Data Location

All logs and reports are stored in an OS-specific user data directory managed by `platformdirs`.

Example paths:
- Linux: ~/.local/share/EvalGit/
- macOS: ~/Library/Application Support/EvalGit/
- Windows: C:\Users\<You>\AppData\Local\EvalGit\


## 🤝 Contributing

See CONTRIBUTING.md for full guidelines.

```
git clone https://github.com/FadlGh/EvalGit.git

cd EvalGit

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

pip install -e .
```

## 🌐 Author

LinkedIn: [Fadl Ghaddar](https://www.linkedin.com/in/fadl-ghaddar)  

Email: [fadl2009gh@gmail.com](mailto:fadl2009gh@gmail.com)

## License

[Apache 2.0](LICENSE)
