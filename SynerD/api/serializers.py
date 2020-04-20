from rest_framework import serializers
from ..models import Service
from ..models import Subscriber
from ..models import Organization
class ServiceSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Service
		fields = ['servicecode', 'servicename', 'description', 'premium', 'allocation']


class SubscriberSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Subscriber
		fields = ['subscriberID', 'servicecode', 'subscriptionrequestdate', 'subscriptionstartdate', 'subscriptionenddate', 'motifofcancellation', 'subscriptiontype', 'username', 'beneficiaryID']


class OrganizationSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Organization
		fields = ['orgcode', 'orgname', 'description', 'datejoined', 'address1', 'address2', 'city', 'state', 'zipcode', 'phonenumber']
