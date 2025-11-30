from django.contrib import admin
from django.urls import path, include
from .views import dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='dashboard'),

    path('settings/', include('settings_app.urls')),
    path('customers/', include('customers_app.urls')),
    path('shipments/', include('shipments_app.urls')),
    path('transport/', include('transport_app.urls')),
    path('workflow/', include('workflow_app.urls')),
    path('alerts/', include('alerts_app.urls')),
    path('accounts/', include('accounts_app.urls')),


]

handler403 = "accounts_app.views.handle_403"
