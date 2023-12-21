from django.shortcuts import render



def text_to_video(request):
    return render(request, 'text2video.html')
