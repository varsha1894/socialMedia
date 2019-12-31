from __future__ import unicode_literals

from django.db import models

class Register(models.Model):
	name=models.CharField(max_length=120,blank=True)
	email=models.EmailField()
	password=models.CharField(max_length=120,blank=True)

	def _unicode_(self):
		return self.email

class collegeposts(models.Model):
	
	page_id=models.CharField(max_length=255)
	post_id=models.CharField(max_length=255)
	created_time=models.CharField(max_length=255)
	message=models.CharField(max_length=255)

class commerce(models.Model):
	Course_Name=models.CharField(max_length=255)
	Eligibility=models.CharField(max_length=255)
	Description=models.CharField(max_length=255)

class science(models.Model):
	Course_Name=models.CharField(max_length=255)
	Eligibility=models.CharField(max_length=255)
	Description=models.CharField(max_length=255)

class collegepages(models.Model):
	page_id=models.CharField(max_length=255)
	name=models.CharField(max_length=255)
	about=models.CharField(max_length=255)
	fan_count=models.IntegerField()
	location=models.CharField(max_length=255)
	link=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)

class keyword_search(models.Model):
    keyword=models.CharField(max_length=255)    	
    name=models.CharField(max_length=255)
    page_id=models.IntegerField()

class twitter_tweets(models.Model):
	keyword=models.CharField(max_length=255)
	tweet_text=models.CharField(max_length=255)
	created_at=models.DateTimeField()
	favourite_count=models.IntegerField()

class humanity(models.Model):
	Course_Name=models.CharField(max_length=255)
	Eligibility=models.CharField(max_length=255)
	Description=models.CharField(max_length=255)    

class keyword_post(models.Model):
	page_id=models.CharField(max_length=255)
	link=models.CharField(max_length=255)
	post_id=models.CharField(max_length=255)
	created_time=models.CharField(max_length=255)
	message=models.CharField(max_length=255)

class collegepages_commerce(models.Model):
	page_id=models.CharField(max_length=255)
	name=models.CharField(max_length=255)
	about=models.CharField(max_length=255)
	fan_count=models.IntegerField()
	location=models.CharField(max_length=255)
	link=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)

class collegepages_humanity(models.Model):
	page_id=models.CharField(max_length=255)
	name=models.CharField(max_length=255)
	about=models.CharField(max_length=255)
	fan_count=models.IntegerField()
	location=models.CharField(max_length=255)
	link=models.CharField(max_length=255)
	phone=models.CharField(max_length=255)

class collegeposts_commerce(models.Model):
	
	page_id=models.CharField(max_length=255)
	post_id=models.CharField(max_length=255)
	created_time=models.CharField(max_length=255)
	message=models.CharField(max_length=255)

class collegeposts_humanity(models.Model):
	
	page_id=models.CharField(max_length=255)
	post_id=models.CharField(max_length=255)
	created_time=models.CharField(max_length=255)
	message=models.CharField(max_length=255)
