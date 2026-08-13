import math
def minimum_distance(p1,p2):
    return math.sqrt( (p1['X'] - p2['X']) ** 2 + (p1['Y'] - p2['Y']) ** 2)
def rajknnclassifier(k=3):
    border = "*" * 60

    data = [
        {'Point' : 'A' , 'X' : 1 , 'Y' : 2 , 'Label' : 'Red'} ,
        {'Point' : 'B' , 'X' : 2 , 'Y' : 3 , 'Label' : 'Red'} ,
        {'Point' : 'C' , 'X' : 3 , 'Y' : 1 , 'Label' : 'Blue'} ,
        {'Point' : 'D' , 'X' : 6 , 'Y' : 5 , 'Label' : 'Blue'} ,
    ]

    print(border)
    print("Raj's KNN Classifier:")
    print(border)
    
    print("Training data : ")
    for i in data:
        print(i)

    print(border)

    print(border)
    print("Raj's KNN Classifier: Enter the new points/coordinates")
    print(border)

    x = int(input("Enter X Coordinate : "))
    y = int(input("Enter Y Coordinate : "))

    new_point = {'X':x , 'Y':y}

    print(border)

    for i in data:
        i['Distance'] = minimum_distance(i,new_point)

    sorted_data = sorted(data,key=lambda item : item["Distance"])
    print("Sorted Data: ")
    print(border)
    for i in sorted_data:
        print(i)
    print(border)

    nearest = sorted_data[:k] #data slicing only top 3 nearest are selected 
        
    print("Nearest 3 members are : ")
    print(border)
    for i in nearest:
        print(i)

    #voting 
    votes = {}

    for i in nearest:
        Label = i['Label']
        votes[Label] = votes.get(Label,0)+1

    imax = 0 
    name = ""
    for d in votes:
        if (votes[d]>imax):
            imax = votes[d]
            name = d

    print(border)
    print("Final predictions is :",name)

    print(border)
    

def main():
    rajknnclassifier()

if __name__ == "__main__":
    main()
