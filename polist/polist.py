from collections import defaultdict
 
class PartialOrderedList(list):
    def __init__(self, values=[]): 
        list.__init__(self)
        self.groups = []
        for value, group in values:
            list.append(self, value)
            self.groups.append(group)
    def __eq__(self, l): 
        grouped = defaultdict(list)
        for i, group in enumerate(self.groups):
            grouped[group].append(list(self)[i])
        for e, group in zip(l, self.groups):
            if e in grouped[group]:
                grouped[group].remove(e)
            else:
                return False
        return True
    def __ne__(self, l):
        return not self.__eq__(l)
    def append(self, value, group):
        list.append(self, value)
        self.groups.append(group)
