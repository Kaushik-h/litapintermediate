from rest_framework import serializers
from Profile.models import Tribe,KYC,Bio
from Auth.models import User
from Auth.serializers import UserNameSerializer

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields=['userId','username','firstName','middleName',
                'lastName','isTribeLeader','isModerator',
                'primaryPhone','primaryEmail','kyc','followers']

class TribeSerializer(serializers.ModelSerializer):
    tribeLeader = UserNameSerializer()
    class Meta:
        model = Tribe
        fields='__all__'

class KYCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYC
        fields='__all__'

class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        fields='__all__'