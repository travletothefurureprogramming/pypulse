# PyPulse

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
