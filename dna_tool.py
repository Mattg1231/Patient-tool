#Import modules
from Patient import Patient
import random

#initialize global variable
random.seed(5) # random seed used for reproducibility
LENGTH_DNA=20


########################
##### Functions ########
########################

def display_menu():
    """ Display all the options, no input, no output """
    print("\n1-List; 2-Info; 3-Remove; 4-Insert; 5-Compare; 6-Compare all; 7-Analyze")


def random_base():
    """select the letter A,C,G,T at random, output (String) """
    bases=["A","C","G","T"]
    return random.choice(bases)
#chooses a random base 

def initialize():
    list_name=["Andrea","Bob","Brooke","Connor","James","Jenna","John","Julie","Kate","Keith","Kelly","Luke","Mark","Pat","Taylor","Tony"]
    list_age=[37,28,34,27,25,44,45,37,48,28,25,33,34,26,30,55]
    list_pat=[]
    for i in range(16):
        list_pat+=[(Patient(list_name[i],list_age[i],random_strand()))]
    return list_pat
#Manually initializes all 16 patients and gives them a random dna strand

def random_strand():
    x=""
    for i in range(LENGTH_DNA):
        x+=random_base()
    return x
#This created a random string of bases that is Length_dna long(20 in this case)

def display(list_pat,condition):
    if len(condition)==0:
        print("","Name","age","DNA-strand (20 length)",sep="\t")
        print("----------------------------------------------------------------")
        for i in range(len(list_pat)):
            print(str(i+1),list_pat[i].name,list_pat[i].age,list_pat[i].strand,sep="\t")
    else:
        print("","Name","age","DNA-strand (20 length)"+"\t",sep="\t",end="")
        for i in range(len(condition)):
            print("\t"+condition[i],end="")
        space="----------------------------------------------------------------"
        for i in range(len(condition)):
            for j in condition[i]:
                space+="--"
        print("\n"+space)
        for i in range(len(list_pat)):
            print(str(i+1),list_pat[i].name,list_pat[i].age,list_pat[i].strand,sep="\t",end="")
            for j in range(len(condition)):
                if not(j==len(condition)-1):
                    print("\t"+"\t"+str(list_pat[i].has_condition[j]),end="")
                else:
                    print("\t"+"\t"+str(list_pat[i].has_condition[j]))
        
#Here I check if there is a condition if not I loop through the list and print out the attrabutes. If there is a condition, I print
#it out in a way where I loop through the conditions to print it out after the main section that never changes(this way it will change
# when you add more conditions). I also added a part where it inserted more "--" for every letter in the condition so it would look nice

def info(list_pat,condition,perc):
    total=len(list_pat)
    age_range=[0.0,0.0,0.0,0.0,0.0,0.0]
    age_total=0
    for i in range(total):
        if list_pat[i].age<20:
            age_range[0]=age_range[0]+1
        elif list_pat[i].age<30 and list_pat[i].age>=20:
            age_range[1]=age_range[1]+1
        elif list_pat[i].age<40 and list_pat[i].age>=30:
            age_range[2]=age_range[2]+1
        elif list_pat[i].age<50 and list_pat[i].age>=40:
            age_range[3]=age_range[3]+1
        elif list_pat[i].age<60 and list_pat[i].age>=50:
            age_range[4]=age_range[4]+1
        else:
            age_range[5]=age_range[5]+1
        age_total+=list_pat[i].age
    print("#Patients",total)
    print("<20:",str(age_range[0]/total*100)+"%")        
    for i in range(4):
        print(str((i+2)*10)+"'s: "+str(age_range[i+1]/total*100)+"%")
    print(">=60: "+str(age_range[5]/total*100)+"%")
    print("\nAge Mean:",age_total/total)
    if not(len(condition)==0):
        for i in range(len(condition)):
            print(condition[i]+": "+str(perc[i])+"%")
#Here I run through a loop of the whole list and find which age group each patient is in aswell as adding the total age
#in order to be able to find the age mean. Then i check for conditions. If there are any i print them out with the percent that i saved
#in the main file project2

def add_new_patient(list_pat):
    name=str(input("Enter Name: "))
    age=int(input("Enter Age: "))
    first_true=False
    second_true=False
    while True:
        strand=str(input("Enter DNA strand : "))
        if not(len(strand)==LENGTH_DNA):
            print("Bad input! -length must be",LENGTH_DNA)
        else:
            first_true=True
        for i in range(len(strand)):
            if not(strand[i:i+1]=="A" or strand[i:i+1]=="C" or strand[i:i+1]=="G" or strand[i:i+1]=="T"):
                print("Bad input! -must enter A,C,G,T")
                break
            else:
                second_true=True
        if first_true and second_true:
            break
    list_pat+=[(Patient(name,age,strand))]
    return list_pat
#goes through a whileloop until 20 DNA bases are inserted. I also went an extra step and made sure that they insert bases
#such as A C T G and not some random letters into the command promt. After i return the patient which was made given the 
#inputs 

def compare(p1,p2): 
    s=""
    for i in range(LENGTH_DNA):
        if (p1.strand[i]==p2.strand[i]):
            s+=p1.strand[i]
        else:
            s+="x"
    return s
#Function has for loop that compairs each base in order and replaces x if they are different using an f statement. Returns the strand

def check_completness(p1):
    num=0.0
    for i in p1:
        if not(i=="x"):
            num+=1
    return num/LENGTH_DNA*100
#checks if there is not a x and then adds to num. divide num by total *100 to get the percent and returns it

def compare_all(list_pat):
    num=0
    for i in range(len(list_pat)):
        for j in range(i):
            num=check_completness(compare(list_pat[i],list_pat[j]))
            if (num>33):
                print(list_pat[i].name+" vs "+list_pat[j].name,str(num)+"%")
#goes through a nested for loop to compare each patient in the list with eachother, then for completeness. 
# If its over 30% it gets printed.

def find_pattern(list_pat,seq):
    num=0.0
    for i in list_pat:
        i.has_condition+=[False]
    for i in range(len(list_pat)):
        for j in range(LENGTH_DNA):
            if list_pat[i].strand[j:int(j+len(seq))]==seq:
                list_pat[i].has_condition[-1]=True
                num+=1
                break
    return num/len(list_pat)*100
#I did a for loop to append false into the patients boolean list. Then i iterated throughout each strand to find if the 
# sequnced was inside of it. If it was make it true, add 1 to the count, and change the boolean to be true. Since I wanted to
# get the bonus, I changed my main method to store the conditions, percentage, and if each patient has the conditions in lists so i can
#print them out again



##########################
########## Main Function #  to uncomment step by step fo testing
##########################
                
def main():
    ##################### TEST FOR OPTION 1
    print("\n****TEST the random_strand function****")
    print(random_strand())

    ##################### TEST FOR OPTION 1
    print("\n****TEST the class Patient****")
    patient=Patient("Tom",20,random_strand())
    print(patient.name,patient.age,patient.strand)
    
    ##################### TEST FOR OPTION 1
    print("\n****TEST the display function****")
    patients=[patient,Patient()]
    patients[1].name="Lucy"
    patients[1].age=25
    patients[1].strand="TCTTGTAAACTCGGAAACTG"
    display(patients)

    ##################### TEST FOR OPTION 2
    print("\n****TEST the info function****")
    info(patients)

    ###################### TEST for OPTION 4
    print("\n****TEST the add_new_patient function****")
    patients=add_new_patient(patients)
    display(patients)
    
    ###################### TEST for OPTION 5
    print("\n****TEST the compare function****")
    common_strand=compare(patients[0],patients[1])
    print(common_strand)

    ###################### TEST for OPTION 5
    print("\n****TEST the check_completness function****")
    print(check_completness(common_strand))

    
    
if __name__=="__main__":
    main()
    
