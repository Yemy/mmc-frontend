from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import (
    Program, TeamMember, Testimonial, Partner, 
    Volunteer, Document, BlogCategory, BlogPost, SiteSettings, FAQ, Event, Product, BankAccount
)

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programs'] = Program.objects.filter(is_active=True)[:3]
        context['testimonials'] = Testimonial.objects.all()
        context['partners'] = Partner.objects.all()
        context['latest_posts'] = BlogPost.objects.filter(status='published').order_by('-published_date')[:3]
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class TeamView(ListView):
    model = TeamMember
    template_name = 'team.html'
    context_object_name = 'team_members'

class ProgramListView(ListView):
    model = Program
    template_name = 'cause.html' # Assuming cause.html is the list view
    context_object_name = 'programs'

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'cause-details.html'
    context_object_name = 'program'

class ContactView(TemplateView):
    template_name = 'contact.html'

class VolunteerCreateView(CreateView):
    model = Volunteer
    template_name = 'volunteer_registration.html'
    fields = [
        'full_name', 'gender', 'date_of_birth', 'nationality', 'phone', 'email', 'address',
        'education_level', 'field_of_study', 'occupation', 'organization',
        'interests', 'skills', 'experience',
        'duration', 'available_times', 'preferred_location', 'motivation',
        'agreed_to_conduct', 'emergency_contact_name', 'emergency_contact_relation', 'emergency_contact_phone'
    ]
    success_url = reverse_lazy('web:index')

class DonateView(ListView):
    model = BankAccount
    template_name = 'donate.html'
    context_object_name = 'bank_accounts'

    def get_queryset(self):
        return BankAccount.objects.filter(is_active=True)

class DocumentListView(ListView):
    model = Document
    template_name = 'documents.html' # Needs to be created or integrated
    context_object_name = 'documents'

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog-grid.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return BlogPost.objects.filter(status='published').order_by('-published_date')

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog-details.html'
    context_object_name = 'post'

class FAQView(ListView):
    model = FAQ
    template_name = 'faq.html'
    context_object_name = 'faqs'

class EventListView(ListView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event-details.html'
    context_object_name = 'event'

class ProductListView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
