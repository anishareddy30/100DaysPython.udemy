capitals = {
    "france" : "paris",
    "germany" : "berlin",
    }

#nested list in dictionary 

travel_log = {
    "france" : ["paris" , "lille" ,"dijon"],
    "germany" : ["berlin" , "hamburg" ],
}

#print lilllie
print(travel_log["france"][1])

#list inside list
nested_list = ["a" , "b" , ["c" , "d"]]

#print d
print(nested_list[2][1])

#list which is nested inside dictionary ... which is nested inside another dictionary
travel_log = {
    "france" : {
        "num_times_visited" : 12 ,
        "cities_visited" : ["paris" , "lillie" , "dijon"]
},
    "germany" : {
        "num_of_times_visited" : 5,
        "cities_visited" : ["berlin" , "hamburg"]
    },
}

print(travel_log["germany"]["cities_visited"][1])