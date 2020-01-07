from django.db import models

class Report(models.Model):
	name = models.CharField(max_length = 50)
	phone = models.CharField(max_length = 20)
	lat  = models.DecimalField(max_digits = 9, decimal_places = 6)
	lng = models.DecimalField(max_digits = 9, decimal_places = 6)
	address = models.CharField(max_length = 200)
	situation = models.TextField()
	details = models.CharField(max_length = 200)
	status = models.CharField(max_length = 200)
	image = models.ImageField(blank = True, null = True, upload_to = id)