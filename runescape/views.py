from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.


def get_runescape_data(request, player_name):
    url = f'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={player_name}'
    response = requests.get(url)

    if response.status_code == 200:
        try:
            # split response text by newlines
            lines = response.text.splitlines()

            # parse each line and handle the missing or incomplete data
            data = []
            for line in lines:
                skill_data = line.split(',')

                # ensure we have at least 3 items (rank, level, experience)
                if len(skill_data) >= 3:
                    # append parsed data to our list
                    data.append({
                        "rank": skill_data[0],
                        "level": skill_data[1],
                        "experience": skill_data[2],
                    })
                else:
                    # handles cases with missing values by marking as "N/A"
                    data.append({
                        "rank": skill_data[0] if len(skill_data) > 0 else "N/A",
                        "level": skill_data[1] if len(skill_data) > 1 else "N/A",
                        "experience": skill_data[2] if len(skill_data) > 2 else "N/A",
                    })
            return JsonResponse({"player": player_name, "data": data})

        except IndexError:
            # handle any unexpected data issues
            return JsonResponse({"error": "Data parsing error"}, status=500)

    else:
        return JsonResponse({"error": "unable to retrieve data"}, status=400)