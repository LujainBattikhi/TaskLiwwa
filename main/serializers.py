from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from main.models import Candidates


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidates
        fields = ['full_name', 'dob', 'years_of_experience', 'department', 'resume']
