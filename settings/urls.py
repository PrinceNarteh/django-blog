from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include("posts.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

admin.site.site_header = 'PriBlog'