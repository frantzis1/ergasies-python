import random

def fibonacci(n):

    # Taking 1st two fibonacci nubers as 0 and 1
    f = [0, 1]


    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
def check_for_prime(p,tests):
	cnt=1
	while cnt<tests:
		a=random.randrange(1,p)
		if pow(a, p,p)==a:
			cnt+=1
		else:
		
			break
	if cnt==tests:
		return True
	else:
		return False

k=input()
n=int(k)
print(fibonacci(n))

ceck=fibonacci(n)
if n > 4:
 einai=check_for_prime(ceck,20)
 if einai:
       print("EINAI PRWTOS")
 else:
     print("den einai prwtos")
else:
    if n == 0:
      print("den einai prwtoss")
    else:
         print("einai prwtos")
