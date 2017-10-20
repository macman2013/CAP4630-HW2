from constraint import *
'''
FINISHED
The car with the YGA-441 plates was fined 25 dollars more than the vehicle from Hawaii
'''
def hint1(fine1, fine2, state, license_plate):
    if(license_plate == "YGA-441" and state == "Hawaii"):
        if(fine1 - fine2 != 25):
            return False
    elif(state == "Hawaii" and license_plate == "YGA-441"):
        if(fine2 - fine1 != 25):
            return False
    return True

'''
FINISHED
The Fierro was fined somewhat less than the automobile with GGZ-007
'''
def hint2(car, license_plate, fine):
    #The Fierro is not the car with license GGZ-007
    if(car == "Fierro" and license_plate == "GGZ-007"):
        return False
    #GGZ-007 cannot be lowest fined
    if(license_plate == "GGZ-007" and fine == 25):
        return False
    #The Fierro is not the highest fined
    if(car == "Fierro" and fine == 100):
        return False
    return True

'''
The car that went to Rainbow Reef, license_plate Yang's car, and the Samantha are three different cars
'''
def hint3(car, state, license_plate):
    #They are all mutually exlusive
    if(car == "Samantha" and (state == "Rainbow Reef" or license_plate == "Yang")):
        return False
    if(state == "Rainbow Reef" and (car == "Samantha" or license_plate == "Yang")):
        return False
    if(license_plate == "Yang" and (car == "Samantha" or state == "Rainbow Reef")):
        return False
    return True


'''
FINSHED
The vehicle that received the $50 fine, the Grandero, and the Injitsu are three different cars
'''
def hint4(car, fine, car2):
    #They are all mutually exlusive
    if(car == "Injitsu" and (fine == 50 or car2 == "Grandero")):
        return False
    if(fine == 50 and (car == "Injitsu" or car2 == "Grandero")):
        return False
    if(car2 == "Grandero" and (car == "Injitsu" or fine == 50)):
        return False
    return True

'''
The vessel that saw 5 fines didn't go to Arno's Spit
'''
def hint5(state, fine):
    #Ella's plane when 10 feet further than black plane so Ella's is pink
    if(fine == 5 and state == "Arno's Spit"):
        return False
    return True

'''
FINISHED
The Grandero was fined somewhat more than the car with the FRZ-192 plates
'''
def hint6(car, fine, license_plate):
    #Grandero does not have the FRZ-192 plates
    if(car == "Grandero" and license_plate == "FRZ-192"):
        return False
    #FRZ-192 plates cannot be fined the most
    if(license_plate == "FRZ-192" and fine == 100):
        return False
    #Grandero cannot be fined the least
    if(car == "Grandero" and fine == 25):
        return False
    return True

'''
FINISHED
The vehicle that received the $100 fine doesn't have the GGZ-007 plates
'''
def hint7(license_plate, fine):
    # $100 fine does not have the GGZ-007 plates
    if(fine == 100 and license_plate == "GGZ-007"):
        return False
    return True

'''
Prints final set of answers for the CSP
'''
def answer_set(x):
    Cavalo = []
    Fierro = []
    Grandero = []
    Injitsu = []
    answer_list = [Cavalo, Fierro, Grandero, Injitsu]
    for a in x:
        if a[-1] == "0":
            Cavalo.append(x[a])
        if a[-1] == "1":
            Fierro.append(x[a])
        if a[-1] == "2":
            Grandero.append(x[a])
        if a[-1] in "3":
            Injitsu.append(x[a])
    for car in answer_list:
        print car

def main():

    problem = Problem()
    cars = ["Cavalo", "Fierro", "Grandero", "Injitsu"]
    license_plates = ["FRZ-192", "GGZ-007", "MRT-628", "YGA-441"]
    states = ["Alaska", "Colorado", "Hawaii", "Louisiana"]
    fines = [25, 50, 75 ,100]

    for i in range(len(cars)):
        problem.addVariable("cars" + str(i), cars)
        problem.addVariable("license_plates" + str(i), license_plates)
        problem.addVariable("states" + str(i), states)
        problem.addVariable("fines" + str(i), fines)


    problem.addConstraint(AllDifferentConstraint())
    #cars is now the identifier
    problem.addConstraint(lambda a, b, c, d: a == "Cavalo" and b == "Fierro" and c == "Grandero" and d == "Injitsu", ("cars0", "cars1", "cars2", "cars3"))

    #change for new problem all below
    for i in range(len(cars)):
        problem.addConstraint(FunctionConstraint(hint1), ["cars" + str(i), "states" + str(i), "license_plates" + str(i)])
        problem.addConstraint(FunctionConstraint(hint2), ["cars" + str(i), "states" + str(i), "fines" + str(i), "fines3"])
        problem.addConstraint(FunctionConstraint(hint3), ["cars" + str(i), "states" + str(i), "license_plates" + str(i)])
        for j in range(len(cars)):
            problem.addConstraint(FunctionConstraint(hint4), ["states" + str(i), "states" + str(j), "fines" + str(i), "fines" + str(j)])
        problem.addConstraint(FunctionConstraint(hint5), ["states" + str(i), "fines" + str(i)])
        problem.addConstraint(FunctionConstraint(hint6), ["cars" + str(i), "fines" + str(i), "license_plates" + str(i)])
        #We know Fierro subset ends in 1
        problem.addConstraint(FunctionConstraint(hint7), ["cars" + str(i), "states" + str(i), "fines" + str(i), "license_plates" + str(i), "cars1", "fines1", "license_plates1"])

    print "Number of Solutions: ", len(problem.getSolutions())
    for answer in problem.getSolutions():
        answer_set(answer)


if (__name__ == "__main__"):
    main()