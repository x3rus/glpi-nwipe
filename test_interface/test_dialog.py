#!/usr/bin/python2
#
##################################


from dialog import DialogDisplay 

mydialog=DialogDisplay("nous avons trouvez la machine \n toto ",0,0);

mydialog.add_buttons([    ("Yes", 0), ("No", 1) ])


# Run it
exitcode, exitstring = mydialog.main()
