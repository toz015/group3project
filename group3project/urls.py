"""
URL configuration for group3project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from group3app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('get-auction/', views.get_auction_sql, name='getAuction'),
    path('get-popular-car/', views.get_popular_car_sql, name='getPopularCar'),
    path('get-vin-car/', views.get_vin_car_sql, name='getVinCar'),
    path('get-buyer-product/', views.get_buyer_product_sql , name='getBuyerProduct'),
    path('get-user-inform/', views.get_user_inform_sql, name='getUserInform'),
    path('get-time-report/', views.get_time_report_sql, name='getTimeReport'),
    path('get-car-inform/', views.get_car_inform_sql, name='getCarInform'),
    path('get-purchase-inform/', views.get_purchase_inform_sql, name='getPurchaseInform'),
    path('get-review-inform/', views.get_review_inform_sql, name='getReviewInform'),
    path('filter-cars/', views.filter_cars_sql, name='filterCars'),
    path('filter-cars-cont/', views.filter_cars_cont_sql, name='filterCarsCont'),
    path('filer-sellers/', views.filter_sellers_sql, name='filterSellers'),
    path('filer-buyers/', views.filter_buyers_sql, name='filterBuyers'),
    path('avg-sell-price/', views.avg_sell_price_sql, name='avgSellPrice'),
    path('delete-user/', views.delete_user_sql, name='deleteUser'),

]
