from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from ticketing.forms import ShowTimeSearchForm
from ticketing.models import Movie, Cinema, Showtime, Ticket


def movie_list(request):
    movies = Movie.objects.all()
    count = len(movies)
    context = {
        'movie_list': movies,
        'movie_count': count
    }
    return render(request, 'ticketing/movie_list.html', context)

def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas': cinemas
    }
    return render(request, 'ticketing/cinema_list.html', context)

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'ticketing/movie_details.html', context)

def cinema_details(request, cinema_id):
    cinema = get_object_or_404(Cinema, pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request, 'ticketing/cinema_details.html', context)


def showtime_list(request):
    search_form = ShowTimeSearchForm(request.GET)
    showtimes = Showtime.objects.all()
    if search_form.is_valid():
        showtimes = Showtime.objects.filter(movie__name__contains=search_form.cleaned_data['movie_name'])
        if search_form.cleaned_data['sale_is_open']:
            showtimes = showtimes.filter(status=Showtime.SALE_OPEN)
        if search_form.cleaned_data['movie_length_min'] is not None:
            showtimes = showtimes.filter(movie__length__gte=search_form.search_form.cleaned_data['movie_length_min'])
        if search_form.cleaned_data['movie_length_max'] is not None:
            showtimes = showtimes.filter(movie__length__lte=search_form.search_form.cleaned_data['movie_length_max'])
        if search_form.cleaned_data['cinema'] is not None:
            showtimes = showtimes.filter(cinema=search_form.cleaned_data['cinema'])
        min_price, max_price = search_form.get_price_boundries()
        if min_price is not None:
            showtimes = showtimes.filter(price__gt=min_price)
        if max_price is not None:
            showtimes = showtimes.filter(price__lte=max_price)

    showtimes = showtimes.order_by('start_time')
    context = {
        'showtimes': showtimes,
        'search_form': search_form
    }
    return render(request, 'ticketing/showtime_list.html', context)

@login_required
def showtime_details(request, showtime_id):
    showtime = Showtime.objects.get(pk=showtime_id)
    context = {
        'showtime': showtime
    }
    if request.method == 'POST':
        try:
            seat_count = int(request.POST['seat_count'])
            assert showtime.status == Showtime.SALE_OPEN, 'خرید این بلیت برای این سانس ممکن نیست'
            assert showtime.free_seats >= seat_count, 'به میزان انتخابی صندلی خالی وجود ندارد'
            total_price = showtime.price * seat_count
            assert request.user.profile.spend(total_price), 'موجودی کافی نیست'
            showtime.reserve_seats(seat_count)
            ticket = Ticket.objects.create(showtime=showtime, customer=request.user.profile, seat_count=seat_count)
        except Exception as e:
            context['error'] = str(e)
        else:
            return HttpResponseRedirect(reversed('ticketing:ticket_details', kwargs={'ticket_id': ticket.id}))
        return render(request, 'ticketing/showtime_details.html', context)

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(customer=request.user.profile).order_by('-order_time')
    context = {
       'tickets': tickets
    }
    return render(request, 'ticketing/ticket_list.hyml', context)

@login_required
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    context = {
        'ticket': ticket
    }
    return render(request, 'ticketing/ticket_details.html', context)
