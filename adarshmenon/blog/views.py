from django.shortcuts import render


def index(request):
    # https://www.imzjy.com/blog/2018-05-20-render-the-markdown-in-django
    # usage in template
    # {{ content | markdown | safe }}
    return render(
        request,
        "blog/base.html",
        {
            "content": "# this is test title\n"
            + "- list 1\n"
            + "- list 2\n <h2>hi test</h2>"
        },
    )
