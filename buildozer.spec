[app]
title = Шифратор
package.name = cryptoapp
package.domain = org.user
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, kivy==2.2.1, deep-translator==1.11.4, cython==0.29.36
android.permissions = INTERNET
orientation = portrait
android.minapi = 21
android.ndk = 23b
source.include_main = True
source.main = shift_2.py  # Укажите ваше имя файла
