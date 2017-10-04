#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

# В проекте используется версия Django, установленная в Virtualenv.

# Добавьте нужные вам пути поиска.
# Если вы получаете ошибку 500 Internal Server Error,
# скорее всего проблема именно в путях поиска.

# Пункт 3 - пути для стилей, так же на сервере и локально отличаются
# это серверные настройки
# sys.path.insert(0, '/home/hosting_asteroid888/projects/stories/app')
# sys.path.insert(0, '/home/hosting_asteroid888/projects/stories')


# это локальные настройки
sys.path.insert(0, '/home/asteroid/projects/all/projects/stories/app')
sys.path.insert(0, '/home/asteroid/projects/all/projects/stories')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

# ------ Ниже этой линии изменения скорее всего не нужны --------

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
