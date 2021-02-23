from django.shortcuts import render
from .forms import conferenceForm
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from .models import Conference
from .serializers import ConferenceSerializer

# Create your views here.


# def formView(request):
#     form = conferenceForm
#     if request.method == 'POST':
#         form = conferenceForm(request.POST)
#         if form.is_valid():
#             form.save()

#     context = {'form': form}
#     return render(request, 'adminlte/lib/form.html', context)


class ConferenceView(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

