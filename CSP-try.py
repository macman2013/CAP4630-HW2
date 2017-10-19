from constraint import *

'''
Henrietta's design went 35 feet
'''
def hint1(student, distance):
    if(student == "Henrietta" and distance != 35):
        return False
    if(student != "Henrietta" and distance == 35):
        return False
    return True
'''
Henrietta's deisgn was silver
'''
def hint2(student, color):
    if(student == "Henrietta" and color != "silver"):
        return False
    if(student != "Henrietta" and color == "silver"):
        return False
    return True

'''
Omar's design went somewhat farther than the silver airplane.
'''
def hint3a(student, color, distance):
    #Omar does not have the silver plane
    if(student == "Omar" and color == "silver"):
        return False
    #Silver plane cannot be the farthest
    if(color == "silver" and distance == 45):
        return False
    #Omar's plane is not the shortest
    if(student == "Omar" and distance == 15):
        return False
    return True


'''
Ella's design went 10 feet farther than the black plane
'''
def hint4(student, color, distance):
    ## Ella's plane is not the black plane
    if (student == "Ella" and color == "black"):
        return False
    #Ella's plane is not the slowest plane
    if (student == "Ella" and distance == 15):
        return False
    if(color == "black" and distance == 45):
        return False
    return True

'''
The pink plane went 10 feet further than the black plane
'''

def hint5(student, color, distance):
    #Ella's plane when 10 feet further than black plane so Ella's is pink
    if(student == "Ella" and color != "pink"):
        return False
    if(student != "Ella" and color == "pink"):
        return False
    #neither color can hold most extreme value
    if(color == "pink" and distance == 15):
        return False
    if(color == "black" and distance == 45):
        return False
    return True

'''
We know Ella is 10 more than the black plane
'''
def hint5a(distance0, color, distance):
     if(color == "black"):
         if(distance0 - distance == 10):
             return True
         return False
     else:
         return True

'''
Prints final set of answers for the CSP
'''
def answer_set(x):
    Ella = []
    Henrietta = []
    Omar = []
    Valerie = []
    answer_list = [Ella, Henrietta, Omar, Valerie]
    for a in x:
        if a[-1] == "0":
            Ella.append(x[a])
        if a[-1] == "1":
            Henrietta.append(x[a])
        if a[-1] == "2":
            Omar.append(x[a])
        if a[-1] in "3":
            Valerie.append(x[a])
    for person in answer_list:
        print person
def main():

    problem = Problem()
    students = ["Ella", "Henrietta", "Omar", "Valerie"]
    colors = ["black", "blue", "pink", "silver"]
    distances = [15, 25, 35, 45]

    for i in range(len(students)):
        problem.addVariable("students" + str(i), students)
        problem.addVariable("colors" + str(i), colors)
        problem.addVariable("distances" + str(i), distances)

    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(lambda a, b, c, d: a == "Ella" and b == "Henrietta" and c == "Omar" and d == "Valerie", ("students0", "students1", "students2", "students3"))
    # problem.addConstraint(lambda d: d == "Valerie", ("students3"))
    for i in range(len(students)):
        problem.addConstraint(FunctionConstraint(hint1), ["students" + str(i), "distances" + str(i)])
        problem.addConstraint(FunctionConstraint(hint2), ["students" + str(i), "colors" + str(i)])
        problem.addConstraint(FunctionConstraint(hint3a), ["students" + str(i), "colors" + str(i), "distances" + str(i)])
        problem.addConstraint(FunctionConstraint(hint4), ["students" + str(i), "colors" + str(i), "distances" + str(i)])
        problem.addConstraint(FunctionConstraint(hint5), ["students" + str(i), "colors" + str(i), "distances" + str(i)])

    #check within 10 of eachother
    for i in range(len(colors)):
        problem.addConstraint(FunctionConstraint(hint5a), ["distances0", "colors" + str(i), "distances" + str(i)])

    print len(problem.getSolutions())
    for answer in problem.getSolutions():
        answer_set(answer)


if (__name__ == "__main__"):
    main()