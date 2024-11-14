from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.


def get_runescape_data(request, player_name):
    url = f'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={player_name}'

    # make a get request for player data
    try:
        response = requests.get(url)
        response.raise_for_status()

    # split the CSV data into rows
        data = response.text.strip().split('\n')

    # put data into a dictionary
        stats = {}
        for line in data:
            skill_data = line.split(',')
            skill_name = skill_data[0]
            rank = skill_data[1]
            level = skill_data[2]
            experience = skill_data[3] if len(skill_data) > 3 else None

            stats[skill_name] = {
                'rank': rank,
                'level': level,
                'experience': experience
        }
    
    # return the data as a JSON response
        return JsonResponse(stats)
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)