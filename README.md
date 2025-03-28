```markdown
# Flask Task Management API

Этот проект представляет собой простое API для управления задачами, созданное с использованием Flask. API позволяет добавлять, удалять и просматривать задачи, хранящиеся в локальной базе данных (списке).

## Функциональность

- **Получение списка задач**: Сортировка задач по дате `deadline` (по умолчанию в порядке возрастания).
- **Добавление новой задачи**: Создание новой задачи с проверкой корректности формата даты.
- **Удаление задачи**: Удаление задачи по её идентификатору (`id`).

## Установка и запуск

1. Убедитесь, что у вас установлен Python 3.7 или выше.
2. Установите зависимости:
   ```bash
   pip install flask
   ```
3. Запустите приложение:
   ```bash
   python app.py
   ```
4. Приложение будет доступно по адресу: `http://127.0.0.1:5000`.

## Эндпоинты

### 1. Получение списка задач

**GET** `/tasks`

Возвращает список всех задач, отсортированных по дате `deadline` в порядке возрастания.

**Пример ответа**:
```json
[
    {
        "1": {
            "title": "tit",
            "description": "disk",
            "deadline": "12-03-2025"
        }
    },
    {
        "3": {
            "title": "tit2",
            "description": "disk2",
            "deadline": "12-03-2023"
        }
    }
]
```

---

### 2. Добавление новой задачи

**POST** `/tasks`

Создаёт новую задачу. Принимает JSON с полями:
- `title` (строка) — название задачи.
- `description` (строка) — описание задачи.
- `deadline` (строка) — крайний срок задачи в формате `dd-mm-yyyy`.

**Пример запроса**:
```json
{
    "title": "New Task",
    "description": "Description of the task",
    "deadline": "25-03-2025"
}
```

**Пример ответа**:
```json
{
    "4": {
        "title": "New Task",
        "description": "Description of the task",
        "deadline": "25-03-2025"
    }
}
```

Если формат даты некорректен, возвращается сообщение об ошибке:
```text
Ошибка ввода формата даты
```

---

### 3. Удаление задачи

**DELETE** `/tasks/<int:id>`

Удаляет задачу по её идентификатору (`id`).

**Пример запроса**:
```bash
DELETE /tasks/2
```

**Пример ответа**:
```text
Задача удалена
```

Если задача с указанным `id` не найдена:
```text
Задача не найдена
```

---

## Примечания

- Локальная база данных (`DB`) представляет собой список словарей, где каждая задача хранится в формате:
  ```python
  {
      id: {
          "title": "str",
          "description": "str",
          "deadline": "dd-mm-yyyy"
      }
  }
  ```
- Для продакшена рекомендуется использовать полноценную базу данных, например, PostgreSQL, и ORM, такую как SQLAlchemy.
- В текущей реализации отсутствует возможность редактирования задач и проверки на пересечения по времени.

## Лицензия

Этот проект предоставляется "как есть" и может быть использован для образовательных целей.
```
