from django.shortcuts import render
from .models import Post
from pprint import  pprint

# Create your views here.


def maps(request):
    lass_locs = []
    for loc in Post.objects(loc__geo_within_box=[(119.428,21.878),(122.380,25.357)]).distinct(field='loc'):
        if loc['coordinates'] not in lass_locs:
            lass_locs.append(swap(loc['coordinates']))



    print len(lass_locs)
    return render(request, 'index.html', { 'lass_locs': lass_locs })



def swap(coor):
    return [coor[1], coor[0]]