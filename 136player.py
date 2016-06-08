arr=[22,33,44,23,56,78]
length=len(arr)
arr.sort();
item=int(input("Enter id to search: "))

for i in range(0,length-1):
   if ( item == arr[i] ):
   	print("Id found in array")
   	break;
   else :
   	print("Idnot found in array")
   	break;
