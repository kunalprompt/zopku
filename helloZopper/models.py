from mongoengine import *
from django.conf import settings

class Pincodes(Document):
	officename = StringField()
	pincode = IntField()
	officeType = StringField()
	Deliverystatus = StringField()
	divisionname = StringField()
	regionname = StringField()
	circlename = StringField()
	Taluk = StringField()
	Districtname = StringField()
	statename = StringField()