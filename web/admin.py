from django.contrib import admin
from .models import (
    SiteSettings, Program, TeamMember, Testimonial, 
    Partner, Volunteer, Document, Event, 
    GalleryImage, BlogCategory, BlogPost, FAQ, Product
)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_1')
    
    def has_add_permission(self, request):
        # Prevent creating more than one SiteSettings instance
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'impact_stats', 'is_active', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    list_editable = ('order',)
    search_fields = ('name', 'role')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website_url')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'submitted_at')
    readonly_fields = ('submitted_at',)
    search_fields = ('full_name', 'email')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'doc_type', 'uploaded_at')
    list_filter = ('doc_type',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'created_at')

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'published_date')
    list_filter = ('status', 'category')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
