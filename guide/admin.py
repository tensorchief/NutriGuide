from django.contrib import admin

# Register your models here.
from guide.models import Profile, Ingredient, Meal, NutritionGoal, PreparationStep, Recipe


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', )
    search_fields = ['user__username',
                     'user__last_name',
                     'user__first_name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ingredient)
admin.site.register(Meal)
admin.site.register(NutritionGoal)
admin.site.register(PreparationStep)
admin.site.register(Recipe)
