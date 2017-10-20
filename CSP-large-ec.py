from constraint import *
'''
The Daily Ray is either the vessel that went to Rainbow Reef or Captain Romero's Vessel
'''
def hint1(boat, location, captain):
    if(boat == "Daily Ray" and not ((location == "Rainbow Reef") != (captain == "Romero" ))):
        return False
    return True
'''
The vessel that went to Rainbow Reef saw fewer manatees than the Watery Pete
'''
def hint2(boat, location, manatee, WPboat_manatees):
    if(location == "Rainbow Reef"):
        #The watery pete did not go to rainbow reef
        if(boat == "Watery Pete"):
            return False
        #we Know WP is #3
        if(manatee >= WPboat_manatees):
            return False
    return True

'''
The Boat that went to Rainbow Reef, Captain Yang's boat, and the Samantha are three different boats
'''
def hint3(boat, location, captain):
    #They are all mutually exlusive
    if(boat == "Samantha" and (location == "Rainbow Reef" or captain == "Yang")):
        return False
    if(location == "Rainbow Reef" and (boat == "Samantha" or captain == "Yang")):
        return False
    if(captain == "Yang" and (boat == "Samantha" or location == "Rainbow Reef")):
        return False
    return True


'''
The vessel that went to Betty Beach saw 2 more manatees than the boat that went to Rainbow Reef
'''
def hint4(location1, location2, manatee1, manatee2):
    if(location1 == "Betty Beach" and location2 == "Rainbow Reef"):
        if(manatee1 - manatee2 != 2):
            return False
    elif(location1 == "Rainbow Reef" and location2 == "Betty Beach"):
        if(manatee2 - manatee1 != 2):
            return False
    return True

'''
The vessel that saw 5 manatees didn't go to Arno's Spit
'''
def hint5(location, manatee):
    #Ella's plane when 10 feet further than black plane so Ella's is pink
    if(manatee == 5 and location == "Arno's Spit"):
        return False
    return True

'''
The boat that saw 3 manatees is either Captain Yang's boat or the Samantha
'''
def hint6(boat, manatee, captain):
     if(manatee == 3):
         #One or the other
         if((captain == "Yang") != (boat == "Samantha")):
             return True
         return False
     return True

'''
Of the Foxy Roxy and the vessel that went to Betty Beach, one saw 3 manatees and the other was lead by Captain Armstrong
'''
def hint7(boat, location, manatee, captain, FR, manateeFR, CapFR):
    #Foxy Roxy did not go to betty Beach
    if(boat == "Foxy Roxy" and location == "Betty Beach"):
        return False
    #Foxy Roxy has to have at least one of these true in set
    if(not(manateeFR == 3 or CapFR == "Armstrong")):
        return False
    if(location == "Betty Beach"):
        #at least one has to be true
        #since we already passed Foxy Roxy condition and answers are unique just check if it has one
        if(not(manatee == 3 or captain == "Armstrong")):
            return False
    return True

'''
The Samantha went to Betty Beach
'''
def hint8(boat, location):
    if(boat == "Samantha" and location != "Betty Beach"):
        return False
    if(boat != "Samantha" and location == "Betty Beach"):
        return False
    return True

'''
Prints final set of answers for the CSP
'''
def answer_set(x):
    Daily_Ray = []
    Foxy_Roxy = []
    Samantha = []
    Watery_Pete = []
    answer_list = [Daily_Ray, Foxy_Roxy, Samantha, Watery_Pete]
    for a in x:
        if a[-1] == "0":
            Daily_Ray.append(x[a])
        if a[-1] == "1":
            Foxy_Roxy.append(x[a])
        if a[-1] == "2":
            Samantha.append(x[a])
        if a[-1] in "3":
            Watery_Pete.append(x[a])
    for boat in answer_list:
        print boat

def main():

    problem = Problem()
    boats = ["Daily Ray", "Foxy Roxy", "Samantha", "Watery Pete"]
    captains = ["Armstrong", "Jacobson", "Romero", "Yang"]
    locations = ["Arno's Spit", "Betty Beach", "Rainbow Reef", "Trey's Tunnel"]
    manatees = [3, 4, 5 ,6]

    for i in range(len(boats)):
        problem.addVariable("boats" + str(i), boats)
        problem.addVariable("captains" + str(i), captains)
        problem.addVariable("locations" + str(i), locations)
        problem.addVariable("manatees" + str(i), manatees)


    problem.addConstraint(AllDifferentConstraint())
    #boats is now the identifier
    problem.addConstraint(lambda a, b, c, d: a == "Daily Ray" and b == "Foxy Roxy" and c == "Samantha" and d == "Watery Pete", ("boats0", "boats1", "boats2", "boats3"))

    #FIXME: change for new problem all below
    for i in range(len(boats)):
        problem.addConstraint(FunctionConstraint(hint1), ["boats" + str(i), "locations" + str(i), "captains" + str(i)])
        problem.addConstraint(FunctionConstraint(hint2), ["boats" + str(i), "locations" + str(i), "manatees" + str(i), "manatees3"])
        problem.addConstraint(FunctionConstraint(hint3), ["boats" + str(i), "locations" + str(i), "captains" + str(i)])
        for j in range(len(boats)):
            problem.addConstraint(FunctionConstraint(hint4), ["locations" + str(i), "locations" + str(j), "manatees" + str(i), "manatees" + str(j)])
        problem.addConstraint(FunctionConstraint(hint5), ["locations" + str(i), "manatees" + str(i)])
        problem.addConstraint(FunctionConstraint(hint6), ["boats" + str(i), "manatees" + str(i), "captains" + str(i)])
        #We know foxy roxy sub set ends in 1
        problem.addConstraint(FunctionConstraint(hint7), ["boats" + str(i), "locations" + str(i), "manatees" + str(i), "captains" + str(i), "boats1", "manatees1", "captains1"])
        problem.addConstraint(FunctionConstraint(hint8), ["boats" + str(i), "locations" + str(i)])

    print "Number of Solutions: ", len(problem.getSolutions())
    for answer in problem.getSolutions():
        answer_set(answer)


if (__name__ == "__main__"):
    main()