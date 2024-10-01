from django.shortcuts import render
from django.conf import settings



# Create your views here.




def home(request):
    import json
    import requests
    context = {
        "api_key": settings.NINJA_API_KEY,
        #"gov_key": settings.GOV_API_KEY
    }


    if request.method == 'POST':

        query = request.POST['query']
        ninja_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        #gov_url = 'https://developer.nrel.gov/api/alt-fuel-stations/v1.json?limit=1&api_key=' 
        response = requests.get(ninja_url, headers={'X-Api-Key': context["api_key"]})
        try:
            api = json.loads(response.content)
           
        except Exception as e:
            api = "There was an error"
        return render(request, 'home.html', {'api': api})
    if request.method == 'WEIGHT':
        return render(request, 'home.html', {'weight': 0})
    else:
        return render(request, 'home.html', {'query': 'Enter a food'})

   
