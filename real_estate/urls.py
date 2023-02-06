from django.conf import settings
from django.conf.urls.static import static
from listings.views import (
    listing_list, 
    listing_read, 
    listing_create, 
    listing_update,
    listing_delete
    )
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<pk>/', listing_read),
    path('listings/<pk>/edit/', listing_update),
    path('listings/<pk>/delete/', listing_delete),
    path('create-listing/', listing_create),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)