'''------------------------------------------------------
                 Import Modules 
---------------------------------------------------------'''
import dna_tool as dna

'''------------------------------------------------------
                Main program starts here 
---------------------------------------------------------'''
print("==========================================")
print('DNA "Analyzer" and Patient Management Tool')
print("==========================================")
list_pat=dna.initialize()
condition=[]
percent=[]
while True:
    dna.display_menu()
    command= input("Command (Enter to exit): ")
    if command=="": #breaks out of the loop when they press enter
        print("\nThanks for using this tool")
        print("Come back soon!")
        break
    elif command=="1":#displays the list of Patients
        dna.display(list_pat,condition)
    elif command=="2":#prints out list
        dna.info(list_pat,condition,percent)
    elif command=="3":#deleted patient if correct number is input
        num=int(input("Who do you want to remove (enter number): "))
        if not(1<=num<=len(list_pat)):
            continue
        del(list_pat[num-1])
    elif command=="4":#calls function to add new patient
        dna.add_new_patient(list_pat)
    elif command=="5":#checks to see if correct number is input then calls functions and prints
        num1=int(input("First patient (enter number): "))
        num2=int(input("Second patient (enter number): "))
        if not(1<=num1<=len(list_pat)):
            continue
        if not(1<=num2<=len(list_pat)):
            continue
        strand=dna.compare(list_pat[num1],list_pat[num2])
        print("Patients",num1,"and",num2,"common strand is "+strand)
        print("They are similar at "+str(dna.check_completness(strand))+"%")
    elif command=="6":
        dna.compare_all(list_pat)
    elif command=="7":
        condition+=[(str(input("Which condition are you looking for: ")))]
        seq=str(input("Enter sequence: "))
        percent+=[dna.find_pattern(list_pat,seq)]
        print("Patients with the "+condition[-1]+" condition: "+str(percent[-1])+"%")