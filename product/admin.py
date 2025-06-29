from django.contrib import admin
from .models import Category, Product, Review

class ReviewInline (admin.StackedInline):
    model = Review
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = 'title price category'.split()
    list_filter = 'price'.split()
    list_editable = 'price category'.split()
    search_fields = 'title description'.split()

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
