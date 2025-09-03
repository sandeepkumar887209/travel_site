from django.core.mail import send_mail
from django.conf import settings
from .forms import TravelQueryForm, ReviewForm
from .models import Review,TravelQuery
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@csrf_exempt
def home(request):
    reviews = Review.objects.order_by('-created_at')[:4]  # Show latest 5 reviews
    query_form = TravelQueryForm()

    if request.method == 'POST' and 'query_submit' in request.POST:
        query_form = TravelQueryForm(request.POST)
        if query_form.is_valid():
            query = query_form.save()

            # Send email
            subject = f"New Travel Query from {query.name}"
            message = f"""
            Name: {query.name}
            Email: {query.email}
            WhatsApp: {query.whatsapp_number}
            Destination: {query.destination}
            Travel Date: {query.travel_date}
            """
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['your_email@gmail.com'])
            except Exception as e:
                print("Email error:", e)

            return redirect('success')

    return render(request, 'home.html', {
        'form': query_form,
        'reviews': reviews
    })

def add_review(request):
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return render(request, 'success.html')  # After submission, go back to home
    return render(request, 'review.html', {'review_form': review_form})



def admin_reviews(request):
    review_list = Review.objects.all().order_by('-created_at')
    paginator = Paginator(review_list, 10)  # Show 10 reviews per page

    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)

    return render(request, 'admin_reviews.html', {'reviews': reviews})








def custom_login(request):
    if request.user.is_authenticated:
        return redirect('admin_queries')  # Redirect if already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin_queries')  # Redirect to queries page
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


@login_required(login_url='/login/')
def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def admin_queries(request):
    query_list = TravelQuery.objects.all().order_by('-created_at')
    paginator = Paginator(query_list, 10)  # Show 10 queries per page

    page_number = request.GET.get('page')
    queries = paginator.get_page(page_number)

    return render(request, 'admin_queries.html', {'queries': queries})




def success(request):
    return render(request, 'success.html')


