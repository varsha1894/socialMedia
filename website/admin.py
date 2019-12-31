from django.contrib import admin

# Register your models here.
from .models import Register,collegeposts,commerce,science,collegepages,keyword_search,twitter_tweets

admin.site.register(Register)
admin.site.register(collegeposts)
admin.site.register(commerce)
admin.site.register(science)
admin.site.register(collegepages)
admin.site.register(keyword_search)
admin.site.register(twitter_tweets)

