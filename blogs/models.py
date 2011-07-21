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
