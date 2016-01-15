#!/usr/bin/python3

"""This module contains the code used to complete the first project of
CSCI 312, "derive".

Author: Cullen Rombach (cmromb)
"""  
def main():
    """Executes the algorithm outlined in the project description:
        
    Read the length N from the command argument (or from input).
    Read and store all the productions.
    Push the start symbol onto the  worklist.
    While the worklist is not empty:
        Get and delete one potential sentence s from the worklist.
        If the | s | > N, continue.
        If s has no nonterminals, print s and continue.
        Choose the leftmost nonterminal NT.
        For all productions NT -> rhs:
            Replace NT in s with rhs; call it tmp.
            Store tmp on worklist.
    """
    # Store the maximum length and filename from input. 
    maxLength = int(input("Length? "))
    filename = input("Filename? ")
    
    # Read through the given file and store its contents in a list.
    rawRules = []
    for line in open(filename, "r"):
        rawRules.append(line.split())
        
    # Store the start symbol.
    startSymbol = rawRules[0][0]
    
    # Create a dictionary of grammar rules.
    rulesDict = dict()
    for rule in rawRules:
        if rule[0] not in rulesDict.keys():
            rulesDict[rule[0]] = []
        i = 2;
        newRule = ""
        while i < len(rule)-1:
            newRule += rule[i] + " " 
            i += 1
        newRule += rule[i]
        rulesDict[rule[0]].append(newRule)
        
    # Initialize the worklist and the filterlist.
    worklist = [startSymbol]
    filterlist = []
    
    # Execute the steps in the "While the worklist is not empty:"
    # section of the program outline.
    while len(worklist) != 0:
        nt = ""
        s = worklist.pop(0)
        if len(s.split()) <= maxLength:    
            # Get a nonterminal in s and store it in nt
            for item in s.split():
                if item in list(rulesDict.keys()):
                    nt = item
                    break
            # Replace the leftmost NT in s with all its productions,
            # then add the new sentences to the worklist.
            if(nt != ""):
                for production in rulesDict[nt]:
                    sList = s.split()
                    for ndx, item in enumerate(sList):
                        if item == nt:
                            sList[ndx] = production
                            break
                    tmp = ""
                    for ndx in range(len(sList)):
                        if ndx == len(sList)-1:
                            tmp += sList[ndx]
                        else:
                            tmp += sList[ndx] + " "
                    # Put tmp back onto the worklist.
                    worklist.append(tmp)
            else:
                if s not in filterlist:
                    filterlist.append(s)
                    print(s)
        
# Execute the program.
main()
    