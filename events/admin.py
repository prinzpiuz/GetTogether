from django.contrib import admin

# Register your models here.
from .models.locale import Language, Continent, Country, SPR, City
from .models.profiles import UserProfile, Organization, Team, Member
from .models.search import Searchable
from .models.events import Place, Event, Attendee

admin.site.register(Language)
admin.site.register(Continent)
admin.site.register(Country)

class SPRAdmin(admin.ModelAdmin):
    raw_id_fields = ('country',)
    list_filter =('country',)
    search_fields = ('name', 'country__name')
admin.site.register(SPR, SPRAdmin)

class CityAdmin(admin.ModelAdmin):
    raw_id_fields = ('spr',)
    list_filter =('spr__country',)
    search_fields = ('name', 'spr__name')
admin.site.register(City, CityAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'realname', 'avatar', 'web_url')
admin.site.register(UserProfile, ProfileAdmin)

class OrgAdmin(admin.ModelAdmin):
    list_display = ('name', 'site')
admin.site.register(Organization, OrgAdmin)

class TeamAdmin(admin.ModelAdmin):
    raw_id_fields = ('country', 'spr', 'city', 'owner_profile', 'admin_profiles', 'contact_profiles')
    list_display = ('__str__', 'member_count', 'owner_profile', 'created_date')
    ordering = ('-created_date',)
    def member_count(self, team):
        return team.members.all().count()
    member_count.short_description = 'Members'
admin.site.register(Team, TeamAdmin)

class SearchableAdmin(admin.ModelAdmin):
    list_display = ('event_url', 'start_time', 'federation_node', 'federation_time')
    list_filter = ('federation_node',)
    ordering = ('-start_time',)
admin.site.register(Searchable, SearchableAdmin)

class PlaceAdmin(admin.ModelAdmin):
    raw_id_fields = ('city',)
admin.site.register(Place, PlaceAdmin)

class EventAdmin(admin.ModelAdmin):
    raw_id_fields = ('place', 'created_by')
    list_display = ('__str__', 'attendee_count', 'created_by', 'created_time')
    ordering = ('-created_time',)
    def attendee_count(self, event):
        return event.attendees.all().count()
    attendee_count.short_description = 'Attendees'
admin.site.register(Event, EventAdmin)

admin.site.register(Member)
admin.site.register(Attendee)


