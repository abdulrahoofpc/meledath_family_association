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

admin.site.register(LonappanFamily, MPTTModelAdmin)
admin.site.register(AipuFamily, MPTTModelAdmin)
admin.site.register(FrancisFamily, MPTTModelAdmin)
admin.site.register(VarunnyFamily, MPTTModelAdmin)
admin.site.register(ThomaFamily, MPTTModelAdmin)
admin.site.register(ChakoruFamily, MPTTModelAdmin)
admin.site.register(KochuvareedFamily, MPTTModelAdmin)


