from django.db import models

class Report(models.Model):
	name = models.CharField(max_length = 50, null = True)
	phone = models.CharField(max_length = 20, null = True)
	lat  = models.DecimalField(max_digits = 9, decimal_places = 6, null = True)
	lng = models.DecimalField(max_digits = 9, decimal_places = 6, null = True)
	address = models.CharField(max_length = 200, null = True)
	situation = models.TextField(null = True)
	details = models.CharField(max_length = 200, null = True)
	status = models.CharField(max_length = 200, null = True)
	image = models.ImageField(blank = True, null = True, upload_to = id)