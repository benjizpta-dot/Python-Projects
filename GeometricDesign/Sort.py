
import os.path
def main():
    if not os.path.exists('countries.txt'):
        print('Error: countries.txt does not exist!')
        exit()
    infile = open('countries.txt', 'r')

    data = infile.read()
    #favs =[x.strip() for x in data.split(',')]
    temp = data.split(',')
    favs = []
    for x in temp:
        favs.append(x.strip())
    print(favs)
    infile.close()
    favs.sort()
    outfile = open('countries.txt', 'w')
    for x in favs:
        outfile.write(x+'\n')
    outfile.close()
main()

    