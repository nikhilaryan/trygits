def bfs(arr,l,r,curr):
	while(l<=r):
		mid=int((l+r)/2)
		if arr[mid]==curr:
			return mid
		elif arr[mid]<curr:
			l=mid+1
		else:
			r=mid-1
	return -1

ar=[1,2,3,4,5,6]
index=bfs(ar,0,(len(ar)-1),9)
if(index!=-1):
	print(index+1)
else:
	print("Element not found")
