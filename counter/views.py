from django.shortcuts import render
from django.conf import settings



# Create your views here.




def home(request):
    import json
    import requests
    context = {
        "api_key": settings.NINJA_API_KEY
    }


    if request.method == 'POST':

        #load = open(config.json)
        #json_contents = json.load(load)
        #ninja_api = json_contents['ninjaApiKey']

        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
        response = requests.get(api_url, headers={'X-Api-Key': context["api_key"]})
        try:
            api = json.loads(response.content)
           
        except Exception as e:
            api = "There was an error"
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a food'})



