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

problem.addConstraint(FunctionConstraint(hint1), ["students", "distances"])
#Check that constraints are working
print len(problem.getSolutions())
print(problem.getSolutions())
