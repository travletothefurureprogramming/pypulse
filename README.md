# PyPulse

<img width="553" height="178" alt="Screenshot 2026-11-01 150729" src="https://github.com/user-attachments/assets/76ccbe9c-69da-49b8-998f-14901a0fdfb8" />
<img width="323" height="226" alt="Screenshot 2026-11-01 150700" src="https://github.com/user-attachments/assets/4bd48f41-3fa8-4552-9413-69a26ae3786c" />
<img width="375" height="211" alt="Screenshot 2026-11-01 150748" src="https://github.com/user-attachments/assets/c2d9c239-6a5d-444b-9e11-02ca5cdad2a0" />


A small system monitoring API built with Python and Flask.

I started PyPulse as a project to learn more about building REST APIs, working with system information and writing cleaner Python applications.

## What it does

* Shows basic system information.
* Monitors CPU, RAM and disk usage.
* Reports system uptime.

## Getting Started

Clone the repository

```
git clone https://github.com/travletothefurureprogramming/pypulse.git
```

Go to folder

```
cd pypulse
```


Create and activate virtual enviroment:

```
python -m venv .venv
```

or 

```
python3 -m venv .venv
```

Windows:

```
.venv/Scripts/activate
```

Linux:

```
source .venv/bin/activate
```

Install the dependencies:

```
pip install -r requirements.txt
```

Start the API:

```
python run.py
```

## Endpoints

| Endpoint    | Description               |
| ----------- | ------------------------- |
| /           | API overview              |
| /api/health | Health status             |
| /api/system | System Information        |
| /api/metrics| CPU, RAM, disk and uptime |

## Development

Run tests:

```
python -m pytest -v
```

Check code with Ruff:

```
ruff check .
ruff format --check .
```

GitHub Actions runs these checks automatically on every push and pull request.

Still a work in progress. More improvements coming soon.
