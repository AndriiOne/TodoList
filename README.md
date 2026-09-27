# Todo List

### Home page
<img width="1124" height="581" alt="Home" src="https://github.com/user-attachments/assets/152c249e-f842-401c-a9f8-e5fc3c59b74a" />

A simple Django app for managing tasks with tags.

## Features
- Create, update and delete tasks and tags
- Mark tasks as done / undo
- Tasks sorted: not done first, newest first

## How to run
```bash
git clone https://github.com/AndriiOne/TodoList.git
cd TodoList
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.sample .env
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/