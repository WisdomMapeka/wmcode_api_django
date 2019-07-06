from django.contrib import admin
from . models import Article, Comments, Comment_owner, Author

admin.site.register(Article)
admin.site.register(Comments)
admin.site.register(Comment_owner)
admin.site.register(Author)

