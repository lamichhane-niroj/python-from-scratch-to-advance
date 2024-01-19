
def nothing():
    print('I\'m useless')


print(nothing)  # This prints the address of the function in the memory block


# what does this statement do?
new = nothing
# This new is just the alies of nothing, they are pointing to same memory block. Hence, they are same
new()
nothing()
