from django.db import models
from django.forms import ModelForm

# Create your models here.
class UserInfo(models.Model): 
	username = models.CharField(max_length = 200)
	firstname = models.CharField(max_length = 200)
	middle  = models.CharField(max_length = 200)
	lastname = models.CharField(max_length = 200)
	dobday = models.CharField(max_length = 200)
	dobmonth = models.CharField(max_length = 200)
	dobyear = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	homephone = models.CharField(max_length = 200)
	cell  = models.CharField(max_length = 200)
	address1 = models.CharField(max_length = 200)
	address2 = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)
	state = models.CharField(max_length = 200)
	zipcode = models.CharField(max_length = 200)
	employername = models.CharField(max_length = 200)
	employeraddress1 = models.CharField(max_length = 200)
	employeraddress2 = models.CharField(max_length = 200)
	employercity = models.CharField(max_length = 200)
	employerzip = models.CharField(max_length = 200)
	employerphone = models.CharField(max_length = 200)
	jobtitle = models.CharField(max_length = 200)
	governmentIDtype = models.CharField(max_length = 200)
	governmentIDnumber = models.CharField(max_length = 200)
	governmentIDissuecountry = models.CharField(max_length = 200)
	governmentIDissuestate = models.CharField(max_length = 200)
	governmentIDissue  = models.CharField(max_length = 200)
	governmentIDexpiredate = models.DateField()
	beneficiaryID = models.CharField(max_length = 200)

class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'firstname', 'middle', 'lastname', 'address1', 'address2', 'city', 'state', 'zipcode', 'email', 'homephone', 'cell', 'dobday']	

class Office(models.Model):
	officename = models.CharField(max_length = 200)
	officecode = models.CharField(max_length = 200)
	attribution = models.CharField(max_length = 200)

class Officer(models.Model):
	subscriberID = models.IntegerField()
	officecode = models.CharField(max_length = 200)
	startdate = models.DateField()
	enddate = models.DateField()

class Service(models.Model):
	servicecode = models.CharField(max_length = 200)
	servicename = models.CharField(max_length = 200)
	description = models.TextField()
	premium = models.CharField(max_length = 200)
	allocation = models.CharField(max_length = 200)

class Organization(models.Model):
	orgcode = models.CharField(max_length = 200)
	orgname = models.CharField(max_length = 200)
	description = models.TextField()
	datejoined = models.DateField()
	address1 = models.TextField()
	address2 = models.TextField()
	city = models.TextField()
	state = models.TextField()
	zipcode = models.TextField()
	phonenumber = models.TextField()

class OrganizationMember(models.Model):
	orgcode = models.CharField(max_length = 200)
	subscriberID  = models.IntegerField()
	membershipstartdate  = models.DateField()
	membershipenddate = models.DateField()
	nativecountry = models.CharField(max_length = 200)
	citizenship = models.CharField(max_length = 200)
	isdelegate = models.BooleanField(max_length = 200)

class Subscriber(models.Model):
	subscriberID = models.IntegerField()
	servicecode = models.CharField(max_length = 200)
	subscriptionrequestdate = models.DateField()
	subscriptionstartdate = models.DateField()
	subscriptionenddate = models.DateField()
	motifofcancellation = models.CharField(max_length = 200)
	subscriptiontype  = models.CharField(max_length = 200)
	username = models.CharField(max_length = 200)
	beneficiaryID = models.IntegerField()

class SubscriptionType(models.Model):	
	subscriptiontypecode = models.CharField(max_length = 200)
	subscriptiontypename = models.CharField(max_length = 200)

class Fee(models.Model):	
	feeID = models.IntegerField()
	feename = models.CharField(max_length = 200)
	servicecode = models.CharField(max_length = 200)
	amount = models.DecimalField(max_digits = 10, decimal_places = 5)

class Event(models.Model):	
	eventID = models.IntegerField()
	servicecode = models.CharField(max_length = 200)
	occurdate = models.DateField()
	subscriberaffected = models.CharField(max_length = 200)
	submittedby  = models.IntegerField()
	submitdate = models.DateField()
	typeOf = models.CharField(max_length = 200)
	approved = models.BooleanField()
	decisiondate = models.DateField()
	decisionstatement = models.TextField()

class Payment(models.Model):	
	paymentID = models.IntegerField()
	contributionID = models.IntegerField()
	amountreceived = models.DecimalField(max_digits = 10, decimal_places = 5)
	receiveddate = models.DateField()
	paymentmethod = models.CharField(max_length = 200)


class Contribution(models.Model):	
	typeOf  = models.CharField(max_length = 200)
	subID = models.IntegerField()
	amount = models.DecimalField(max_digits = 10, decimal_places = 5)
	duedate = models.DateField()
	frequency = models.CharField(max_length = 200)