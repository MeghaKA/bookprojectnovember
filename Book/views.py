from django.shortcuts import render
from .forms import BookCreateForm,BookUpdateForm
from .models import Book
from django.shortcuts import redirect

# Create your views here.

#Book/create
    #1)get functionality for creating book,return all book objects
    #2)postcreating a book




def Book_create(request):

    form=BookCreateForm()
    context={}
    context["form"]=form
    template_name="Book/bookcreate.html"
    books=Book.objects.all()
    context["Book"]=books
    if request.method=="POST":
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            print("insidee")
            return redirect("create")
        else:
            context["form"]=form
            return render(request,template_name,context)




#Book/view/1
     #get return boom with corresponding id

def view_Book(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["Book"]=book
    return render(request,"Book/bookview.html",context)





#Book/update/1
    #get return boom with corresponding id
    #post update book
def update_Book(request,id):
    book=Book.objects.get(id=id)
    form=BookUpdateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookUpdateForm(request.POST,instance=Book)
        if form.is_valid():
            form.save()
            return redirect("create")
        else:
            form=BookUpdateForm(request.POST,instance=Book)
            context["form"] = form
            return render(request, "Book/bookedit.html", context)
    return render(request,"Book/bookedit.html",context)
#Book/delete/1
    #get delete book with id

def delete_Book(request,id):
    Book.objects.get(id=id).delete()
    return redirect("create")


