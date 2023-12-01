from django.shortcuts import render


def index(request):
    return render(request,"index.html")


def text_to_video(request):
    return render(request, 'text2video.html')
