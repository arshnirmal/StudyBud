from django.http import HttpResponse
from django.shortcuts import render
from base.form import RoomForm

from base.models import Room

# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Let\'s talk about Django'},
#     {'id': 2, 'name': 'Let\'s talk about Python'},
#     {'id': 3, 'name': 'Let\'s talk about JavaScript'},
# ]


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, key):
    # room = None
    # for r in rooms:
    #     if r['id'] == int(key):
    #         room = r
    #         break

    room = Room.objects.get(id=key)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/create_room.html', context)
