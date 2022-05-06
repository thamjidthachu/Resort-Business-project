from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Services, Images, Comments


# Register your models here.
class ImagesList(admin.ModelAdmin):
    model = Images


class ImagesInline(admin.StackedInline):
    model = Images
    extra = 0

    # class CommentsInline(admin.TabularInline):
    #     model = Comments
    #     can_delete = False
    #     readonly_fields = ('author', 'message', 'comment_time')
    #     verbose_name_plural = 'Comments'

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class CommentAdmin(admin.ModelAdmin):
    list_display = ('message', 'author', 'object_id', 'content_type')
    list_filter = ['content_type', 'author']


class ServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'discription']}),
        ('Date information', {'fields': ['create_time'], 'classes': ['collapse']}),
    ]
    inlines = [ImagesInline]
    list_display = ('name', 'create_time',)
    readonly_fields = ('create_time',)


admin.site.register(Services, ServiceAdmin)
admin.site.register(Comments, CommentAdmin)
admin.site.register(Images, ImagesList)
