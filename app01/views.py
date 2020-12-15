from django.shortcuts import render
from django.http import HttpResponse
from web_models import models
from django.http import HttpResponseRedirect


# Create your views here.

def redIndex(request):
    return HttpResponseRedirect("/index-0-0.html")


def index(request, *args, **kwargs):
    for k, v in kwargs.items():
        kwargs[k] = int(v)
    position_list = models.position.objects.all()
    gender_list = models.gender.objects.all()
    #  进行全选判断
    if kwargs.get("position_id") == 0 and kwargs.get("gender_id") != 0:
        result = models.hero.objects.filter(
            hero_gender_id=kwargs.get("gender_id"),
        )
    elif kwargs.get("gender_id") == 0 and kwargs.get("position_id") != 0:
        result = models.hero.objects.filter(
            hero_position_id=kwargs.get("position_id"),
        ).select_related("hero_position")
    elif kwargs.get("gender_id") == 0 and kwargs.get("position_id") == 0:
        result = models.hero.objects.all()
    else:
        result = models.hero.objects.filter(
            hero_position_id=kwargs.get("position_id"),
            hero_gender_id=kwargs.get("gender_id"),
        )
    print(locals())
    return render(request, "index.html", locals())
