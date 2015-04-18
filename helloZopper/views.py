from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound

# csrf
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

#import settings.py
from django.conf import settings

#including forms and models
from models import *

# cache control
from django.views.decorators.cache import cache_control

# other python modules
import bson
import json
import time
from datetime import date

@csrf_exempt
@cache_control(private=True)
def indexView(request):
	if request.method=="GET":
		return render(request, 'index.html')

@csrf_exempt
@cache_control(private=True)
def searchRecordsAPI(request):
	if request.method=="POST":
		postData = json.loads(request.body)
		taluk = postData["locality"].title()
		district = postData["district"].title()
		state = postData["state"].upper()
		pincode = postData["pincode"]
		min_query = Q(Taluk=taluk)
		if district!="":
			min_query &= Q(Districtname=district)
		if state!="":
			min_query &= Q(statename=state)
		if pincode!="":
			pincode = int(pincode)
			min_query &= Q(pincode=pincode)		
		records = Pincodes.objects.filter(min_query)
		output = []
		for i in records:
			rec = {
				# "id": str(i.id),
				"officename": i["officename"],
				"pincode": i["pincode"],
				# "officeType": i["officeType"],
				# "division": i["divisionname"],
				# "region": i["regionname"],
				# "circle": i["circlename"],
				"taluk": i["Taluk"],
				"district": i["Districtname"],
				"state": i["statename"].title(),
			}
			output.append(rec)
		output = sorted(output, key=lambda x: x["pincode"])
		return HttpResponse(json.dumps({'response': 200, "result": output }), content_type='application/json')

@csrf_exempt
def crudReadView(request):
	if request.method=="GET":
		return render(request, "crud-read.html")

@csrf_exempt
def crudReadDeleteAPI(request, id):
	if request.method=="GET":
		try:
			record = Pincodes.objects.get(id=id)
			record = {
				"officename": record["officename"],
				"pincode": record["pincode"],
				"officeType": record["officeType"],
				"division": record["divisionname"],
				"region": record["regionname"],
				"circle": record["circlename"],
				"taluk": record["Taluk"],
				"district": record["Districtname"],
				"state": record["statename"].title(),
			}
			return HttpResponse(json.dumps({'response': 200, "result": record }), content_type='application/json')
		except Exception, e:
			return HttpResponse(json.dumps({'response': 400, "result": {} }), content_type='application/json')
		else:
			return HttpResponse(json.dumps({'response': 400, "result": {} }), content_type='application/json')
	elif request.method=="DELETE":
		try:
			record = Pincodes.objects.get(id=id).delete()
			return HttpResponse(json.dumps({ 'response': 200 }), content_type='application/json')
		except Exception, e:
			return HttpResponse(json.dumps({ 'response': 400 }), content_type='application/json')
		else:
			return HttpResponse(json.dumps({ 'response': 400 }), content_type='application/json')

@csrf_exempt
def crudCreateRecordView(request):
	if request.method=="GET":
		return render(request, "crud-create.html")

@csrf_exempt
def crudUpdateRecordView(request):
	if request.method=="GET":
		return render(request, "crud-update.html")


@csrf_exempt
def crudCreateUpdateAPI(request):
	if request.method=="POST":
		postData = json.loads(request.body)		
		officename = str(postData["officeName"]).title()
		pincode = int(postData["pincode"])
		officetype = str(postData["officeType"]).title()
		deliverystatus = str(postData["deliveryStatus"]).title()
		divisionname = str(postData["divisionName"]).title()
		regionname = str(postData["regionName"]).title()
		circlename = str(postData["circleName"]).title()
		taluk = str(postData["taluk"]).title()
		district = str(postData["districtName"]).title()
		state = str(postData["stateName"]).upper()
		try:
			record = Pincodes.objects.create(
				officename=officename,
				pincode=pincode,
				officeType=officetype,
				Deliverystatus=deliverystatus,
				divisionname=divisionname,
				regionname=regionname,
				circlename=circlename,
				Taluk=taluk,
				Districtname=district,
				statename=state
			)
			result = "Object created with id - " + str(record.id)
			return HttpResponse(json.dumps({'response': 200, 'result': result }), content_type='application/json')
		except Exception, e:
			return HttpResponse(json.dumps({'response': 400 }), content_type='application/json')
	elif request.method=="PUT":
		postData = json.loads(request.body)
		oid = 	str(postData["id"])
		officename = str(postData["officeName"]).title()
		pincode = int(postData["pincode"])
		officetype = str(postData["officeType"]).title()
		deliverystatus = str(postData["deliveryStatus"]).title()
		divisionname = str(postData["divisionName"]).title()
		regionname = str(postData["regionName"]).title()
		circlename = str(postData["circleName"]).title()
		taluk = str(postData["taluk"]).title()
		district = str(postData["districtName"]).title()
		state = str(postData["stateName"]).upper()
		try:
			record = Pincodes.objects.get(id=oid).update(
				set__officename=officename,
				set__pincode=pincode,
				set__officeType=officetype,
				set__Deliverystatus=deliverystatus,
				set__divisionname=divisionname,
				set__regionname=regionname,
				set__circlename=circlename,
				set__Taluk=taluk,
				set__Districtname=district,
				set__statename=state
			)
			return HttpResponse(json.dumps({'response': 200 }), content_type='application/json')
		except Exception, e:
			return HttpResponse(json.dumps({'response': 400 }), content_type='application/json')


