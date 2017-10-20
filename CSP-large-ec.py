# Quizzle 3 Extra Credit - CSP Solution
# Krista Shuckerow and Dale Keith

from constraint import *
'''
FINISHED
The car with the YGA-441 plates was fined 25 dollars more than the vehicle from Hawaii
'''
def hint1(state, license_plate, fine1, fine2):
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
FINISHED
The four cars are the vehicle from Colorado, the Grandero, the Fierro, and the Injitsu
'''
def hint3(state, car1, car2, car3):
    #They are all mutually exlusive
    if(state == "Colorado" and (car1 == "Grandero" or car2 == "Fierro" or car3 == "Injitsu")):
        return False
    if(car1 == "Grandero" and (state == "Colorado" or car2 == "Fierro" or car3 == "Injitsu")):
        return False
    if(car2 == "Fierro" and (state == "Colorado" or car1 == "Grandero" or car3 == "Injitsu")):
        return False
    if(car3 == "Injitsu" and (state == "Colorado" or car1 == "Grandero" or car2 == "Fierro")):
        return False
    return True


'''
FINSIHED
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
FINISHED
The vehicle from Alaska was fined 25 dollars more than the Fierro
'''
def hint5(state, car, fine1, fine2):
    if(state == "Alaska" and car == "Fierro"):
        if(fine1 - fine2 != 25):
            return False
    elif(car == "Fierro" and state == "Alaska"):
        if(fine2 - fine1 != 25):
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

    #Hint 1, 2, 3, 4, 5, 6 done here
    for i in range(len(cars)):
        for j in range(len(cars)):
            problem.addConstraint(FunctionConstraint(hint1), ["states" + str(i), "license_plates" + str(i), "fines" + str(i), "fines" + str(j)])
        problem.addConstraint(FunctionConstraint(hint2), ["cars" + str(i), "license_plates" + str(i), "fines" + str(i)])
        for j in range(len(cars)):
            for k in range(len(cars)):
                problem.addConstraint(FunctionConstraint(hint3), ["states" + str(i), "cars" + str(i), "cars" + str(j), "cars" + str(k)])
        for j in range(len(cars)):
            problem.addConstraint(FunctionConstraint(hint4), ["cars" + str(i), "fines" + str(i), "cars" + str(j)])
        for j in range(len(cars)):
            problem.addConstraint(FunctionConstraint(hint5), ["states" + str(i), "cars" + str(j), "fines" + str(i), "fines" + str(j)])
        problem.addConstraint(FunctionConstraint(hint6), ["cars" + str(i), "fines" + str(i), "license_plates" + str(i)])
        #We know Fierro subset ends in 1
        problem.addConstraint(FunctionConstraint(hint7), ["license_plates" + str(i), "fines" + str(i)])

    print "Number of Solutions: ", len(problem.getSolutions())
    for answer in problem.getSolutions():
        answer_set(answer)


if (__name__ == "__main__"):
    main()