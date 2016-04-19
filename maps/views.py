from django.shortcuts import render
from .models import Post
from pprint import  pprint

# Create your views here.


def maps(request):
    lass_locs = []
    device_id = []
    s_d0 = []
    cursor = Post.objects().order_by("-date").order_by("-time").aggregate({"$group": { "_id":"$device_id", "coordinates":{"$first":"$loc.coordinates"},"s_d0":{"$first":"$s_d0"}}})
    for document in cursor:
        if document['_id'] not in device_id:
	    device_id.append(document['_id'])
            lass_locs.append(swap(document['coordinates']))
	    s_d0.append(document['s_d0'])
            



    print len(lass_locs)
    return render(request, 'index.html', { 'lass_locs': lass_locs,'s_d0':s_d0,'device_id':device_id})



def swap(coor):
    return [coor[1], coor[0]]
