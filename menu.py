#!usr/bin/python
#chmod +X readfasta.py
import sys

def menu():

    #this program displays the menu of the multiple alignnment analyser
    #menu.py


    status=True
    print """Select an option from below:

          1) Open a Multiple Alignment File               (O)
          2) Alignment Information                        (A)
          3) Alignment Explorer                           (E)
          4) Information per Sequence                     (I)
          5) Analysis of Glycosylation Signatures         (S)
          6) Export to Fatsa                              (X)
          7) Exit                                         (Q)"""
       
    menu={ "-":"-","1":"Open a Multiple Alignment File ", "2":"Alignment Information","3":"Alignment Explorer","4":"Information per Sequence","5":"Analysis of Glycosylation Signatures","6":"Export to Fatsa","7":"Exit"}




    while status:
    
        options=menu.keys()  
        options.sort()
    
        selection=raw_input("Enter a number or a letter, then press enter to view an option: ")
    
        for key in menu:
            print key + ":"+ menu[key]
        
    
        if selection== "1" or selection== "O":
            print " You have selected to Open a Multiple Alignment"          
            
        elif selection == "2" or selection== "A":
            print " You have selected to view the Alignment Information"
                
        elif selection== "3" or selection== "E":
            print "You have selected to view the Alignment Explore"
                        
        elif selection == "4" or selection== "I":
            print " You have selected to view the Information per sequence"
        
        elif selection== "5" or selection=="S":
            print "You have selected to view the Analysis of Glycosylation Signature"
                
        elif selection == "6" or selection== "X":
            print " You have selected to view the Export to Fasta Function"       
        
    
        elif selection== "7" or selection=="Q":
            break
        else:
            print "unknown option please refer to the menu"
        
        
        
 
 




menu()

