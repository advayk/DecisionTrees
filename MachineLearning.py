
file = list()
def ReadFile(file):
    with open(file) as f:
        lines = f.readlines()
        print(lines)


ReadFile("TennisDataSet.txt")


#def entropy():
#    entropy = -(Yes)*(log(yes)/log(2)) - (pNo * (log_2(no)/log(2))
