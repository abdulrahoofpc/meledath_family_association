# from django.urls import path
# from . import views

# urlpatterns = [
#     path('aipu_family',views.aipu_family_view, name='aipu_family'),
#     path('lonappan_family',views. lonappan_family_view, name='lonappan_family'),
#     path('francis_family/', views.francis_family_view, name='francis_family'),
#     path('thoma_family/', views.thoma_family_view, name='thoma_family'),
#     path('chakoru_family/', views.chakoru_family_view, name='chakoru_family'),
#     path('varunny_family/', views.varunny_family_view, name='varunny_family'),
#     path('kochuvareed_family/', views.kochuvareed_family_view, name='kochuvareed_family'),
    
# ]

from django.urls import path
from . import views

urlpatterns = [
    # Aipu Family URLs
    path('aipu/', views.family_tree, name='aipu-family'),
    path('aipu/<int:member_id>/', views.family_tree, name='aipu-family-member'),
    
    # Lonappan Family URLs
    path('lonappan/', views.lonappan_family_tree, name='lonappan-family'),
    path('lonappan/<int:member_id>/', views.lonappan_family_tree, name='lonappan-family-member'),
    
    # Francis Family URLs
    path('francis/', views.francis_family_tree, name='francis-family'),
    path('francis/<int:member_id>/', views.francis_family_tree, name='francis-family-member'),
    
    # Varunny Family URLs
    path('varunny/', views.varunny_family_tree, name='varunny-family'),
    path('varunny/<int:member_id>/', views.varunny_family_tree, name='varunny-family-member'),
    
    # Thoma Family URLs
    path('thoma/', views.thoma_family_tree, name='thoma-family'),
    path('thoma/<int:member_id>/', views.thoma_family_tree, name='thoma-family-member'),
    
    # Chakoru Family URLs
    path('chakoru/', views.chakoru_family_tree, name='chakoru-family'),
    path('chakoru/<int:member_id>/', views.chakoru_family_tree, name='chakoru-family-member'),
    
    # Kochuvareed Family URLs
    path('kochuvareed/', views.kochuvareed_family_tree, name='kochuvareed-family'),
    path('kochuvareed/<int:member_id>/', views.kochuvareed_family_tree, name='kochuvareed-family-member'),
    
    # Home URL - redirect to default family (Aipu)
    path('', views.family_tree, name='family-home'),
]