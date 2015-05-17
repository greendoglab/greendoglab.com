title: Favicon в Django.
date: 2012-09-16
type: blog
tags: [Django, Снипеты]

Если честно я как-то не думал что такая простая мелочь как favicon.ico может решаться множеством способов.. Но как-то столкнулся с тем, что нужно, и не работал мой любимый стандартный способ. 

А по итогу оказалось все очень даже просто.. Существует несколько способов добавить в Django проект favicon.ico и самый простой это `html`

    <link rel="shortcut icon" href="/path/to//favicon.ico" />

Второй и третий способы в Django.

    urlpatterns = patterns('',
        (r'^favicon.ico$', 'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT, 'path': "favicon.ico"}),
    )

    from django.views.generic.base import TemplateView, RedirectView

        urlpatterns = patterns('',
        url(r'^favicon\.ico$', RedirectView.as_view(url='/path/to/favicon.ico')),
    )

Третий nginx

    location = /favicon.ico {
        rewrite (.*) /path/to/favicon.ico
    }

Лично я использую 1-й Django способ, на скромно посещаемых проектах, и nginx на крупно посещаемых.