#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 01:11:01 2021

@author: johnmckenna
"""

from Teams import Teams

class League:
    def __init__(self, Team1, Team2, Team3):
        self.Team1 = Team1
        self.Team2 = Team2
        self.Team3 = Team3
        
    def PrintTeamNames(self):
        print(self.Team1.name + ",", self.Team2.name + ",",  self.Team3.name)
        
    def PrintTeamAval(self):
        print(self.Team1.name, self.Team1.avaliability)
        print(self.Team2.name, self.Team2.avaliability)
        print(self.Team3.name, self.Team3.avaliability)
        
        
team1 = Teams("Average Joes")
team1.add_avaliability(1800)
team2 = Teams("Mel Kiper's")
team2.add_avaliability(900)
team3 = Teams("Sweats")
team3.add_avaliability(1620)

league = League(team1, team2, team3)
league.PrintTeamNames()
league.PrintTeamAval()
        
    
        
        

