from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:

            if self.deleted_forms and self._should_delete_form(form):
                continue
            elif form.cleaned_data.get('is_main'):
                count += 1
            if count > 1:
                raise ValidationError('Основным должен быть только один тег')
            elif count == 0:
                raise ValidationError('не указан тег')

        return super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 10
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_display_links = ['id', 'title']
    inlines = [ScopeInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


