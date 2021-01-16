import numpy as np
from model import generate_recommendations

client_id = 10
already_rated = [293, 294, 1000000]
k = 5
m_dir = '/home/parth27/bizzbytes/tensorflow-recommendation-wals/wals_ml_engine/jobs/wals_ml_local_20210116_103341/model'
user_map = np.load(m_dir+"/user.npy")
item_map = np.load(m_dir+"/item.npy")
row_factor = np.load(m_dir+"/row.npy")
col_factor = np.load(m_dir+"/col.npy")
user_idx = np.searchsorted(user_map, client_id)
user_rated = [np.searchsorted(item_map, i) for i in already_rated]

print(len(item_map))

recommendations = generate_recommendations(942, user_rated, row_factor, col_factor, k)

article_recommendations = [item_map[i] for i in recommendations]

print(article_recommendations)