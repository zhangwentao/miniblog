# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from miniblog.blogs.models import Artical,Tag,Artical_Tag,Touch_Ip,Comment,Artical_Comment
from django.shortcuts import render_to_response
import datetime
tags = Tag.objects.all()

def test(request):
	artical_list = Artical.objects.all()
	return render_to_response('abstract.html',{'artical_list':artical_list,'tags':tags})
	
def artical(request,id):
	artical=Artical.objects.get(id = id)
        artical_comments = Artical_Comment.objects.filter(artical_id = id)
	comment_list = []
	for artical_comment in artical_comments:
		comment_list.append(Comment.objects.get(id = artical_comment.comment_id))
	return render_to_response('artical.html',{'artical':artical,'tags':tags,'comment_list':comment_list,'page_url':request.build_absolute_uri()})

def articalsInTag(request,id):
	artical_tags = Artical_Tag.objects.filter(tag_id = id)
	artical_list = []
	for artical_tag in artical_tags:
		artical_list.append(Artical.objects.get(id = artical_tag.artical_id))
	return render_to_response('abstract.html',{'artical_list':artical_list,'tags':tags})

def about(req):
	return render_to_response('about.html')

def ip(request):
	return render_to_response('iptest.html')

def draw(request):
	return HttpResponse('2');
	
def cross(request):
	return render_to_response('crossdomain.xml',{})

def writeip(request):
        tip = Touch_Ip.objects.get(id = 1)
        tip.ip = request.GET['ip']
        tip.save()
        return HttpResponse('success')	

def readip(request):
	tip = Touch_Ip.objects.get(id = 1)
        return HttpResponse(tip.ip) 

def comment(request):
	get = request.GET
	artical_id = get['artical_id']
	name = get['name']
	email = get['email']
	site = get['site']
	content = get['content']
	page_url=get['page_url']
	com = Comment(visitor_name=name,visitor_email=email,visitor_site=site,content=content,creation_time=datetime.datetime.now())
	com.save()	
        ac=Artical_Comment(artical_id=artical_id,comment_id=com.id)
	ac.save()
	return HttpResponseRedirect(page_url)
