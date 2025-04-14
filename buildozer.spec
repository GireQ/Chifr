[app]
# Название приложения
title = Шифратор

# Идентификаторы пакета
package.name = cryptoapp
package.domain = org.user

# Пути к исходникам
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.main = shift_2.py

# Зависимости
requirements = 
    python3,
    kivy==2.2.1,
    deep-translator==1.11.4,
    cython==0.29.36

# Разрешения Android
android.permissions = INTERNET

# Ориентация экрана
orientation = portrait

# Версии Android SDK
android.api = 34
android.minapi = 21
android.maxapi = 34

# Версии инструментов
android.ndk = 25.2.9519653
android.build_tools = 34.0.0



# Дополнительные настройки
log_level = 2
android.arch = arm64-v8a
android.mode = debug
