import os
import configparser
from pathlib import Path

if os.name == "nt":
    CONFIG_PATH = Path(os.getenv("APPDATA")) / "MMFApplications"
else:
    home = Path(os.getenv("HOME"))
    username = os.getenv("USER") or os.getenv("USERNAME") or "Default"
    CONFIG_PATH = home / ".wine" / "drive_c" / "users" / username / "AppData" / "Roaming" / "MMFApplications"

CONFIG_PATH.mkdir(parents=True, exist_ok=True)

def write_at_config(group: str, key: str, value: str):
    config = configparser.ConfigParser()
    config_file = CONFIG_PATH / "fnag1"
    if config_file.exists():
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config.read_file(f)
        except Exception:
            pass

    if not config.has_section(group):
        config.add_section(group)

    config.set(group, key, str(value))

    temp_file = config_file.with_suffix('.tmp')
    with open(temp_file, 'w', encoding='utf-8') as f:
        config.write(f)
    os.replace(temp_file, config_file)

    print(f"Config saved at: {config_file}")

def read_at_config(group: str, key: str):
    config = configparser.ConfigParser()
    config_file = CONFIG_PATH / "fnag1"

    if not config_file.exists():
        return None

    config.read(config_file)

    try:
        return config[group][key]
    except KeyError:
        return None