"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/fin_reports/', include('fin_reports.urls')),
    path('api/reservation/', include('reservation.urls')),
    path('api/jeju_schedule/', include('jeju_schedule.urls')),
    path('api/jeju_data/', include('jeju_data.urls')),
    path('api/image/', include('image.urls')),
    path('api/user/', include('user.urls')),
    path('api/ledger/', include('ledger.urls'))
]
