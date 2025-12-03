names = ["Sviatoslav", "Filip", "Anna", "Joseph", "Alfie", "Emily", "Adela", "Matvii", "Xuanbin", "Alexandra", "Ester", "Anastasiia", "Radovan"]
def iterSelectSort(objects):
    for j in range(len(objects)):
        smallest = objects.pop(j)
        
        for i in range(len(objects)-1):
            if objects[i] < smallest:
                smallest = objects[i]
    return