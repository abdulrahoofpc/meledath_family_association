from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import (
    Gallery, Event, Profile, Member, Memory, Topic,
    Comment, TeamMember, PremiumEvent, PremiumEventImage,
    Advertisement, LifeMember
)

# Premium Event
@admin.register(PremiumEvent)
class PremiumEventAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'date', 'location')
    search_fields = ('title', 'location')
    list_filter = ('date',)


@admin.register(PremiumEventImage)
class PremiumEventImageAdmin(admin.ModelAdmin):
    list_display = ('event', 'caption')


# Team Members
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_women_association')
    list_filter = ('is_women_association',)
    search_fields = ('name', 'position')
    prepopulated_fields = {'slug': ('name',)}


# Discussion (Topics & Comments)
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


# Memories
@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'death_date')
    search_fields = ('name',)
    list_filter = ('birth_date', 'death_date')


# Family Members (MPTT tree model)
admin.site.register(Member, MPTTModelAdmin)


# Profiles
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'phone_number', 'pin_code')
    search_fields = ('user__username', 'full_name', 'phone_number')
    list_filter = ('pin_code',)
    ordering = ('user__username',)


# Gallery
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('headline', 'subhead')
    search_fields = ('headline', 'subhead')
    ordering = ('headline',)


# Events
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('headline', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('headline', 'subhead')
    ordering = ('-date',)


# Advertisement
@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)


# Life Members
@admin.register(LifeMember)
class LifeMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'membership_no')
    search_fields = ('name', 'membership_no')
    ordering = ('membership_no',)
