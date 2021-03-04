from django.forms import forms
from django.forms import ModelForm
from Book.models import Book

#normal form



class BookCreateForm(ModelForm):

    class Meta:
        model=Book
        fields="__all__"
    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price")
        pages=cleaned_data.get("pages")
        if price<50:
            msg="invalid price prove value >50"
            self.add_error("price",msg)
        if pages<30:
            msg = "invalid page numbers"
            self.add_error("pages", msg)

class BookUpdateForm(ModelForm):
    """Book_name=models.CharField(max_length=120,unique=True)
    pages=models.IntegerField(default=50)
    price=models.IntegerField(default=50)
    author=models.CharField(max_length=75)"""
    class Meta:
        model=Book
        fields="__all__"
   #mobile project
   #create
   #view
   #edit
   #delete
