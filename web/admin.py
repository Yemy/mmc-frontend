from django.contrib import admin
from .models import (
    SiteSettings, Program, TeamMember, Testimonial, 
    Partner, Volunteer, Document, Event, 
    GalleryImage, BlogCategory, BlogPost, FAQ, Product, BankAccount
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
    list_display = ('full_name', 'email', 'phone', 'duration', 'submitted_at')
    list_filter = ('gender', 'duration', 'submitted_at', 'agreed_to_conduct')
    readonly_fields = ('submitted_at',)
    search_fields = ('full_name', 'email', 'phone')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'gender', 'date_of_birth', 'nationality', 'phone', 'email', 'address')
        }),
        ('Education & Background', {
            'fields': ('education_level', 'field_of_study', 'occupation', 'organization')
        }),
        ('Interests & Skills', {
            'fields': ('interests', 'skills', 'experience')
        }),
        ('Availability & Motivation', {
            'fields': ('duration', 'available_times', 'preferred_location', 'motivation')
        }),
        ('Emergency Contact & Commitment', {
            'fields': ('emergency_contact_name', 'emergency_contact_relation', 'emergency_contact_phone', 'agreed_to_conduct')
        }),
        ('Metadata', {
            'fields': ('submitted_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'account_name', 'account_number', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    search_fields = ('bank_name', 'account_number')

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
