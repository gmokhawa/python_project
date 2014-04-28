#!usr/bin/python
#chmod +X readfasta.py
import sys

#1.this fuction receives a path to a file to be analysed.The program then dispalys the alignment information

#firstarg=str(sys.argv[1])
def Information_per_Sequence (fp):


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
 
    k=0
    for line in ID:
        if line not in d.keys():
            d[line]=sequence[k]
            
        else:
            d[line]=d[line]+sequence[k]
            
        k=k+1
        
    
    
    # d.items gives a list of all items in the dictionary (d).Now i want to be able to choose one line form the list and print it's  id (key), lenth (value), count the DNA bases and print the sequence in characters of 60.since d[k] prints the dictionary and it value, and d.keys() only prints the keys, i will look for the key/[ID] of interest in d.keys() then analyse it's value(d[key])
     
    Id= raw_input (" enter sequence ID: ")
    
    if Id in d.keys():
        
        
        print " Sequence Id:     %s\n Sequence Length: %s" % (Id, len(d[Id]))
        
        print ' Frequency per base: \n                   [A]:', str (d[Id]).count("A")
        print '                   [B]:',str (d[Id]).count("C")
        print "                   [G]:",str (d[Id]).count("G")
        print "                   [T]:",str (d[Id]).count("T")

               
    else: 
        print "Id not found"
        
    sequences= d[Id]
    sequences=sequences.replace('-','')
    
    temp=[]
    seq=''
    for x in sequences:

        y=1 #creates a counter for x from 1
        if y%60!=0: #60 being the max characters, so it will go new line at 61
            seq+=x
        else:
            print seq
            print ("\n")
            seq=x
    print"Sequence:", seq
            

    
        
    
    
    return d 

    
    
        
     
#################start of program

#iputfile=sys.argv[1]


fp=open("clustal_sequence",'r')

Information = Information_per_Sequence(fp)
print Information
   
    
    
    