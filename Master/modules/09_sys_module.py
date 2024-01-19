import sys

# system error print
sys.stderr.write("This is the error text\n")
sys.stderr.flush()

# system output print
sys.stdout.write("This is the normal output text\n")

# command line argument like c can be used by using sys module
print(sys.argv)


def greet(argv):
    if len(argv) > 1:
        print("Hello ", argv[1])
    else:
        print("Hello ")


greet(sys.argv)
