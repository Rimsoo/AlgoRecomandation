
from cmath import sqrt
import json
from math import sqrt, pow

def euclidian(p1, p2):
    return sqrt(pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1], 2))

def normalized_result(p1, p2):
    return 1/(1 + euclidian(p1, p2))

def pearson(rd1, rd2): 
    d1 = {}
    d2 = {}
    if (rd1.keys() != rd2.keys()):
        for k in rd1.keys() & rd2.keys():
            d1[k] = rd1[k]
            d2[k] = rd2[k]

    d1 = dict(sorted(d1.items()))
    d2 = dict(sorted(d2.items()))

    x = list(d1.values())
    y = list(d2.values())

    XxY = [a*b for a,b in zip(x,y)]
    x2 = [a**2 for a in x ]
    y2 = [a**2 for a in y ]
    n = len(x)
    
    return (n * sum(XxY) - sum(x) * sum(y)) / (sqrt((n * sum(x2) - sum(x)**2 ) * (n * sum(y2) - sum(y)**2 ) ))

def recomandation(data, for_who):
    p1 = for_who
    d1 = data[p1]

    recommendation = {}

    for p2, d2 in data.items():
        if(p2 == p1):
            continue

        recommendation[p2] = {}
        recommendation[p2]["sim"] = pearson(d1,d2)
        
        for k, v in d2.items():
            if(k in d1):
                recommendation[p2][k] = -1
            else:
                recommendation[p2][k] = v
                recommendation[p2]["sim."+k] = v*recommendation[p2]["sim"]
    
    return recommendation

def main():
	#Read JSON data into the datastore variable
    with open("data.json", 'r') as f:
        data = json.load(f)

    print(recomandation(data, "Toby"))

    #print (pearson(data["Lisa Rose"], data["Gene Seymour"]))

    # film1 = "You, Me and Dupree"
    # film2 = "Snakes on a Plane"
    #Use the new datastore datastructure
    # print (normalized_result(
    #         (data[p1][film1], data[p1][film2]), 
    #         (data[p2][film1], data[p2][film2])))
    


if __name__ == "__main__":
    main()
