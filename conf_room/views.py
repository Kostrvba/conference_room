from django.shortcuts import render, redirect
from django.views import View

from conf_room.models import Room


class MenuView(View):
    def get(self, request):
        return render(request, 'menu.html')


class AddRoom(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'add_rooms.html', {'rooms': rooms})

    def post(self, request):
        name = request.POST['name']
        seats = int(request.POST['seats'])
        projector = request.POST.get("projector") == "on"

        if not name:
            return render(request, 'add_rooms.html', context={"error": "You must add room name"})
        if seats <= 0:
            return render(request, 'add_rooms.html', context={"error": "Room must have more seats than 0"})
        if Room.objects.filter(name=name).first():
            return render(request, 'add_rooms.html', context={"error": "You have a room under this name"})

        Room.objects.create(name=name, seats=seats, projector=projector)
        return redirect('/menu')


class RoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'all_rooms.html', {'rooms': rooms})
