import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from main.forms import RegistrationForm
from main.models import Candidates
import logging

from main.serializers import CandidateSerializer

logger = logging.getLogger('django')


def index(request):
    return render(request, 'main/index.html', {})


class Registration(CreateView):
    model = Candidates
    form_class = RegistrationForm
    template_name = 'main/index.html'
    success_url = '/'

    def form_valid(self, form):
        return super(Registration, self).form_valid(form)


# ViewSets define the view behavior.
class CandidatesViewSet(viewsets.ModelViewSet):
    queryset = Candidates.objects.all()
    serializer_class = CandidateSerializer

    def list(self, request, pk=None):
        x_admin = request.META['HTTP_X_ADMIN']
        if x_admin != "1":
            return Response({"error": "UNAUTHORIZED"}, status=status.HTTP_401_UNAUTHORIZED)

        if pk is None:
            candidates = Candidates.objects.all().values('full_name', 'dob', 'years_of_experience', 'department',
                                                         'resume').order_by('-create_date')
            logger.info(candidates)
            candidates_list = CandidateSerializer(candidates, many=True)
            return Response(candidates_list.data, status=status.HTTP_200_OK)
        else:
            logger.info('----------------------')
            candidate = Candidates.objects.filter(id=pk).first()
            candidate = CandidateSerializer(candidate)
            resume = candidate.resume.path
            file_pointer = open(resume, "r")
            logger.info('*********************************')
            logger.info(f'******************{file_pointer}***************')
            response = HttpResponse(file_pointer, content_type='application/msword')
            response['Content-Disposition'] = 'attachment; filename=NameOfFile'
            return response

    def retrieve(self, request, *args, **kwargs):
        candidate = Candidates.objects.filter(id=kwargs['pk']).values('full_name', 'resume').first()
        full_name = candidate['full_name']
        resume = candidate['resume']
        logger.info(f'resume {resume}')
        with open(resume, 'rb') as f:
            contents = f.read()
        response = HttpResponse(contents, content_type='application/octet-stream')
        name = f'resume-{full_name}'
        response['Content-Disposition'] = f'attachment; filename={name}'
        return response
