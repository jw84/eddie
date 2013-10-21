from django.http import HttpResponse

def index(request):
	return HttpResponse('<html><title>screensaver</title></html>')
