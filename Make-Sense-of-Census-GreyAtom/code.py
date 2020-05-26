# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(path)
print(data)
print(type(data))
#Code starts here
print(np.shape(data))
#age
age=data[:,0]
##print(age)
max_age=max(age)
min_age=min(age)
age_mean=np.mean(age).round(2)
age_std=np.std(age).round(2)
print(max_age,min_age,age_mean,age_std)
race=data[:,2]
race_0=race[race==0]
race_1=race[race==1]
race_2=race[race==2]
race_3=race[race==3]
race_4=race[race==4]
len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
lens=[len_0,len_1,len_2,len_3,len_4]
min_len=min(lens)
for i in range(len(lens)):
    if min_len==lens[i]:
        minority_race=i
print(minority_race)

senior_citizens = data[age>60]
senior_citizens_len=len(senior_citizens)
working_hours_sum=sum(senior_citizens[:,6])
avg_working_hours=(working_hours_sum/senior_citizens_len).round(2)
print(working_hours_sum)
print(avg_working_hours)

high=data[data[:,1]>10]
low=data[data[:,1]<=10]
avg_pay_high=np.mean(high[:,7]).round(2)
avg_pay_low=np.mean(low[:,7]).round(2)
print(avg_pay_high,avg_pay_low)






