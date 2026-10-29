import configparser
from pathlib import Path

CONFIG_FILE = Path(__file__).resolve().parent.parent / "config.ini"

parser = configparser.ConfigParser()

loaded_files = parser.read(CONFIG_FILE, encoding="utf-8")

if not loaded_files:
    raise FileNotFoundError(
        f"Configuration file not found: {CONFIG_FILE}"
    )

HOST = parser.get("server", "host")
PORT = parser.getint("server", "port")

DEBUG = parser.getboolean("application", "debug")

LOG_LEVEL = parser.get("logging", "level").upper()
LOG_FILE = parser.get("logging", "file")

