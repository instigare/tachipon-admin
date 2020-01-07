from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Report

import time

@method_decorator(login_required, name='dispatch')
class ReportListView(generic.ListView):
	model = Report

@method_decorator(login_required, name='dispatch')
class ReportDetailView(generic.DetailView):
	model = Report

@login_required
@csrf_exempt
def delete(request):
	reportid = request.GET.get('id', '')

	reportinst = Report.objects.get(id = reportid)
	reportinst.delete()

	# return JsonResponse({
	# 	'status': 'deleted',
	# })

	return redirect('/')

@login_required
@csrf_exempt
def update(request):
	reportid = request.GET.get('id', '')

	reportinst = Report.objects.get(id = reportid)
	reportinst.status = 1
	reportinst.save()

	# return JsonResponse(
	# 	{
	# 		'name': reportinst.name,
	# 		'phone': reportinst.phone,
	# 		'lat': reportinst.lat,
	# 		'lng': reportinst.lng,
	# 		'situation': reportinst.situation,
	# 		'details': reportinst.details,
	# 		'status': reportinst.status,
	# 	}
	# )

	return redirect('/')

@csrf_exempt
def report(request):
	name = request.POST.get("name", None)
	phone = request.POST.get("phone", None)
	lat = request.POST.get("lat", None)
	lng = request.POST.get("lng", None)
	situation = request.POST.get("situation", None)
	details = request.POST.get("details", None)
	image = request.POST.get("image", None)

	# insert calculator to get address using lat and lng

	newreport = Report()
	newreport.name = name
	newreport.phone = phone
	newreport.lat = lat
	newreport.lng = lng
	newreport.situation = situation
	newreport.details = details
	newreport.status = 0
	newreport.save()
	
	return JsonResponse(
		{
			'name': name,
			'phone': phone,
			'lat': lat,
			'lng': lng,
			'situation': situation,
			'details': details,
			'image': image,
			'reportcode': '0',
		}
	)

# curl -d "name=value1&phone=value2&lat=0.000000&" -H "Content-Type: application/x-www-form-urlencoded" -X POST http://127.0.0.1:8000/manager/report
# https://stackoverflow.com/questions/57131896/how-do-i-save-google-places-location-to-django-models