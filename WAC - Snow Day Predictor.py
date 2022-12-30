#PROBLEM START

#This problem was featured from DMOJ's Wesley Anger Contest 3 and has been transferred to this site. If there are any concerns regarding a specific problem's time limit, please contact the administrators.

#Being fed up with online snow day predictors and their inaccurate results, you have decided to take matters into your own hands and write your own snow day predictor.

#You are given the temperature T (in Celsius), the total amount of snowfall D (in centimetres), and the probability of freezing rain P (as a percentage).

#A snow day will only occur if at least two of the following conditions are satisfied:

#The temperature is strictly colder than -40 degrees Celsius.
#There is 15cm of snow or more on the ground.
#The risk of freezing rain is strictly more than 50%.
#Please determine whether the given weather information will cause a snow day. If there is a snow day, output YES. Otherwise, output NO.

#Constraints
#For this problem, you will be required to pass all the samples in order to receive any points.

#−100≤T≤100
#0≤D≤100
#0≤P≤100

#Input Specification
#The first and only line will contain 3 integers T, D, and P, representing the temperature, the snowfall, and the risk of freezing rain.

#Output Specification
#Output one line only. If there is a snow day, output YES. Otherwise, output NO.

#PROBLEM END

split_text = input().split(" ")
temp = int(split_text[0])
snow = int(split_text[1])
rain = int(split_text[2])
if ((temp < -40) and (15 <= snow)):
  print("YES")
elif ((temp < -40) and (50 < rain)):
  print("YES")
elif ((50 < rain) and (15 <= snow)):
  print("YES")
else:
  print("NO")
