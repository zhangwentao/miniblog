# Create your views here.
from django.http import HttpResponse
from miniblog.blogs.models import Artical,Tag,Artical_Tag,Touch_Ip
from django.shortcuts import render_to_response

tags = Tag.objects.all()

def test(request):
	artical_list = Artical.objects.all()
	return render_to_response('abstract.html',{'artical_list':artical_list,'tags':tags})
	
def artical(request,id):
	artical=Artical.objects.get(id = id)
	return render_to_response('artical.html',{'artical':artical,'tags':tags})

def articalsInTag(request,id):
	artical_tags = Artical_Tag.objects.filter(tag_id = id)
	artical_list = []
	for artical_tag in artical_tags:
		artical_list.append(Artical.objects.get(id = artical_tag.artical_id))
	return render_to_response('abstract.html',{'artical_list':artical_list,'tags':tags})

def about(req):
	return render_to_response('about.html')

def draw(request):
	return HttpResponse('2');
	
def cross(request):
	return render_to_response('crossdomain.xml',{})

def writeip(request,ip):
        tip = Touch_Ip.objects.get(id = 1)
        tip.ip = ip
        tip.save()
        return HttpResponse(ip)	

def readip(request):
	tip = Touch_Ip.objects.get(id = 1)
        return HttpResponse(tip.ip) 
