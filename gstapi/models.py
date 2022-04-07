from django.db import models

# # Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=100)
    state_code = models.CharField(max_length=2)
    cost = models.IntegerField(default=1, blank=True, null=True)

    def gst_amount(self):
        gst = 0
        igst= 0
        cgst=0
        if self.state_code == "MH":
            gst = (self.cost * 18)/100
            igst = cgst = gst/2
            return {
                'cgst':igst, 'igst' : cgst}
            
        else:
            gst = (self.cost * 18)/100
            return gst

    def __str__(self):
        return self.name

