from django.contrib import admin
from django.urls import path
from prod import views

urlpatterns = [
    path('', views.show),
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('downloadall/', views.download_all_file),
    path('downloadsingle/<int:id>', views.download_single_file),
    path('downloadNoHt/', views.download_all, name='download'),
    path('downloadNoHtS/<int:id>', views.download_single, name='downloadS')
]
