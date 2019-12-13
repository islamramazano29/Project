import pandas as pd
df  = pd.read_csv('features_data_with_normalization.csv')
churned = df['churned']
platforms = df['platform']
summ_android = 0
summ_ios = 0
for i in range(0,len(churned)):
    if churned[i] == 1 and platforms[i] == 1:
        summ_android+=1
    if churned[i] == 1 and platforms[i] == -1:
        summ_ios+=1

print(summ_android/summ_ios)









