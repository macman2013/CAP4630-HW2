from constraint import *
problem = Problem()
problem.addVariable("students", ["Ella", "Henrietta", "Omar", "Valerie"])
problem.addVariable("colors", ["black", "blue", "pink", "silver"])
problem.addVariable("distances", [15, 25, 35, 45])
print len(problem.getSolutions())


def hint1(student, distance):
    if(student == "Henrietta" and distance != 35):
        return
    if(student != "Henrietta" and distance == 35):
        return
    return student, distance

def hint2(student, color):
    if(student == "Henrietta" and color != "silver"):
        return
    if(student != "Henrietta" and color == "silver"):
        return
    return student, color


problem.addConstraint(FunctionConstraint(hint1), ["students", "distances"])
#Check that hint 1 constraints are working
print len(problem.getSolutions())

#check that hint2 constraints are working
problem.addConstraint(FunctionConstraint(hint2), ["students", "colors"])
print len(problem.getSolutions())
