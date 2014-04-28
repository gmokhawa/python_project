#!usr/bin/python
#chmod +X readfasta.py
import sys

#1.this fuction receives a path to a file to be analysed.The program then dispalys the alignment information

#firstarg=str(sys.argv[1])
def Alignment_Information (fp):


    name = ""
    data=[]
    ID=[]
    sequence = []
    all_sequences=[]    
    Aligned_sequences=[]
    conserved_regions=[]
    d = {}
#    r=open("clustal.aln","r")

    for line in fp:  
   
        if line.startswith("CLUSTAL"):
            name+=line
            print """
 File Name: """, name
        elif line =="\n":     
            continue
        else: 
            if line[0]!= " ":
                l= line.index(" ")
                r= line.rindex(" ")
                ID.append(line[0:l])
                sequence.append(line[r+1:-1])            
 #       print ID 
 #       print sequence
  
    k=0
    for line in ID:
        if line not in d.keys():
            d[line]=sequence[k]
            
        else:
            d[line]=d[line]+sequence[k]
            
        k=k+1
    
    # d.values gives a list of (all_sequences) without the ID.Now i need to count all the A T G C characters (not the (-)s) in the list to get the total lenth of the sequences which can then be divided by the total number of sequences (given by len(d) or len(all_sequences).
     
    all_sequences=(d.values())
#    all_sequences=all_sequences.replace("-", " ")
    for i in all_sequences: # where i is a sequence in the list     
        #print i
        aligned_sequences=i #this gives sequences in lines that are perfectly aligned
        
        
        if i != "-":
            lengths=[len(i)]#the length of each sequence in the list
    
        if len(lengths)==0: 
            print 0
        else:(float(sum(lengths))/len(lengths))
        
#    print "The avarage length of the sequences: ", (float(sum(lengths))/len(lengths))   
    
#    print "The Average lenth of the sequences: ",sum(map(len,all_sequences))/len(all_sequences)
            
              
    for ID in d:

#        print ID, ":", d[ID] # gives the id and sequence
    
        print " Sequence  ID : %s in an alignment of length %i  nucleotide bases" % (ID, len(d[ID])) #gives the id and sequence length
      
#    print "\n The Average lenth of the sequences is: ",sum(map(len,all_sequences))/len(all_sequences)
    
    print "\n The avarage length of the sequences: ", (float(sum(lengths))/len(lengths)) 
    
    sequence=d.values() #this gives a list of all the values in the dictionary. from there i chose one sequence (sequence[0]) to loop through for 3 sequences.
    two=0
    three=0
    ind=0

    for x in sequence[0]:
        if x==sequence[1][ind] and x==sequence[2][ind]:
            three=three+1
        elif x==sequence[1][ind] or x==sequence[2][ind]:
            two=two+1
    print " The Number of X matches: "
    print "                         [02=]",two
             
    print "                         [03=]",three

    
    
    return d 

    
    
        
     
#################start of program

#iputfile=sys.argv[1]


fp=open("clustal_sequence",'r')

Information = Alignment_Information(fp)
print Information
   
    
    
    