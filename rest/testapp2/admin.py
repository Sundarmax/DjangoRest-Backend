from django.contrib import admin
from testapp2.models import *
from testapp.models import *
from adminsortable2.admin import SortableAdminMixin,SortableInlineAdminMixin


#Remove commented code and check the output in djagno admin page. 

# @admin.register(create_super_book)
# class MyModelAdmin(SortableAdminMixin, admin.ModelAdmin):
#     pass


# class MySubModelInline(SortableInlineAdminMixin, admin.TabularInline):  # or admin.StackedInline
#     model = create_super_book # A model which is having FK relationship called submodel

# @admin.register(add_subject)
# class MyModelAdmin(admin.ModelAdmin):
#     inlines = (MySubModelInline,)

class ButtonTabularInline(SortableInlineAdminMixin, admin.TabularInline):
    # We don't use the Button model but rather the juction model specified on Panel.
    model = Panel.buttons.through

@admin.register(Panel)
class PanelAdmin(admin.ModelAdmin):
    inlines = (ButtonTabularInline,)

admin.site.register(create_super_book)
#admin.site.register(Button)
#admin.site.register(Panel)
#admin.site.register(PanelButtons)

#admin.site.register(add_subject)
