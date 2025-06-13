import requests
import json


class JewelerAPI:
    def __init__(self):
        self.base_url = 'https://www.naj.co.uk/'

    def get_stores(self, radius=800, location="Birmingham, UK"):
        search_criteria = {"SearchUnits": "m", "InclusiveSearch": False, "SearchRadius": radius,
                           "NoSearchAnalytics": False, "Location": location,
                           "Position": {"south": 52.38599896742283, "west": -2.017433632448159,
                                        "north": 52.60869933491674, "east": -1.709829372653529},
                           "Filters": {"Target Clientelle": "Consumer", "Member Category": "Designer craftsperson"},
                           "Keyword": "", "Count": 100}

        response = requests.get(
            url=f'{self.base_url}api/flexmap/5be3f45a-39b8-409d-bb17-7714f79cc5d1/search',
            params={'searchCriteria': json.dumps(search_criteria)},
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
                'Accept': 'application/json, text/plain, */*',
            }
        )
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Error fetching stores with code {response.status_code} and message {response.text}")
