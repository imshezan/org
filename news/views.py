from django.shortcuts import render
from .models import Post, Category, Gallery
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib.auth import authenticate, login, logout


def career(request):
    return render(request, 'career.html')


def contact_us(request):
    return render(request, 'contact-us.html', )


def donate(request):
    return render(request, 'donate.html', )


def index(request):
    return render(request, 'index.html')


def post_list(request, ):
    global context
    posts = Post.objects.all().order_by('-id')
    if 'category' in request.method == 'GET':
        posts = Category.objects.get(pk=int)(request.GET.get('category')).post_set.all()

    context = {
        'posts': posts
    }

    return render(request, 'press.html', context)


def view_post(request, pk):
    spost = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'spost': spost})


# Gallery

def gallery_view(request, ):
    global context
    pics = Gallery.objects.all().order_by('-id')
    if 'category' in request.method == 'GET':
        pics = Gallery.objects.get(id=int)

    context = {
        'pics': pics

    }

    return render(request, 'gallery.html', context)


def view_pic(request, img_id):
    spic = Gallery.objects.get(pk=img_id)
    context = {
        'spic': spic
    }
    return render(request, 'img.html', context)


def slider(request):
    slid = Gallery.objects.filter(id=True).order_by('-id')[0:3]

    context = {
        'slid': slid
    }

    render(request, 'slider.html', context)


def what_we_do(request):
    posts_list = Post.object.all()
    return render(request, 'who-we-are.html', {'post_list': posts_list})


def resources(request):
    return render(request, 'resources.html')


def thankyou(request):
    return render(request, 'thankyou.html')


def what_we_do(request):
    return render(request, 'what-we-do.html')


def where_we_work(request):
    return render(request, 'where-we-work.html')


def who_we_are(request):
    return render(request, 'who-we-are.html')


# User Login Log Out
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'thankyou.html')
        else:
            return HttpResponse("Username or password incorrect")
    return render(request, 'login.html')


# user log out

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
