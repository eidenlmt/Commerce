from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


from .models import User, listings, watchlist
from .forms import CreateListingsForm


def index(request):
    return render(request, "auctions/index.html", {
        "listings": listings.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def create_listing(request):
    if request.method == 'POST':
        form = CreateListingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    return render(request, "auctions/create.html", {
        "form": CreateListingsForm()
    })

def listing_view(request, listing_title):
    listing = listings.objects.get(title=listing_title)
    return render(request, "auctions/listings.html", {
        "listing": listing
    })


def watchlist_view(request):
    if "watchlist" not in request.session:
        request.session["watchlist"] = []
    return render(request, "auctions/watchlist.html", {
        "watchlist": request.session["watchlist"],
        "listings": listings.objects.all()
    })


def watchlist_add(request, listing_title):
    listing = get_object_or_404(listings, title=listing_title)
    already_existed = watchlist.objects.get(user=request.user, item=listing).exists()
    if already_existed:
        return render(request, "auctions/listings.html", {
            "message": "already in watchlist"
        })
    else:
        watchlist.objects.create(user=request.user, item=listing)
    
    return HttpResponseRedirect(reverse("watchlist_view"))

