from datetime import datetime
import gedcom
divdate=[]
mardate=[]
def US4MbD():
    print("USER STORY 04")
    for k,i in gedcom.FAMs.items():
        divdate=i.divorced
        mardate=i.married
        #print(divdate)
        if i.divorced != 'N/A':
            
            if i.divorced < i.married:
                print('error')
            else:
                print("everything is fine. No divorce before marriage")
