from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, "just_chat/index.html")


def room(request, room_name):
    return render(request, "just_chat/room.html", {
        "room_name_json": mark_safe(json.dumps(room_name)), 
        "username": mark_safe(json.dumps(request.user.username)),
        })
    