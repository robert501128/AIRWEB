from django.shortcuts import render
from .models import Post
from pprint import  pprint

# Create your views here.


def maps(request):
    lass_locs = []
    cursor = Post.objects(loc__geo_within_box=[(119.428,21.878),(122.380,25.357)]).aggregate({"$group": { "_id":"$device_id", "loc":{"$max":"$loc"}}})
    for loc in cursor:
        if loc['loc']['coordinates'] not in lass_locs:
            lass_locs.append(swap(loc['loc']['coordinates']))



    print len(lass_locs)
    return render(request, 'index.html', { 'lass_locs': lass_locs })



def swap(coor):
    return [coor[1], coor[0]]
