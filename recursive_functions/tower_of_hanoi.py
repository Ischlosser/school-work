
def towerOfHan(n , source, destination, auxiliary):
    if n==1:
        print ("Move cirlce 1 from source",source,"to destination",destination)
        return
    towerOfHan(n-1, source, auxiliary, destination)
    print ("Move cirlce",n,"from source",source,"to destination",destination)
    towerOfHan(n-1, auxiliary, destination, source)

n = 3
towerOfHan(n,'A','B','C') 
