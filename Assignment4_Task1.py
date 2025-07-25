try:
    file='Files\\sample.txt'
    f=open(file,'r')
    lines = f.readlines()
    print("Reading file content:\nLine1:",lines[0],"Line2:",lines[1])
    f.close()
except FileNotFoundError:
    print("Error: The {} was not found.".format(file))


