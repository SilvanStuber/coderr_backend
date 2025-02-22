"""
URL configuration for coderr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from offers_app.api.urls import offer_patterns, offerdetail_patterns
from orders_app.api.urls import order_patterns, order_count_patterns, completed_order_count_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', include('login_app.api.urls')),
    path('api/registration/', include('registration_app.api.urls')),
    path('api/base-info/', include('base_info_app.api.urls')), 
    path('api/profile/', include('profile_app.api.urls')),
    path('api/profiles/', include('profile_app.api.urls')),
    path('api/reviews/', include('reviews_app.api.urls')), 
    path('api/offers/', include((offer_patterns, 'offers_app'), namespace='offers')),
    path('api/offerdetails/', include((offerdetail_patterns, 'offers_app'), namespace='offerdetails')),
    path('api/orders/', include((order_patterns, 'orders_app'), namespace='orders')),
    path('api/order-count/', include((order_count_patterns, 'orders_app'), namespace='order-count')),
    path('api/completed-order-count/', include((completed_order_count_patterns, 'orders_app'), namespace='completed-order-count')),
] + staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

