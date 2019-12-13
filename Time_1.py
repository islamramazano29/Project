import pandas as pd
df  = pd.read_csv('equity_value_data.csv')
time = df['timestamp']
user = df['user_id']
count_1 = 0
count_users = []
for i in range(len(user)-2):
    if user[i] == user[i+1]:
        count_1+=1
    else:
        count_users.append((count_1, user[i]))
        count_1 = 0

#print(count_users)

count_users_1 = [i[0] for i in count_users]
print(max(count_users_1))
a = count_users_1.index(max(count_users_1))
print(user[a])

time_android=0
time_ios = 0
df_2 = pd.read_csv('features_data_with_normalization.csv')
platform = df_2['platform']
for i in range(0,len(count_users_1)):
    k = count_users[i][1]
    ind = user.index(k)
    if platform[ind] == 1:
        time_android+=count_users[i][0]
    if platform[ind] == -1:
        time_ios+=count_users[i][0]

print(time_ios/time_android)

