from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import pyglet

def PlayView(request):
	if request.method=='GET':
		song=request.GET.get('song')
		#s=pyglet.media.load(str(song))
		#s.play()
		linkaddr = "/static/"+song
		return render_to_response('play.html',{'song':linkaddr})