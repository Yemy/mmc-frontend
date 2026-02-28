import os
from django.db import models
from django.utils.text import slugify

class SiteSettings(models.Model):
    """
    Singleton model for static site-wide configuration.
    """
    name = models.CharField(max_length=255, default="Mulu Mesfin Charity (MMC)")
    logo = models.ImageField(upload_to='settings/', blank=True, null=True)
    favicon = models.ImageField(upload_to='settings/', blank=True, null=True)
    
    # Contact Info
    email = models.EmailField(blank=True, null=True)
    phone_1 = models.CharField(max_length=20, blank=True, null=True)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    map_iframe_url = models.TextField(help_text="Google Maps Iframe URL", blank=True, null=True)
    
    # About Suite
    mission = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    core_values = models.TextField(blank=True, null=True)
    founder_bio = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    about_text = models.TextField(blank=True, null=True)
    about_image = models.ImageField(upload_to='settings/', blank=True, null=True)
    
    # Social Links
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.name

class Program(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='programs/')
    description = models.TextField()
    impact_stats = models.CharField(max_length=255, help_text="e.g. 500+ Children Supported", blank=True, null=True)
    goal = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    raised = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def get_percentage(self):
        if self.goal <= 0:
            return 0
        return (self.raised / self.goal) * 100

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='team/')
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, help_text="e.g. Beneficiary, Partner")
    quote = models.TextField()
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partners/')
    website_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Document(models.Model):
    DOC_TYPES = (
        ('report', 'Technical/Progress Report'),
        ('legal', 'Legal Document (License, etc.)'),
        ('policy', 'Privacy Policy/Terms'),
    )
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    doc_type = models.CharField(max_length=20, choices=DOC_TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption or f"Gallery Image {self.pk}"

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, related_name='posts')
    author = models.CharField(max_length=100, default="Admin")
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    published_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question
