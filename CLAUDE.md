# Kodiq Monorepo

> Оркестратор для всех проектов Kodiq. Каждый подпроект — git submodule.

## Структура

```
kodiq/
├── academy/    — Образовательная платформа, курсы
├── ide/        — AI Desktop IDE (Tauri + React) → ide/CLAUDE.md
├── mobile/     — React Native мобильное приложение
├── web/        — Лендинг kodiq.ai (Next.js) → web/CLAUDE.md
├── shared/     — Общие пакеты: auth, UI, types (@kodiq/shared)
└── scripts/    — Скрипты для работы с monorepo
```

## Правила

- **Язык общения**: русский. Код и термины — английский.
- **Submodules**: каждый подпроект — отдельный репозиторий. Не делай коммиты внутри submodule из корневого репо.
- **Обновление submodules**: `git submodule update --remote <name>` для обновления до последнего коммита.
- **CLAUDE.md подпроектов**: при работе внутри подпроекта следуй его CLAUDE.md (если есть).
- **Shared пакет**: `@kodiq/shared` — общие типы, утилиты, Supabase клиент. Изменения здесь влияют на все проекты.

## Быстрый старт

```bash
git clone --recursive https://github.com/kodiq-ai/kodiq.git
cd kodiq
./scripts/setup.sh
```

## Git

- Коммиты в корневом репо: обновление submodule refs, скрипты, документация.
- Коммиты в подпроектах: делаются внутри соответствующего подпроекта.
- Формат: `feat:`, `fix:`, `refactor:`, `docs:`, `chore:`, `test:`
