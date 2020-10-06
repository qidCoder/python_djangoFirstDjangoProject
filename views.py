from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
#/ - redirects to the "/blogs" route with a method called "root"
def root(request):
    return redirect("/blogs")

#/blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

#/blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

#/blogs/create - redirect to the "/" route with a method called "create"
def create(request):
    return redirect('/')

#/blogs/< number > - display the string "placeholder to display blog number: {number}" with a method named "show" (eg. localhost:8000/blogs/15 should display the message: 'placeholder to display blog number 15')
def show(request, num):
    return HttpResponse(f"placeholder to display blog number: {num}")

#/blogs/< number >/edit - display the string "placeholder to edit blog {number}" with a method named "edit"
def edit(request, num):
    return HttpResponse(f"placeholder to edit blog {num}")

#/blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"
def destroy(request, num):
    return redirect('/blogs')

#(**Bonus**) /blogs/json - return a JsonResponse with title and content keys.
def json(request):
    return JsonResponse({"title":"My first blog", "content":"Lorem ipsum  dolor sit"})