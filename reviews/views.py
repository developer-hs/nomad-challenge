from django.shortcuts import redirect , reverse
from reviews.forms import CreateReviewForm
from movies.models import Movie
from books.models import Book


def create_review(request , pk):
  if request.method == "POST":
    form = CreateReviewForm(request.POST)
    kind = request.GET.get('kind', 'movie')
    
    if form.is_valid():
      review = form.save()
      
      if kind == "movie":
        try:
          movie = Movie.objects.get(pk=pk)
          review.movie = movie
        except Movie.DoesNotExist:
          return redirect(reverse("core:home"))
          
      else:
        try:
          book = Book.objects.get(pk = pk)
          review.book = book
        except Book.DoesNotExist:
          return redirect(reverse("core:home"))

      review.created_by = request.user
      review.save()
      return redirect(reverse(f"{kind}s:{kind}" , kwargs={"pk" : pk}))

def delete_review(request,review_pk,kind_pk):
  kind = request.GET.get("kind", "movie")
  
  if kind == "movie":
    try:
      obj = Movie.objects.get(pk = kind_pk)
    except Movie.DoesNotExist:
      return redirect(reverse("core:home"))
  else:
    try:
      obj = Book.objects.get(pk = kind_pk)
    except Book.DoesNotExist:
      return redirect(reverse("core:home"))
  
  review = obj.reviews.get(pk = review_pk)
  if request.user == review.created_by:
    obj.reviews.remove(review)
    return redirect(reverse(f"{kind}s:{kind}" , kwargs={"pk" : kind_pk}))

  return redirect(reverse("core:home"))
    


