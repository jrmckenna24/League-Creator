# -*- coding: utf-8 -*-


class Teams:
    def __init__(self, TeamName):
        self.name = TeamName
        self.avaliability = [] 
        
    def add_avaliability(self, time):
        self.avaliability.append(time)
        self.avaliability.sort()
        
    def remove_avaliability(self, time):
        self.avaliability.remove(time)
        self.avaliability.sort()
        


