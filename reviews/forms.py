from django import forms
from reviews.models import Review

class CreateReviewForm(forms.ModelForm):
  
  rating = forms.IntegerField(max_value=5, min_value=1)
  class Meta:
    model = Review
    fields = ("text","rating")

  def save(self):
    review = super().save(commit=False)
    return review
