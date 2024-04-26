from django.contrib import admin

from jambo.apps.customers import models


@admin.register(models.BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BusinessLocation)
class BusinessLocationAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Business)
class BusinessAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CustomerContact)
class CustomerContactAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
