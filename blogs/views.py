from django.http import HttpResponse,HttpResponseRedirect
from miniblog.blogs.models import Artical,Tag,Artical_Tag,Comment
from django.shortcuts import render_to_response
from django.template import RequestContext
import datetime

tags = Tag.objects.all()

def home(request):
	artical_list = Artical.objects.all()
	return render_to_response('abstract.html',{'artical_list':artical_list,'tags':tags})
	
def artical(request,id):
	artical=Artical.objects.get(id = id)
        comment_list = Comment.objects.filter(artical = artical)
	return render_to_response('artical.html',{'artical':artical,'tags':tags,'comment_list':comment_list,'page_url':request.build_absolute_uri()},context_instance=RequestContext(request))

def articalsInTag(request,id):
	artical_tags = Artical_Tag.objects.filter(tag_id = id)
	artical_list = []
	for artical_tag in artical_tags:
		artical_list.append(Artical.objects.get(id = artical_tag.artical_id))
	return render_to_response('abstract.html',{'artical_list':artical_list,'tags':tags})

def about(req):
	return render_to_response('about.html')

def comment(request):
	post = request.POST
	artical_id = post['artical_id']
	name = post['name']
	email = post['email']
	site = post['site']
	content = post['content']
	page_url=post['page_url']
	artical=Artical.objects.get(id = artical_id)
	com = Comment(visitor_name=name,visitor_email=email,visitor_site=site,content=content,artical = artical)
	com.save()	
	return HttpResponseRedirect(page_url)
