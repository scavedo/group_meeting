from django.shortcuts import render

# Create your views here.
def index(request):
        # now return the rendered template
        return render(request, 'meeting/index.html')
