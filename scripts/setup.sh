#!/bin/bash
set -euo pipefail

echo "🔧 Kodiq Setup"
echo "==============="

# Инициализация и обновление submodules
echo ""
echo "📦 Initializing submodules..."
git submodule update --init --recursive

# Установка зависимостей для каждого подпроекта
for dir in ide mobile web shared; do
  if [ -f "$dir/package.json" ]; then
    echo ""
    echo "📦 Installing dependencies for $dir..."
    cd "$dir"
    if [ -f "bun.lock" ] || [ -f "bun.lockb" ]; then
      bun install
    elif [ -f "yarn.lock" ]; then
      yarn install
    elif [ -f "pnpm-lock.yaml" ]; then
      pnpm install
    else
      npm install
    fi
    cd ..
  fi
done

echo ""
echo "✅ Setup complete!"
