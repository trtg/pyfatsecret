from fatsecret import * 
import matplotlib.pyplot as plt #for plotting weights
from datetime import *
from pandas import *
#-----------------------------------
#get your consumer key and secret after registering 
#as a developer here: http://platform.fatsecret.com/api/ 
consumer_key='your_key_goes_here'
consumer_secret='your_secret_goes_here'

fs=Fatsecret(consumer_key,consumer_secret)
saved_meals=fs.saved_meals_get()
print saved_meals
#for now, search expressions cannot contain spaces
result=fs.foods_search("Betty")
print result

#retrieve fat,protein,carbs, and calories for the last 3 months
two_months_ago=fs.food_entries_get_month(datetime.now()-timedelta(weeks=8))
last_month=fs.food_entries_get_month(datetime.now()-timedelta(weeks=4))
this_month=fs.food_entries_get_month()

rdates = [datetime.fromtimestamp(float(i['date_int'])*60*60*24) for i in this_month]
fats = [i['fat'] for i in this_month] 
proteins = [i['protein'] for i in this_month] 
carbs = [i['carbohydrate'] for i in this_month] 
calories = DataFrame({'calories' : Series([i['calories'] for i in this_month],index=rdates)})

d={'fat':Series(fats,index=rdates),
        'carb':Series(carbs,index=rdates),
        'protein':Series(proteins,index=rdates)}
df = DataFrame(d)
fig,axes = plt.subplots(2,1)
df.plot(ax=axes[0],style='-o',sharex=True)
calories.plot(ax=axes[1],style='-o',sharex=True)
#add some space between subplots to avoid overlapping dates
plt.subplots_adjust(hspace=0.8)
plt.show()
