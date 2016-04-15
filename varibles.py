#get input 
name = raw_input("Name? >")
age = raw_input("Age? >")
whatever = raw_input("Shoutout? >")

#checks if strigs are empty
if name == " " and age == " " and wahtever == " ":
    print "STOP HAMMA TIME"
else:
    #if strings NOT empty:
    print "YO NAME IS %s AND YO AGE IS %s AND YO WOUL LIKE TO SAY %s!!!!!" % (name, age, whatever)
    raw_input()
