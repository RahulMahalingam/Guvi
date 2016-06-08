n=int(input("Enter no."))
for i in range(2,n):
	if((n%i==0) and (i%2!=0)):
		print(i)
		break;
