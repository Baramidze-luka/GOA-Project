
def Mirror(List):
    reversed = List
    reversed.reverse()
    return List + reversed

print(Mirror([1,2]))