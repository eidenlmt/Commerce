from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import User, listings, watchlist
from .forms import CreateListingsForm, BidsForm


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


@login_required
def create_listing(request):
    if request.method == 'POST':
        form = CreateListingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    return render(request, "auctions/create.html", {
        "form": CreateListingsForm()
    })


@login_required
def listing_view(request, listing_id):
    listing = get_object_or_404(listings, pk=listing_id)

    return render(request, "auctions/listings.html", {
        "listing": listing,
        "form": BidsForm()
    })


@login_required
def place_bid(request, listing_id):
    listing = get_object_or_404(listings, pk=listing_id)

    if request.method == 'POST':
        form = BidsForm(request.POST)
        if form.is_valid():
            form.save()
            listing.price = form.cleaned_data["bids"]
            listing.save()
            return HttpResponseRedirect(reverse("listing_view", args=[listing_id]))


@login_required
def watchlist_view(request):
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist.objects.filter(user=request.user)
    })


@login_required
def watchlist_add(request, listing_id):
    listing = get_object_or_404(listings, id=listing_id)
    already_existed = watchlist.objects.filter(user=request.user, item=listing)

    if already_existed.exists():
        already_existed.delete()
        messages.info(request, 'Successfully deleted from your watchlist')
        return HttpResponseRedirect(reverse("watchlist_view"))
    else:
        add = watchlist.objects.create(user=request.user, item=listing)
        add.save()
        messages.success(request, 'Successfully added to your watchlist')
        return HttpResponseRedirect(reverse("watchlist_view"))




