from django.contrib import admin

# Register your models here.
from .models import Service, Subscriber, Organization, Office, Officer, SubscriptionType, Fee, Event, Payment 

#admin.site.register(Service)
admin.site.register(Subscriber)
admin.site.register(Organization)


@admin.register(Service)

class ServiceAdmin(admin.ModelAdmin):
	list_display = ['servicecode','servicename','description','allocation']
	search_fields = ['servicename']
	list_filter = ['servicecode']

@admin.register(Office)	

class OfficeAdmin(admin.ModelAdmin):
	list_display = ['officename','officecode','attribution']


@admin.register(Officer)	

class OfficerAdmin(admin.ModelAdmin):
	list_display = ['subscriberID','officecode','startdate','enddate']	

@admin.register(SubscriptionType)
class SubscriptionTypeAdmin(admin.ModelAdmin):	
	list_display = ['subscriptiontypecode','subscriptiontypename']


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):	
	list_display = ['feeID','feename','servicecode','amount']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):	
	list_display = ['eventID','servicecode','occurdate','approved']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):	
	list_display = ['paymentID','contributionID', 'amountreceived', 'receiveddate', 'paymentmethod']
