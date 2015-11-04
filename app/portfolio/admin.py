from django.contrib import admin
from django.conf import settings
from app.portfolio.models import *

class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('portfolioBaslik',)}
    list_display= ('portfolioBaslik','kategori')
    search_fields=['portffolioBaslik']
    
class KategoriAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug': ('baslik',)}
    
admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Kategori,KategoriAdmin)
