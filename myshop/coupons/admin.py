from import_export.admin import ImportExportActionModelAdmin

from django.contrib import admin

from myshop.coupons.models import Coupon


# @admin.register(Coupon)
# class CouponAdmin(admin.ModelAdmin):
#     list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
#     list_filter = ['active', 'valid_from', 'valid_to']
#     search_fields = ['code']

class CouponAdmin(ImportExportActionModelAdmin):

    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
