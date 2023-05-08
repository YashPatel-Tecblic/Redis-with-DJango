from django.shortcuts import render,HttpResponse
from .models import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from django.core.cache import cache


CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

def RecepiApi(request):
    if 'recipe' in cache:
        products = cache.get('recipe')
        return HttpResponse(products)
    else:
        results = list(Recipe.objects.all().values())
        cache.set("recipe", results, timeout=CACHE_TTL)
        return HttpResponse(results)


# def recepiApi(request):
#     if 'recipe' in cache:
#         result = cache.get('recipe')
#         content ={
#             'result':'From cache'
#         }
#         return JsonResponse(result,content)
#     else:
#         results = list(Recipe.objects.all()) 
#         cache.set("recipe",results,timeout=CACHE_TTL)
#         content = {
#             'result': 'From Database'
#         }
#         return JsonResponse(results,content)