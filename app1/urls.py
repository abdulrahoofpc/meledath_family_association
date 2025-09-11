from django.urls import path
from . import views

urlpatterns = [
    # ----- Basic pages -----
    path("", views.Home, name="home"),
    path("family-pillars/", views.FamilyPillars, name="family_pillars"),
    path("history/", views.History, name="history"),

    # ----- Team -----
    path("team/", views.team_list, name="team"),
    path("team/<slug:slug>/", views.team_detail, name="team_detail"),

    # ----- Authentication -----
    path("register/", views.register, name="register"),
    path("login/", views.custom_login, name="login"),
    path("logout/", views.custom_logout, name="logout"),

    # ----- Extras -----
    path("memory/<int:id>/", views.memory_detail, name="memory_detail"),
    path("premium-events/", views.premium_event_view, name="premium_event_list"),
    path("premium-events/<slug:slug>/", views.premium_event_detail, name="premium_event_detail"),
    path("discussion/", views.discussion_view, name="discussion"),
    path("post-comment/", views.post_comment, name="post_comment"),
    path("familytree1/", views.FamilyTree1, name="familytree1"),
    path("events/", views.event_list, name="events"),
    path("gallery/", views.gallery_list, name="gallery"),

    # ----- Advertisements -----
    # path("advertisements/", views.advertisement_list, name="advertisement_list"),  # Optional listing page
]
