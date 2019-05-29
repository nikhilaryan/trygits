
def last(n):
    return n[-1]
 
def sorti(tuples):
     tuples.sort(key=last)

a=[]
end =0
while(end==0):
	istring = input("enter values")
	tup = tuple(int(x) for x in istring.split(","))
	a.append(tup)
	sorti(a)
	print(a)
