# Kodiq

Monorepo-оркестратор для проектов [Kodiq AI](https://github.com/kodiq-ai).

## Проекты

| Проект | Описание | Стек |
|--------|----------|------|
| [`academy`](https://github.com/kodiq-ai/academy) | Образовательная платформа, курсы | — |
| [`ide`](https://github.com/kodiq-ai/ide) | AI Desktop IDE | Tauri 2, React 19, TypeScript |
| [`mobile`](https://github.com/kodiq-ai/mobile) | Мобильное приложение | React Native |
| [`web`](https://github.com/kodiq-ai/web) | Лендинг kodiq.ai | Next.js |
| [`shared`](https://github.com/kodiq-ai/shared) | Общие пакеты (auth, UI, types) | TypeScript |

## Быстрый старт

```bash
# Клонирование с submodules
git clone --recursive https://github.com/kodiq-ai/kodiq.git
cd kodiq

# Установка зависимостей
./scripts/setup.sh
```

Если уже склонировали без `--recursive`:

```bash
git submodule update --init --recursive
```

## Обновление submodules

```bash
# Обновить все до последних коммитов
git submodule update --remote

# Обновить конкретный
git submodule update --remote ide
```

## Лицензия

Каждый подпроект имеет собственную лицензию. См. LICENSE в каждом репозитории.
