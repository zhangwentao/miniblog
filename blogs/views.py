# coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from miniblog.blogs.models import Artical,Tag,Artical_Tag,Comment
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.syndication.views import Feed 
from blogs.models import Artical
import datetime
import markdown
import re
def home(request):
	tags = Tag.objects.all()
	artical_list = Artical.objects.all()
	return render_to_response('abstract.html',{'artical_list':artical_list,'tags':tags})
	
def artical(request,id):
	tags = Tag.objects.all()
	try:
		artical=Artical.objects.get(id = id)
	except:
		print 'error'
		return render_to_response('500.html',{'reason':'noThisArtical'});
        comment_list = Comment.objects.filter(artical = artical)
	response_dic = {'artical':artical,
			'tags':tags,
			'comment_list':comment_list,
			'page_url':request.build_absolute_uri()}
	return render_to_response('artical.html',response_dic,context_instance=RequestContext(request))

def articalsInTag(request,id):
	tags = Tag.objects.all()
	tag = Tag.objects.get(id = id)
	artical_tags = Artical_Tag.objects.filter(tag = tag)
	artical_list = []
	for artical_tag in artical_tags:
		artical_list.append(Artical.objects.get(id = artical_tag.artical.id))
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
	if name == '' or email == '' or content == '':
		return render_to_response("error.html",{"reason":"姓名、邮箱和内容是必填的。"})	
	if validateEmailAddr(email) == False:
		return render_to_response("error.html",{"reason":"你的邮箱地址的格式不对。"})	
	artical=Artical.objects.get(id = artical_id)
	com = Comment(visitor_name=name,visitor_email=email,visitor_site=site,content=content,artical = artical)
	com.save()	
	return HttpResponseRedirect(page_url)

def validateEmailAddr(addrString):
	pattern = re.compile("\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*")	
	result = re.search(pattern,addrString)
	if result == None:
		return False
	else:
		return True 

class BlogFeed(Feed):
	title = "文韬的BLOG"
	link = 'http://wentao.me'
	description = "wentao's blog"	
	def items(self):
		return Artical.objects.all()
	def item_title(self,item):
		return item.title
	def item_link(self,item):
		return self.link+'/blog/'+str(item.id)+'/'
	def item_description(self,item):
		return markdown.markdown(item.content)
