from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('index', views.MainIndexView.as_view()),
    path('sign', views.SignIndexView.as_view(), name = "sign_view"),
    path('tableproduct', views.ProductView.as_view(), name="tables_view"),
    path('tablecustomer', views.CustomerTablesView.as_view(), name = "tablescustom_view"),
    path('regProduct', views.regProductView.as_view(), name = "registerprod_view"),
    path('dashboard', views.dashboardView.as_view(), name = 'dashboard_view'),
]
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)