from django.shortcuts import render
from .models import Post
# Create your views here.
def maps(request):
  post_list = Post.objects()[0]
  return render(request, 'maps.html', {
	'post_list':post_list,
	})
