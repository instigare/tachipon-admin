from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
	return render(request, 'index.html')

@csrf_exempt
def report(request):
	name = request.POST.get("name", None)
	phone = request.POST.get("phone", None)
	address = request.POST.get("address", None)
	situation = request.POST.get("situation", None)
	details = request.POST.get("details", None)
	image = request.POST.get("image", None)

	# insert sql to add request to database 
	
	return JsonResponse(
		{
			'name': name,
			'phone': phone,
			'address': address,
			'situation': situation,
			'details': details,
			'image': image,
			'reportcode': '0',
		}
	)