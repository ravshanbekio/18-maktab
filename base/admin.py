from django.contrib import admin
from base.models import Blog, Comment, NewsletterFollowers, Contact, Describe

admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(NewsletterFollowers)
admin.site.register(Contact)
admin.site.register(Describe)