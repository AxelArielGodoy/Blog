
from django.contrib import admin
from .models import Comment, Post


class PostAdmin(admin.ModelAdmin):

    reaonly_fields = ('creado', 'actualizado', 'id')
    list_display = ( 'titulo', 'autor', 'creado')
    list_filter = ('autor', 'creado')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)

