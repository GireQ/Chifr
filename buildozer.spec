[app]
title = Шифратор
package.name = cryptoapp
package.domain = org.user
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, kivy, deep-translator
android.permissions = INTERNET
orientation = portrait
android.sdk = 24
android.minapi = 21
android.ndk = 23b
source.include_main = True
source.main = shift_2.py  # Укажите ваше имя файла
