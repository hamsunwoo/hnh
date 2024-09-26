import requests
import json

#def get_api():
#    headers = {
#            'accept': 'application/json',
#            }
#    files = {'file': (f'{file_path}', open(f'{file_path}', 'rb'), 'image/png'),}
#    response = requests.post('http://localhost:8000/uploadfile/', headers=headers, files=files)

    # print(response.text)
    # {"Hello":[{"label":"hot dog","score":0.5382884740829468},
    # {"label":"not hot dog","score":0.4617115557193756}]}
#    r = json.loads(response.text)
#    data = r["Hello"]
    # print(data)
    # [{'label': 'hot dog', 'score': 0.5382884740829468},
    # {'label': 'not hot dog', 'score': 0.4617115557193756}]
#    return data

def get_max_label(p):
    max_score = 0
    max_label = ""
    #data = get_api()
    for i in p:
        if i['score'] > max_score:
            max_score = i['score']
            max_label = i['label']
    return max_label

def get_max_score(p):
    max_score = 0
    max_label = ""
    #data = get_api()
    for i in p:
        if i['score'] > max_score:
            max_score = i['score']
            max_label = i['label']
    return max_score

def get_label(p):
    win_label = get_max_label(p)
    win_score = get_max_score(p)
    
    if win_label == "hot dog" and win_score >= 0.8:
        last_label = "hot dog"
        return {"label" : last_label, "score": win_score}
    else:
        last_label = "not hot dog"
        return {"label": last_label, "score": win_score}

#def get_max_score2():
#    max_p = max(p, key=get_score)
#    return max_p
#
#def get_max_score3():
#    max_p = max(p, key=lambda x: x['score'])
#    print(max_p)
#    return max_p

