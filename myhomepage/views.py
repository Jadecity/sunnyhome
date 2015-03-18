from django.shortcuts import render, HttpResponse
from django.template import Context, loader
from myhomepage.models import Me

# Create your views here.
def homepage(request, name):
    person = Me.objects.get(name = name)
    context = Context({
        "name":person.name,
        "avatar_path":person.photo,
        "motto": "life is a leaf in permanent space.",
        "title": "My Homepage",
        "items": [1,2,3,4],
        "desc": person.intro
    })
    template = loader.get_template("homepage.html")
    return HttpResponse( template.render( context ) )

def page404(request):
    return HttpsResponse("sorry....")
