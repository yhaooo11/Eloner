

import requests 
import json


header = { 'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAF1tOgEAAAAA25hxqrkARehLPHKc2a2G83ZOgHQ%3Da1nxk2LJNzjf4pIeERsPsK7lW2RnXf2rvQ8bMn4EiDKftPc4M7'}


url = []


def getTweetsBTC():
    url.clear()
    r = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=elonmusk&count=2000", headers=header)
    rjson = json.loads(r.content)
    total = 0

    for x in range(len(rjson)):
        if "bitcoin" in rjson[x]['text'].lower():
            total += 1
            url.append(f"https://twitter.com/elonmusk/status/{rjson[x]['id_str']}")
           
    return total

def getTweetsBTCEmbedded():
    html = []
    for x in range(len(url)):
        re = requests.get(f"https://publish.twitter.com/oembed?url={url[x]}")
        rejson = json.loads(re.content)
        html.append(rejson['html'])
        
    return html

def getTweetsDOGE():
    url.clear()
    r = requests.get("https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=elonmusk&count=2000", headers=header)
    rjson = json.loads(r.content)
    total = 0

    for x in range(len(rjson)):
        if "doge" in rjson[x]['text'].lower() or "dogecoin" in rjson[x]['text'].lower():
            total += 1
            url.append(f"https://twitter.com/elonmusk/status/{rjson[x]['id_str']}")
           
    return total

def getTweetsDOGEEmbedded():
    html = []
    for x in range(len(url)):
        re = requests.get(f"https://publish.twitter.com/oembed?url={url[x]}")
        rejson = json.loads(re.content)
        html.append(rejson['html'])
        
    return html



    









