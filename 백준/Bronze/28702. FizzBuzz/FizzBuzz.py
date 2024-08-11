
try:i=int(input())+3
except:pass
try:i=int(input())+2
except:pass
try:i=int(input())+1
except:pass
if i%3==0 and i%5==0:print('FizzBuzz')
elif i%3==0 and i%5!=0:print('Fizz')
elif i%3!=0 and i%5==0:print('Buzz')
else:print(i)