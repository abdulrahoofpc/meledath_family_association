from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    AipuFamily,
    LonappanFamily,
    FrancisFamily,
    VarunnyFamily,
    ThomaFamily,
    ChakoruFamily,
    KochuvareedFamily
)

class FamilyMemberAdmin(MPTTModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_order', 'parent', 'membership_category')
    list_editable = ('birth_order',)
    ordering = ('birth_order', 'first_name')

admin.site.register(LonappanFamily, FamilyMemberAdmin)
admin.site.register(AipuFamily, FamilyMemberAdmin)
admin.site.register(FrancisFamily, FamilyMemberAdmin)
admin.site.register(VarunnyFamily, FamilyMemberAdmin)
admin.site.register(ThomaFamily, FamilyMemberAdmin)
admin.site.register(ChakoruFamily, FamilyMemberAdmin)
admin.site.register(KochuvareedFamily, FamilyMemberAdmin)