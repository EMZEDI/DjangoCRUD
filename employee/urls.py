from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('', views.intro),
    path('admin/', admin.site.urls),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('downloadall/', views.download_all_file),
    path('downloadsingle', views.download_single),
    path('downloadNoHt/', views.download_all, name='download')
]
