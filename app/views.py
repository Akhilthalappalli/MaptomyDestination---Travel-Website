from django.shortcuts import render, redirect
from.import models
from app.forms import PlaceForm,ToplistForm
from app.models import Place,Top_list
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage

from app.filters import PlaceFilter


# Create your views here.
def home(request):

    t_list = Top_list.objects.all()
    return render(request,'index.html',{"list" : t_list})


def search(request):
    query=request.POST.get("q" or None)
    collect = Place.objects.all()

    if query is not None:
            collect = collect.filter(
            Q(place_name__icontains=query)
            )

    return render(request,'new.html',{"search":collect})




def collection(request):

    collect = Place.objects.all()


    paginator =Paginator(collect, per_page=9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request,'collection.html',{
        'collect' : page_obj.object_list,
        # 'tags' : Place.tags.most_common(),
        'paginator' : paginator,
        'page_number' : int(page_number)
        })


def season(request):

   query = request.GET.get('query_name')
   # print(query)
    
   # print(query)

   name_p = query

   collect = Place.objects.filter(season__description__contains=query )

   return render(request,'season.html',{"search":collect,"name":name_p}) 
  
def states(request):

   query = request.GET.get('query_name')
   # print(query)
   
   name_p = query
   

   collect = Place.objects.filter(state__description__contains=query)
   # print(collect)


   return render(request,'states.html',{"search":collect,"name":name_p})
 

  
def type(request):

   query = request.GET.get('query_name')
   # print(query)
        
   name_p = query     

   collect = Place.objects.filter(place_type__description__contains=query)
   # print(collect)
   # collect = Place.objects.filter(state__contains=query)

   return render(request,'type.html',{"search":collect,"name":name_p})

   