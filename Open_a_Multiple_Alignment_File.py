#!usr/bin/python
#chmod +X readfasta.py
import sys


#1.this fuction receives a path to a file to be analysed.The program the loads the  fasta file


#firstarg=str(sys.argv[1])
def Open_a_Multiple_Alignment_File(fp):


    name = ""
    data=[]
    ID=[]
    sequence = []
    conserved_regions=[]
    d = {}
#    r=open("clustal.aln","r")

    for line in fp:  
        
        #line=line.rstrip()
        #now to put the word clustal in to name variable
   
        if line.startswith("CLUSTAL"):
            name+=line
            print """
 File Name: """,  name      
        
    #now to get all the conserved regions(*) in to one conserved_regions list
       # elif line.startswith(" "):
       #conserved_regions+=line
      #  print conserved_regions

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
    # to print formatted sequence data  data of 60 characters. Sequence lines are generated from the dictionary using the d.values() command to make a sequences list to work from.
    
    #since range function can be used to generate intergers from 0(minimum i value) to  (n=len(i)= maximum value of i) and increasing by 60 characters. I can set the min value of j to 0, and splice by jumping every 60, characters, then join the characters in to a temp[] list.
    sequences=d.values()
    #print "dd", d[ID]
    temp=[]
    for i in sequences:
        for j in range(0,len(i),60): 
            temp.append(i[j:j+60])
    print '\n'.join(temp)
        
        
        
    return d


 #   for line in (data):
 
 #       data="\n"+line.rstrip()
    
 #       data=line.split(" ")  
 
#       line.index(" ")
#        line.rindex(" ")
        
   
#################start of program
#iputfile=sys.argv[1]


fp=open("clustal.aln",'r')

sequence=Open_a_Multiple_Alignment_File(fp)
print "Sequence: ", sequence
#print Open_a_Multiple_Alignment_File(fp)
  
    
   
    
    
    