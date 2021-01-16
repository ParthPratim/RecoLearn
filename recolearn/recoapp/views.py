from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

model = __import__('tensorflow-recommendation-wals.wals_ml_engine.trainer.model', globals(), locals(), [], 0)

def recommend(user_id):

    #already_rated =[ int(x) for x in load_database()['ALREADY_RATED'] ]
    already_rated = []
    k = 8
    m_dir = './tensorflow-recommendation-wals/wals_ml_engine/jobs/wals_ml_local_20210116_103341/model'
    #user_map = np.load(m_dir+"/user.npy")
    item_map = np.load(m_dir+"/item.npy")
    row_factor = np.load(m_dir+"/row.npy")
    col_factor = np.load(m_dir+"/col.npy")

    #user_idx = np.searchsorted(user_map, client_id)

    user_rated = [np.searchsorted(item_map, i) for i in already_rated]

    #print(len(item_map))

    recommendations = model.wals_ml_engine.trainer.model.generate_recommendations(user_id, already_rated, row_factor, col_factor, k)

    article_recommendations = [item_map[i] for i in recommendations]

    with open("recoapp/u.item") as f:
        content = f.readlines()
    names = []
    for ar in article_recommendations:
        names.append(content[int(ar)].strip().split('|')[1])
    return names


def index(request):    
    #model.wals_ml_engine.trainer.model.generate_recommendations()
    user_id = int(request.GET['user_id'])
    if user_id < 1 or user_id > 942 :
        return HttpResponse("user_id should be in rannge 1-942")
    context = {
        "data" : recommend(user_id),
        "user_id" : user_id
    }
    return render(request, 'modern.html', context=context)
