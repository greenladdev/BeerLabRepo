# Beer Fault Finder

A Python + Flask web application with a beer-inspired interface that helps users explore **50 common beer off-flavors**.

## Features

- List page with the top 50 off-flavors
- Flashcards quiz with 50 cards and 3 choices per card
- Detail page for each flavor with:
  - Flavor description
  - Beer styles where it appears most often
  - Practical brewer avoidance guidance

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.main
```

Open: `http://127.0.0.1:5000`
