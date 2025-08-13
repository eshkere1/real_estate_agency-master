from django.contrib import admin
from .models import Flat, Complaint, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ("town", "address", "owner")
    readonly_fields = ["created_at"]
    list_display = ("address", "price", "new_building", "construction_year", "town", "owners_phonenumber", "owner_pure_phone")
    list_editable = ["new_building"]
    list_filter = ["new_building", "rooms_number", "has_balcony"]
    raw_id_fields = ("liked_by",)

admin.site.register(Flat, FlatAdmin)

@admin.register(Complaint)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ("flat", "user")

@admin.register(Owner)

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)

class AdminInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ("owner", "flat")