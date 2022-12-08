#!/usr/bin/python3

"""
Advent coding
puzzle 1 - who carries the most calories
puzzle 2 - what's the score for the cheat strategy rock/paper/scissors
"""
# email:tony_zheng35@hotmail.com
# date: 2022-12-01

import os
import time
import sys
import argparse
import datetime
import string

class Advent(object):

    def __init__(self):

        self.elfs = []
        self.calories = []

    def GetOptions(self):

        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--input_file", action = "store", dest = "InputFile", required=True, help = "Input File")
    
        options = parser.parse_args()
        self.input_file = options.InputFile

        self.time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") # create timestamped log
        self.LogFileName = f"Advent_{self.time}.txt"

    def CountCalories(self):

        with open(self.input_file, 'r') as input_list:
            content = input_list.readlines()
            elves_calories = {}
            calories = []
            count = 0
            for idx, line in enumerate(content):
                if line[0].isdigit():
                    line = line.replace('\n','')
                    calories.append(line)
                elif line == "\n":
                    count += 1
                    elves_calories[count] = sum([int(cal) for cal in calories])
                    calories = []
            
            calories = elves_calories.values()
            top_3 = sorted(calories, key = int)[::-1][:3]
            f"The most calories a elf is carrying: {max(calories)}"
            f"The calories carried by the top 3 carriers in total is: {max(top_3)}"
            self.LOG = open(self.LogFileName, "a")
            self.LOG.write(f"The most calories a elf is carrying: {max(calories)}\n")
            self.LOG.write(f"The calories carried by the top 3 carriers in total is: {sum(top_3)}")
            self.LOG.close()
    
    def CountScores(self):
        
        #p1_scores = {'A': 1, 'B': 2, 'C': 3}
        p2_scores = {'X': 0, 'Y': 3, 'Z': 6}
        #win_loss = {0:[('A','X'),('B','X'),('C','X')], 3:[('A','Y'),('B','Y'),('C','Y')], 6:[('C','Z'),('A','Z'),('B','Z')]}
        win_type = {1:[('A','Y'),('B','X'),('C','Z')], 
                    2:[('A','Z'),('B','Y'),('C','X')], 
                    3:[('A','X'),('B','Z'),('C','Y')]
                    }

        with open(self.input_file, 'r') as input_list:
            content = input_list.readlines()
            #rounds = {}
            player1 = []
            player2 = []
            score = 0

            for idx, line in enumerate(content):
                line = line.replace('\n','')
                line = line.split(' ')
                if line[0] in ['A','B','C']:
                    player1.append(line[0])
                if line[1] in ['X','Y','Z']:
                    player2.append(line[1])
                    score += p2_scores[line[1]]

        games = list(zip(player1, player2))

        for game in games:
            for k, v in win_type.items():
                if game in v:
                    score += k
                else:
                    continue
        
        f"The score for strategy scenario: {score}"
        self.LOG = open(self.LogFileName, "a")
        self.LOG.write(f"The score for strategy scenario: {score}")
        self.LOG.close()

    def RucksackItems(self):
        
        low_priority = list(string.ascii_lowercase)
        high_priority = list(string.ascii_uppercase)
        low_numbers = list(range(1, 27))
        high_numbers = list(range(27, 53))
        lower_dict = dict(zip(low_priority, low_numbers))
        upper_dict = dict(zip(high_priority, high_numbers))

        with open(self.input_file, 'r') as input_list:
            content = input_list.readlines()
            #rounds = {}
            #compartment1 = []
            #compartment2 = []

            priority = []

            group_numbers = list(range(0, len(content)+1, 3))
            group_numbers.remove(0)
            print (group_numbers)

            group_counter = []
            for x in group_numbers:
                elfs = []
                for idx, line in enumerate(content):
                    line = line.replace('\n','')
                    if x not in group_counter:
                        if idx == (x-1):
                            group_counter.append(x)
                            elfs.append(line)
                            print (elfs)
                            common = list(set(elfs[0]) & set(elfs[1]) & set(elfs[-1]))
                            print (common)
                            for c in common:
                                if c.islower():
                                    priority.append(lower_dict[c])
                                elif c.isupper():
                                    priority.append(upper_dict[c])
                                else:
                                    print(f"error, not alphabet")
                            break
                        elif idx < x and not group_counter:
                            elfs.append(line)
                        elif idx < x and idx >= group_counter[-1]:
                            elfs.append(line)
                        elif idx < x and idx < group_counter[-1]:
                            continue
                            
                #n = int(len(line)//2)
                #compartment1.append(line[:n])
                #compartment2.append(line[n:])
                
            #sacks = list(zip(compartment1, compartment2))
            #for sack in sacks:
                #sack1 = set(sack[0])
                #sack2 = set(sack[1])
                #common = list(sack1 & sack2)
                
        print (priority)
        print (sum(priority))

        #print (f"The sum of priorities common to both compartments: {sum(priority)}")
        print (f"The sum of priorities of item types: {sum(priority)}")
        self.LOG = open(self.LogFileName, "a")
        self.LOG.write(f"The sum of priorities common to both compartments: {sum(priority)}")
        self.LOG.close()

    def CampCleanup(self):

        with open(self.input_file, 'r') as input_list:
            
            content = input_list.readlines()
            count = 0
            for idx, line in enumerate(content):
                line = line.replace('\n','')
                elf1 = [int(x) for x in line.split(",")[0].split("-")]
                #print (elf1)
                elf2 = [int(y) for y in line.split(",")[1].split("-")]
                #print (elf2)
                if max(elf1) >= max(elf2) and min(elf1) <= min(elf2):
                    print (elf1, elf2)
                    #print ('elf1 contains elf2')
                    count += 1
                elif max(elf2) >= max(elf1) and min(elf2) <= min(elf1):
                    #print (f"max elf2: {max(elf2)}")
                    #print (f"max elf1: {max(elf1)}")
                    #print (f"min elf2: {min(elf2)}")
                    #print (f"min elf1: {min(elf1)}")
                    print (elf2, elf1)
                    #print ('elf2 contains elf1')
                    count += 1
                elif min(elf2) <= max(elf1) and min(elf2) >= min(elf1):
                    count += 1
                elif min(elf1) <= max(elf2) and min(elf1) >=min(elf2):
                    count += 1
                else:
                    continue

        print (count)
        
        #print (f"The sum of priorities common to both compartments: {sum(priority)}")
        print (f"The number of pairs that has range that fully contain the other: {count}")
        #self.LOG = open(self.LogFileName, "a")
        #self.LOG.write(f"The number of pairs that has range that fully contain the other: {count}")
        #self.LOG.close()

    def CrateStacking(self):

        with open(self.input_file, 'r') as input_list:
            content = input_list.readlines()
            stack_crate = {}
            for idx, line in enumerate(content):
                line = line.replace('\n','')
                line = line.split(" ")
                if idx < 8:
                    count = 0
                    stack = 0
                    for i, l in enumerate(line):
                        if l == '':
                            count += 1
                            #print(count)
                        if count == 4:
                            stack += 1
                            #print(stack)
                            count = 0
                            if str(stack) not in f"{stack_crate.keys()}" and stack != 0:
                                stack_crate[f"{stack}"] = []
                        if "[" in l:
                            crate = l.split("[")[-1].split("]")[0]
                            #print(crate)
                            stack += 1
                            if str(stack) not in f"{stack_crate.keys()}" and stack != 0:
                                stack_crate[f"{stack}"] = []
                            stack_crate[f"{stack}"] += crate 
   
                elif idx == 8:
                    stack_numbers = list(filter(None, line))
                elif line == '':
                    continue
                else:  
                    move = 0
                    stack_f = ''
                    stack_t = ''
                    for i, l in enumerate(line):
                        if l == 'move' or l == 'from' or l == 'to':
                            continue
                        elif line[i-1] == 'move':
                            move = line[i]
                            print (move)
                        elif line[i-1] == 'from':
                            stack_f = line[i]
                            print (stack_f)
                        elif line[i-1]  == 'to':
                            stack_t = line[i]
                            print (stack_t)

                        if move and stack_t and stack_f:
                            print (stack_crate[stack_f][:int(move)])
                            print (stack_crate[stack_t])
                            stack_crate[stack_t][:0] += stack_crate[stack_f][:int(move)]
                            stack_crate[stack_f] = stack_crate[stack_f][int(move):]
                            #print (stack_crate)
    
            print (stack_crate)
        
        print (f"The top of each stack are:\n")
        self.LOG = open(self.LogFileName, "a")
        self.LOG.write(f"The top of each stack are:\n")
        for k,v in stack_crate.items():
            print (f"stack:{k}, crate: {v[0]}\n")
            self.LOG.write(f"stack:{k}, crate: {v[0]}\n")
        self.LOG.close()
    
    def SubroutineSignal(self):

        with open(self.input_file, 'r') as input_list:
            content = input_list.read()
            packets = []
            for idx, dp in enumerate(content):
                if idx-13 >= 0:
                    packet = content[idx-13:idx+1]
                    print (packet)
                    if len(set(packet)) == len(packet):
                        print (f"The number of characters that need to be processed before first of start-of-message marker is detected : {idx+1}")
                        self.LOG = open(self.LogFileName, "a")
                        self.LOG.write(f"The number of characters that need to be processed before processing is : {idx+1}")
                        self.LOG.close()
                        break
                else:
                    continue
 
def Main():
    Run = Advent()
    Run.GetOptions()
    #Run.CountCalories()
    #Run.CountScores()
    #Run.RucksackItems()
    #Run.CampCleanup()
    #Run.CrateStacking()
    Run.SubroutineSignal()

if __name__ == "__main__":
    Main()

    