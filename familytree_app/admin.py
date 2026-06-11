# /home/keyurjoshi/familytree_project/familytree_app/admin.py
from django.contrib import admin
from django import forms
from .models import City, FamilyIdentification, FamilyMember, Photo, msgKind, sandesha, comments, instructions

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent'].label_from_instance = lambda obj: f'{obj.id} - {obj.full_name}'
        self.fields['spouse'].label_from_instance = lambda obj: f'{obj.id} - {obj.full_name}'

@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    form = FamilyMemberForm
    list_display = ('id', 'full_name', 'parent', 'spouse')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(FamilyIdentification)
class FamilyIdentificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

@admin.register(msgKind)
class MsgKindAdmin(admin.ModelAdmin):
    list_display = ('id', 'msgK')

@admin.register(sandesha)
class SandeshaAdmin(admin.ModelAdmin):
    list_display = ('id', 'msg')

@admin.register(instructions)
class InstructionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'srNo', 'msg')

@admin.register(comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'msg', 'mobile', 'surname', 'name', 'city')
