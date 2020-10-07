
from django.urls import path
from.import views
urlpatterns = [
   path("", views.index, name="ShopHome"),
   path("about", views.about, name="Aboutus"),
   path("contact", views.contact, name="ContactUs"),
   path("tracker", views.tracker, name="TrackingStatus"),
   path("Search", views.search, name="Search"),
   path("products/<int:myid>", views.productView, name="ProductViews"),
   path("checkout", views.checkout, name="CheckOut"),
]