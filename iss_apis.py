### Query International Space Station from NASA

import requests
import json
from datetime import datetime

def json_print(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def iss_query_no_param():
    #response = requests.get("http://api.open-notify.org/this-api-doesnt-exist")
    #print(response.status_code)
    response = requests.get("http://api.open-notify.org/astros.json")
    #print(response.json())
    #print(response.status_code)
    json_print(response.json())


parameters = {
    "lat": 37.4341632,
    "lon": -121.900236
}

def get_pass_times(obj):
    pass_times = obj.json()['response']
    print(pass_times)
    rise_times = []
    for d in pass_times:
        time = d['risetime']
        rise_times.append(time)
    times = []
    for rt in rise_times:
        time = datetime.fromtimestamp(rt)
        times.append(time)
        print(time)


def iss_query_with_param():
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    json_print(response.json())
    get_pass_times(response)

def iss_query():
    iss_query_no_param()
    iss_query_with_param()