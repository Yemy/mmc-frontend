from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('programs/', views.ProgramListView.as_view(), name='programs'),
    path('programs/<slug:slug>/', views.ProgramDetailView.as_view(), name='program_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('volunteer/', views.VolunteerCreateView.as_view(), name='volunteer'),
    path('documents/', views.DocumentListView.as_view(), name='documents'),
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('events/', views.EventListView.as_view(), name='event_list'),
    path('events/<slug:slug>/', views.EventDetailView.as_view(), name='event_detail'),
    path('shop/', views.ProductListView.as_view(), name='shop'),
    path('donate/', views.DonateView.as_view(), name='donate'),
]
