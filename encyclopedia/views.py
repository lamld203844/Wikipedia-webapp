import secrets
import markdown2

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util

class pageForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50, 
                            widget=forms.TextInput(attrs={
                                'placeholder':'Enter title',
                                'class': 'form-control mb-3'
                            }))
    content = forms.CharField(label="Content", max_length=1000,
                            widget=forms.Textarea(attrs={
                                'placeholder': 'Enter content as Markdown',
                                'class': 'form-control mb-3'
                            }))
    edit = forms.BooleanField(initial=False, widget= forms.HiddenInput(), required=False )
    
def index(request):
    list = util.list_entries()

    return render(request, "encyclopedia/index.html", {
        "entries": list,
        "value": "All pages",
        # Support for search in side bar
        "lists": list
    })

def login_view(request):
    if request.method == "POST":
        #Get username/password from data form
        username = request.POST["username"]
        password = request.POST["password"]

        #Authenticating
        user = authenticate(request, username=username, password=password)

        #If user is returned, login and route to index
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        # Otherwise, re-render page 
        else:
            return render(request, "encyclopedia/login.html", {
                "message": "Invalid credentials"
            })

    return render(request, "encyclopedia/login.html")

def logout_view(request):
    logout(request)
    list = util.list_entries()

    return render(request, "encyclopedia/index.html", {
            "entries": list,
            "value": "All pages",
            # Support for search in side bar
            "lists": list
        })

def showEntry_url(request, name):
    # Get entry 
    entry = util.get_entry(name)

    # Check existence of name
    if entry is None:
        return render(request, "encyclopedia/not_found.html", {
            "name": name,
            "lists": util.list_entries()
        })
    # Convert
    return render(request, "encyclopedia/show_entry.html", {
        "name": name,
        "entry": markdown2.markdown(entry),
        "lists": util.list_entries()
    })

def search(request):
    # get name from searching form
    value = request.GET.get('q','')
    # If NAME is exist,let's redirect with name
    if(util.get_entry(value) is not None):
        return HttpResponseRedirect(reverse("encyclopedia:show_entry", kwargs={
            'name': value,
        }))
    # If not, generating list of substring
    else:
        sub = []
        entries = util.list_entries()
        for entry in entries:
            if value.upper() in entry.upper():
                sub.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": sub,
            "value": "Search for " + value,
            "lists": util.list_entries()
        })
        
## ========================================
## When user create a new page
## Actual saving happens in this function 
## ========================================

def create_edit(request):
    # Check request method
    if request.method == "POST":
        # Take in data
        form = pageForm(request.POST)
        # Check data is valid (server side)
        if form.is_valid():
            # Isolate title from "cleaned" version of title
            title = form.cleaned_data["title"]
            # Check existing
            entry_existing = False
            lists = util.list_entries()
            for list in lists:
                if title.lower() == list.lower():
                    entry_existing = True
                    break
                
            # saving form when  forms is new or editing mode 
            if (entry_existing == False or form.cleaned_data["edit"] is True):
                # Isolate content from "cleaned" version of content
                content = form.cleaned_data["content"]
                # Saving process 
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse("encyclopedia:show_entry", kwargs={
                        'name': title
                    }))
            else:
                return render(request, "encyclopedia/create_edit.html", {
                        "form": form,
                        "existed": True,
                        "entry": title
                    })
        else:
        #if form is invalid, it renders page with existing information
            return render(request, "encyclopedia/create_edit.html",{
                "form": form,
                "existed": False
            })
            
    return render(request, "encyclopedia/create_edit.html",{
        "form": pageForm(),
        "existed": False
    })
def edit(request, name):
    # get existing data
    content = util.get_entry(name)
    # if entry isn't exist
    if content is None:
        return render(request, "encyclopedia/not_found.html",{
            'name': name,
            'lists': util.list_entries()
        })
    else:
        form = pageForm()
        form.fields["title"].initial = name
        # form.fields["title"].widget = forms.HiddenInput()
        form.fields["content"].initial = content
        form.fields["edit"].initial = True
        return render(request, "encyclopedia/create_edit.html", {
            'form':form,
            'editing': True,
            'title': name,
            'lists': util.list_entries()
        })



def random(request):
    name = secrets.choice(util.list_entries())
    return HttpResponseRedirect(reverse("encyclopedia:show_entry", kwargs={
        'name':name
    }))