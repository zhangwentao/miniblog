from django.db import models

class Tag(models.Model):
	name= models.CharField(max_length = 50)

class Artical(models.Model):
	title = models.CharField(max_length = 50)
	content = models.TextField(max_length = 20000)
	creation_time = models.DateTimeField(auto_now_add = True)
	modified_time = models.DateTimeField(auto_now = True)

class Artical_Tag(models.Model):
	artical_id = models.BigIntegerField()
	tag_id	= models.BigIntegerField()

class Touch_Ip(models.Model):
	ip = models.CharField(max_length = 30)

class Comment(models.Model):
	visitor_name = models.CharField(max_length = 50)
	visitor_email = models.CharField(max_length = 50)
	visitor_site = models.CharField(max_length = 50)
	content = models.TextField(max_length = 20000)
	creation_time = models.DateTimeField(auto_now_add = True)

class Artical_Comment(models.Model):
	artical_id = models.BigIntegerField()
	comment_id = models.BigIntegerField()

