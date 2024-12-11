# Реферальная система, вход по номеру через смс[В разработке/набросок]

## Описание

Просто вход по номеру через интерфейс/API + присвоение к номеру реферальной ссылки. МБ когда-нибудь доделаю

### Как запустить проект
Устанавливаем виртуальное окружение:

```bash
python -m venv venv
```

Активируем виртуальное окружение:

```bash
. venv/Scripts/activate
```

> Для деактивации виртуального окружения выполним (после работы):
> ```bash
> deactivate
> ```

Устанавливаем зависимости:

```bash
python -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

Применяем миграции:

```bash
python manage.py makemigrations
python manage.py migrate
```
