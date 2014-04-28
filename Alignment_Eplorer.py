#!usr/bin/python
#chmod +X readfasta.py
import sys


#4.Information per sequence:This option gives user the opportunity to selct one of the sequences of the alignment to display some basic information about it.


#firstarg=str(sys.argv[1])
def Alignment_Explore(fp):


    name = ""
    data=[]
    ID=[]
    sequence = []
    ID_sequence_alignment=[]
    conserved_regions=[]
    d = {}
    s=input("Enter the start of segment: ")
    e=input ("Enter the end of segment: ")    

    for line in fp:  
        
        #now to put the word clustal in to name variable
   
        if line.startswith("CLUSTAL"):
            name+=line
            print "\n Segment %i-%i of"% (s,e), name   

        elif line =="\n":     
            continue
        else: 
            if line[0]!= " ":
                l= line.index(" ")
                r= line.rindex(" ")
                ID.append(line[0:l])
                sequence.append(line[r+1:-1])            
    
    k=0
    for line in ID:
        if line not in d.keys():
            d[line]=sequence[k]
            
        else:
            d[line]=d[line]+sequence[k]
            
        k=k+1
   #to produce a sequence Id (which is the key in my dictinary) and then produce the sequence (value) i printed ID, d[ID] in a for Key in Dictionay loop. this procuses a list (sequences) with len(sequences)=2 where sequences[0] is the key/sequence Id, and sequences[1] is the nucleotide sequence. so since i want to splice the nucleotide.

         
    for ID in d:
        sequences=ID, d[ID]
              
#        print 'splice', ID, sequences[1][s:e] 
       
        # to print formatted sequence data of 60 characters. Sequence lines are generated from the the script above, where sequences=ID, sequences[1][s:e]
           
        #since range function can be used to generate intergers from 0(minimum i value) to  (n=len(i)= maximum value of i) and increasing by 60 characters. I can set the min value of j to 0, and splice by jumping every 60, characters, then join the characters in to a temp[] list.
        sequences=ID, sequences[1][s:e] 
        print "new",sequences
               
        temp=[]
        for i in sequences:
                
                for j in range(0,len(i),60): 
                    temp.append(i[j:j+60])
                print  "\n    ".join(temp)
       
       
       
       
    return d

    

 
   
#################start of program
#iputfile=sys.argv[1]


fp=open("clustal_sequence",'r')

Explore=Alignment_Explore(fp)
print Explore

  
    
   
    
    
    