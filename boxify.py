# The function source code is tweetable!
def boxify(s): return len(s)*"+---"+"+\n"+'| '+' | '.join(list(s))+" |\n"+len(s)*"+---"+'+'

if __name__ == '__main__':
    print(boxify('Stupendous!'))
