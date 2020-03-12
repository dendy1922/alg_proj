from django.contrib import admin
from .models import Algorithm_description, Algorithm_execution_result


@admin.register(Algorithm_description)
class AlgAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'big_o_notation',)


@admin.register(Algorithm_execution_result)
class AlgExecAdmin(admin.ModelAdmin):
    list_display = ('name_alg', 'timing', 'input_mas', 'result_mas',)
    list_filter = ('name_alg',)
    search_fields = ('name_alg__name', 'timing', 'input_mas', 'result_mas',)
