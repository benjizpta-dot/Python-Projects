import os.path

def main():

    if os.path.isfile("data.txt"):
        print("data.txt exists")

    else: 
        print("data.txt does not exist")
        exit()
    infile = open('data.txt', 'r')
    presidents = infile.read()
    pres = infile.readlines()
    presidentList = presidents.split('\n')
    print(presidentList)
    
   
main()