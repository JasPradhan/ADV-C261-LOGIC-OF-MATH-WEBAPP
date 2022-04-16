import requests

print("Enter your input : ")

equation=input()

result='https://newton.now.sh/api/v2//simplify/'+equation

data=requests.get(result).json()

print("\nOperation for given equation : ",data['operation'])

print("\nExpression for given equation : ",data['expression'])
 
print("\nResult of given equation : ",data['result'])