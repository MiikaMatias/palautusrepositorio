from matchers import All, Or, Not, And, HasAtLeast, HasFewerThan, PlaysIn

class Query():

    def __init__(self, matcher=All()) -> None:
        self._matcher = matcher

    def hasAtLeast(self, value:int, of: str):
        return Query(And(self._matcher,HasAtLeast(value, of)))

    def hasFewerThan(self, value:int, of: str):
        return Query(And(self._matcher,HasFewerThan(value, of)))

    def playsIn(self, team:str):
        return Query(And(self._matcher,PlaysIn(team)))
    
    def oneOf(self, m1, m2): 
        return Query(Or(m1, m2))

    def build(self):
        return self._matcher