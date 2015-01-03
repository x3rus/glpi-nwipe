#!/usr/bin/python2
#
##################################


from dialog import DialogDisplay 
toto=['aji modele h1000e','goban modele clone']
mydialog=DialogDisplay("nous avons trouvez la machine \n ",0,0, toto);

mydialog.add_buttons([    ("Yes", 0), ("No", 1) ])


# Run it
exitcode, exitstring = mydialog.main()
