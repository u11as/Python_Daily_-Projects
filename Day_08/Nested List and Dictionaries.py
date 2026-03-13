capitals={
    "France":"Paris",
    "Germany":"Berlin",
}

# Nested List in Dictionary

#travel_log = {
    #"France":["Paris","Lille","Dijon"],
    #"Germany":["Stuttgart","Berlin"],
#}

#print(travel_log["France"][2])

Nested_list = ['A','B',['C','D']]

print(Nested_list[2][1])

travel_log = {
    "France":{
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits": 11,
     },

    "Germany":{
        "cities_visited":["Stuttgart","Berlin","Hamburg"],
        "total_visits":15,
     },
}

print(travel_log["Germany"]["cities_visited"][2])