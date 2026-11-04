def main():

    outfile = open('odds.txt', 'w')

    for i in range(1, 100, 2):
        outfile.write(str(i) + ' ')

    outfile.close()


main()   