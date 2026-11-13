from django.contrib import admin
from .models import Raca, Animal,Tutor, Vacina


class VacinasInLine(admin.TabularInline):
    model = Vacina #Formulário de objeto vacina
    extra = 1      #Adiciona uma vacina por vez


class AnimalAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Dados do animal", {"fields": ["raca", "nome", "tipo_animal", "nascimento"]}),
        ("Dados do tutor do animal", {"fields": ["tutor"]}),
    ]
    inlines = [VacinasInLine]


admin.site.register(Raca)
admin.site.register(Tutor)
admin.site.register(Animal, AnimalAdmin)