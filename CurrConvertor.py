print("WELCOME TO THE CURRENCY CONVERTER!!")
print("--------------------------------------------")
print("Please use the following codes for respective countries currencies:")
print("----------------------------------------------------------------------------------------")

d1={"Indian ruppees":"INR","United Kingdom Pounds":"Pounds","German Euros":"Euros","United Stated Dollors":"USD","Canadian Dollors":"CAD","Chinese Yuan":"Yuan","Russian Ruble":"Ruble"}


print(d1)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
curr=str(input("ENter currency which you need to convert: "))
print("----------------------------------------------------------------------------------------")
ans=str(input("Enter currency to which you want to convert:"))
print("----------------------------------------------------------------------------------------")
amt=float(input("Enter amount to be converted:"))
print("----------------------------------------------------------------------------------------")

if curr=="INR" and ans=="Pounds":
    result=(amt)/96.92
elif curr=="Pounds" and ans=="INR":
    result=(amt)*96.92
elif curr=="INR" and ans=="Euros":
    result=(amt)/84.34
elif curr=="Euros" and ans=="INR":
    result=(amt)*84.34
elif curr=="USD" and ans=="INR":
    result=(amt)*81.52
elif curr=="INR" and ans=='USD':
    result=(amt)/81.52
elif curr=="CAD" and ans=="INR":
    result=(amt)*60.77
elif curr=="INR" and ans=="CAD":
    result=(amt)/60.77
elif curr=="INR" and ans=="Yuan":
    result=(amt)/11.45
elif curr=="Yuan" and ans=="INR":
    result=(amt)*11.45
elif curr=="Ruble" and ans=="INR":
    result=(amt)*1.34
elif curr=="INR" and ans=="Ruble":
    result=(amt)/1.34
else:
    print("Oops sorry!! Something went Wrong..")

print("Conversion of {} from {} to {} is: {}".format(amt,curr,ans,result))
