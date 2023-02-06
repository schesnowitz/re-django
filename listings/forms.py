from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
                    "title",
                    "price",
                    "num_bedrooms",
                    "num_bathrooms",
                    "address",
                    "square_footage",
                    "image"
                ]  