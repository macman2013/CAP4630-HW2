from constraint import *
problem = Problem()
problem.addVariable("students", ["Ella", "Henrietta", "Omar", "Valerie"])
problem.addVariable("colors", ["black", "blue", "pink", "silver"])
problem.addVariable("distances", [15, 25, 35, 45])
print len(problem.getSolutions())

'''
Henrietta's design went 35 feet
'''
def hint1(student, distance):
    if(student == "Henrietta" and distance != 35):
        return
    if(student != "Henrietta" and distance == 35):
        return
    return student, distance
'''
Henrietta's deisgn was silver
'''
def hint2(student, color):
    if(student == "Henrietta" and color != "silver"):
        return
    if(student != "Henrietta" and color == "silver"):
        return
    return student, color

'''
Omar's design went somewhat farther than the silver airplane.
'''
def hint3(student, color, distance):
    if(student == "Omar")

problem.addConstraint(FunctionConstraint(hint1), ["students", "distances"])
#Check that hint 1 constraints are working
print len(problem.getSolutions())

#check that hint2 constraints are working
problem.addConstraint(FunctionConstraint(hint2), ["students", "colors"])
print len(problem.getSolutions())
