from django.http import JsonResponse
from django.shortcuts import render
import requests

def place_text_search(request):
	key = "AIzaSyATAFLFSnKUFSYOH5p-LINwRwhyMc9Pd-U"
	query = request.GET.get('query', 'coded')
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&region=kw&key=%s"%(query, key)

	next_page = request.GET.get('nextpage')
	if next_page is not None:
		url += "&pagetoken="+next_page

	response = requests.get(url)

	context = {
	"response": response.json()
	}
	return render(request, 'places_search.html', context)
	# return JsonResponse( response.json(), safe=False)

def place_detail(request):
	key = "AIzaSyATAFLFSnKUFSYOH5p-LINwRwhyMc9Pd-U"
	mapkey = "AIzaSyBg4zdZNrCn7-2GPTQsnkfboO2YLOD5BKE"
	place_id = request.GET.get('place_id','')
	url = "https://maps.googleapis.com/maps/api/place/details/json?key=%s&placeid=%s"%(key, place_id)

	response = requests.get(url)
	context = {
	"response": response.json(),
	"map": mapkey
	}
	return render(request, 'place_detail.html', context)
	#return JsonResponse( response.json(), safe=False)
