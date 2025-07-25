try:
    file='Files\\output.txt'
    f=open(file,'w')
    write = f.write(input("Enter text to write to the file: "))
    f.close()
    if write >0 :
        print("Data successfully written to {}.".format(file))
    else:
        print("Something went wrong.")

    f = open(file, 'a')
    append = f.write("\n"+input("Enter additional text to append: "))
    f.close()

    if append > 0:
        print("Data successfully appended.")
    else:
        print("Something went wrong in appending data.")

    f = open(file, 'r')
    read = f.read()
    print("Final content of {}:\n".format(file),read)
    f.close()
except FileNotFoundError:
    print("Error: The {} was not found.".format(file))


