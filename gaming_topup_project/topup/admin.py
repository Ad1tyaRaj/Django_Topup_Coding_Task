from django.contrib import admin
from .models import Game, TopUpProduct, TopUpOrder

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'game_id', 'is_active']
    search_fields = ['name', 'game_id']

@admin.register(TopUpProduct)
class TopUpProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'game', 'price']
    search_fields = ['name', 'game__name']
    
class TopUpOrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'amount', 'created_at']
    search_fields = ['user__username', 'product__name']
    list_filter = ['created_at']
