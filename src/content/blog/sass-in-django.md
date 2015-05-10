title: Использваоние sass в Django проектах.
date: 2012-10-24
type: blog
tags: [Django, css]

Как-то все туго да сложно у меня было с этим вопросм. Сам по себе sass достаточно удобен, и на сегодня, мне кажется, лучший css процессор. 

Но все равно в каждом проекте под Django я использовал чистый css. Так как подулючить sass было реально проблематично.  Были поделки что бы командой `./manage.py ..` компилировать. Жутко неудобно! 

Но в рабочем процессе столкнулся с надобностью, не отвертеться. И оказалось все очень просто! Есть замечательная вещь [django_compressor](http://django_compressor.readthedocs.org/en/latest/)  элементарно [подключается](http://django_compressor.readthedocs.org/en/latest/quickstart/#installation) и работает на ура!

Удобный sass в Django проектах. Мало того, сжимает, если нужно, css. Работает с [CoffeeScript](http://coffeescript.org/). В общем шикарная вещь.