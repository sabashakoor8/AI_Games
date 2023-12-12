def successors(stable):
    # find empty spot
    empty = stable.index(0)
    # generate list of unfiltered candidate positions
    candidates = [empty-2, empty-1, empty+1, empty+2] 
    #print(candidates)
    # keep only those which are inside the stable
    candidates = [c for c in candidates if c >= 0 and c < len(stable)]
   # print(candidates)
    # Cows can always move right, Sheep always left, and from two fields
    # apart, they have to jump over an opposite animal
    candidates = [c for c in candidates if
        stable[c:c+2] == [1, 0] or # cow can move right
        stable[c-1:c+1] == [0, 2] or # sheep can move left
        stable[c:c+3] == [1, 2, 0] or # cow jumps over sheep
        stable[c-2:c+1] == [0, 1, 2]] # sheep jumps over cow
    # make sure that all these entries are occupied
    # (not necessary for operation, just better style)
    assert not [c for c in candidates if stable[c] == 0]
    for c in candidates:
        new_stable = stable[:] # make a copy
        # move the candidate into empty pos
        new_stable[c], new_stable[empty] = new_stable[empty], new_stable[c]
        yield new_stable # remember where we were
def solutions(stable):
    if stable == goal_stable:
        return [stable]
    # else, depth first
    for new_stable in successors(stable):
        # print new_stable
        sol = solutions(new_stable)
        if sol:
            return [stable] + sol
#start_stable=['C','C','C','C','E','S','S','S','S']
#goal_stable=['S','S','S','S','E','C','C','C','C']
start_stable = [1,1,1,1,0,2,2,2,2]
goal_stable = [2,2,2,2,0,1,1,1,1]
for p in solutions(start_stable):
    print(p)

