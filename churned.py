with open('equity_value_data.csv', 'r') as f:
    users = f.read()
churned = []
days  = 0
lines = users.split('\n')
lines = lines[1:-1]
old_user_id = None
current_churned = None

count_users = 0

for line in lines:
    data_list = line.split(',')
    close_equity = float(data_list[1])
    user_id = data_list[2]

    if old_user_id != user_id:
        days = 0
        count_users += 1
    else:
        if user_id == current_churned:
            continue

    old_user_id = user_id

    if close_equity < 100:
        days += 1
    if days >= 28:
        churned.append(user_id)
        current_churned = user_id
        days = 0


# print(churned)
# print(len(churned))
# print(count_users)
# print(len(churned) / count_users * 100)


import pandas as pd
import  numpy as np
plus_minus = []
features_data = pd.read_csv('features_data.csv')
data = features_data["user_id"]
# print(data)
for i in data:
    if i in churned:
        plus_minus.append(1)
    else:
        plus_minus.append(0)
#print(plus_minus)

features_data['churned'] = plus_minus
features_data.to_csv('features_data_with_churned')


