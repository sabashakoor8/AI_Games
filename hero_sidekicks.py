def select_travellers(candidates):
    # select 1 or 2 travellers
    # since there are only these two cases, choose
    # pedestrian approach rather than recursion
    # one traveller
    for first in range(len(candidates)):
        yield [candidates[first]]
        # two travellers
    for first in range(len(candidates)):
        for second in range(first+1, len(candidates)):
            yield[candidates[first], candidates[second]]
other_side = { "left" : "right", "right" : "left" }
def safe(state):
    # never leave your sidekick alone with another hero
    person_side, _ = state
    for side in ['left', 'right']:
        # check all sidekicks on given side without their hero
        lone_kick = [index for (person, index) in person_side
            if person == 'kick'
            if person_side[person, index] == side
            if person_side['hero', index] != side]
        # collect all heros on the current side (they are the bad ones!)
        present_hero = [index for (person, index) in person_side
            if person == 'hero'
            if person_side[person, index] == side]
        # if there is a lone sidekick *and* another hero, trouble!
        if lone_kick and present_hero:
            return False
    return True
class Hero:
    def start(self):
         # where everybody is, where the boat is
        return {(person, index):"left"
            for person in ['hero', 'kick']
            for index in [1,2,3]}, "left"
    def goal(self, state):
        person_side, boat = state
        # is everybody on the right?
        return set(person_side[person] for person in person_side) == { "right" }
    # person_side.values() should also work
    def succ(self, state):
        # who can move?
        person_side, boat = state
        # collect all people on the side of the boat
        person_with_boat = [person for person in person_side if person_side[person] == boat]
        for traveller_group in select_travellers(person_with_boat):
            new_side = person_side.copy() # never change the original
            for traveller in traveller_group:
                # the traveller moves to the other side
                new_side[traveller] = other_side[person_side[traveller]]
            new_state = new_side, other_side[boat]
            if safe(new_state):
                yield new_state
game = Hero()