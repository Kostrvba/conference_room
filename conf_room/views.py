from django.shortcuts import render, redirect
from django.views import View

from conf_room.models import Room


def MenuView(request):
    return render(request, 'menu.html')


class AddRoom(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'add_rooms.html', {'rooms': rooms})

    def post(self, request):
        name = request.POST['name']
        seats = request.POST['seats']
        projector = request.POST["projector"] == "on"
        Room.objects.create(name=name, seats=seats, projector=projector)
        return redirect('/room/new')
