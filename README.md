# Five Nights at Glackus`s Education Edition API

## Описание

Этот проект предоставляет API для управления игровыми механиками Five Nights at Glackus`s Education Edition. API реализует управление энергией, музыкальной шкатулкой, камерами, фонариком, сущностями, временем и игровой сессией.

## Структура проекта

- [`fnagapi.py`](fnagapi.py) — Основная реализация API, классы для управления игровыми системами.
- [`config.py`](config.py) — Работа с конфигурационным файлом игры (чтение/запись параметров).
- [`constants.py`](constants.py) — Константы для идентификаторов сущностей, камер и времени.
- [`test_program.py`](test_program.py) — Пример использования API, тестовая программа.
- [`README.md`](README.md) — Описание проекта.
- [`.gitignore`](.gitignore) — Исключение служебных файлов из репозитория.

## Быстрый старт

1. Установите зависимости (если требуются).
2. Запустите [`test_program.py`](test_program.py) для проверки работы API:

```sh
python test_program.py
```

## Пример использования

```py
from fnagapi import entity, session
from constants import ENTITY_WANDARMO

session.set_level(6)
entity.ai_ignore(ENTITY_WANDARMO)
print(entity.get_ai_ignored_list())
```

## Документация

- Основные классы и методы описаны в [`fnagapi.py`](fnagapi.py).
- Константы для работы с сущностями и камерами — в [`constants.py`](constants.py).
- Пример конфигурирования — в [`config.py`](config.py).

## Автор

Gleb Ustimenko for LighSync Games

## Лицензия

API распространяется по лицензии MIT
(C) LighSync Games. 2023-2025
