from django.urls import path
from reviews import views
app_name = "reviews"

urlpatterns = [
  path("create/<int:pk>" , views.create_review , name="create"),
  path("<int:review_pk>/review/<int:kind_pk>/delete" , views.delete_review , name="delete")
]