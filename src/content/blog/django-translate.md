title: Перевод Django в OSX.
date: 2012-10-10
type: blog
tags: [Django, Mac, Ubuntu, ОС]

Столкнулся с небольшой проблемкой перевода сайта на Django. При замечательной команде `./manage.py makemessages` система давала ошибку:

    Importing Django settings module settings
    processing language nl
    Error: errors happened while running xgettext on __init__.py
    /bin/sh: xgettext: command not found

В Ububntu все просто, блин взял да и потсавил xgettext и проблема решена. Но на маке не так все просто, сам gettext  стаивтья из любого менеджера пакетов, но это не помогает. Я начала гуглить и нашел кучу советов, поставить [PoEdit](http://www.poedit.net/download.php), наделать кучу симлинков, доавбить переменную в `$PATH`.. а по итогу решается все проще некуда. 

brew install.

    brew install gettext
    brew link gettext

И вообщем-то все. Дальше все работает довольно прекрасно.