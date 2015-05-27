#/usr/bin/python2


###############
## Variables ##
###############

debug=1;
#glpi_server="http://glpi.magrit.int" # "http://goban.x3rus.com/glp"
#glpi_user="adm-tboutry" #adm-glpi"
#glpi_pass="******" #4dmPkPas4dmin

glpi_server="http://goban.x3rus.com/glpi"
glpi_user="adm-glpi"
glpi_pass="4dmPkPas4dmin"

glpi_rebut_state_id='2'

message_to_user="Oupss pas supporser s'afficher contacter l'admin SVP"

#############
## Modules ##
#############
from glpi_client.XMLRPCClient import XMLRPCClient
import commands # juste sous unix
from subprocess import call, check_output
import urwid

from dialog import DialogDisplay

##############
## function ##
##############

# Originalement la fonction retournait le systeme des qu'il le trouvait
# cependant il fut constater que parfois 2 machines ont le meme # de serie :(
def search_serial(serial, list_of_machines):
	lst_system_found=[]
	for system in list_of_machines:
		if 'serial' in system.keys():
			if system['serial'] == serial:
				lst_system_found.append(system)
	return lst_system_found

def menu(title, choices):
	body = [urwid.Text(title), urwid.Divider()]
	for c in choices:
		button = urwid.Button(c)
		urwid.connect_signal(button, 'click', item_chosen, c)
		body.append(urwid.AttrMap(button, None, focus_map='reversed'))
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
	# TODO: faire qqc de plus beau
	# dans la liste des choix j'affiche l'information suivante 
	# id:83673 name:nom_machine contact:Thomas
	# ici je manipule la sting pour extraire la valeur de l'id
	#id_machine_to_update=choice.split()[0].split(':')
	global id_machine_to_update
	id_machine_to_update=choice
	print ("le choix : " + str(choice))
	print (" id  : " + str(id_machine_to_update))
	
	raise urwid.ExitMainLoop()


# connection a GLPI

glpi = XMLRPCClient(glpi_server)
glpi.connect(glpi_user, glpi_pass)

id_machine_to_update=None

# par default limit de 15
# Extraction de l'ensemble des machines dans GLPI avec nom , id et serial
lst_ordis=glpi.listObjects(itemtype='Computer',limit=20000)

# Recuperation du numero de serie de la machine avec le meme outil qu'utilise GLPI
# Execution d'un script c'etait plus simple quelque probleme avec le sudo : p, je strip aussi le retour chariot de la reponse.
SSN_2_WIPE="92OAAQ048009"
#SSN_2_WIPE=check_output(["./get_ssn.sh"]).rstrip('\n')


if debug:
	print ("Le numero de serie a wipe est : " )
	print ("|"+SSN_2_WIPE+"|")


#### recherche numero de serie dans la liste des machines ####
ordi2wipe=search_serial(SSN_2_WIPE,lst_ordis)

if ordi2wipe != None :


	if debug:
		print (10 * "-")
		print ("Machine trouver  :P ")
		print (ordi2wipe)

	lst_machine_menu=[]
	for machine in ordi2wipe:
		info=glpi.getObject(itemtype='Computer',id=machine['id'])
		msg_ordi='id:' + info['id'] + " "
		msg_ordi+='nom:' + info['name'] + " "
		msg_ordi+='contact:' + info['contact'] + " "
		lst_machine_menu.append(msg_ordi)
	
	if debug:
		print (5 * "-")
		print (lst_machine_menu)


	# Affiche le menu 
	main = urwid.Padding(menu(u'Selectionnez le systeme', lst_machine_menu), left=2, right=2)
	top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
	align='center', width=('relative', 60),
	valign='middle', height=('relative', 60),min_width=20, min_height=9)
	urwid.MainLoop(top, palette=[('reversed', 'standout', '')]).run()
		
	if debug:
		print ("numero machine choisi : ")
		print (id_machine_to_update)

	# id_machine_to_update ressemble a 
	# print id_machine_to_update ==  id:2 nom:goban contact:xerus
	# extraction de l'id
	id_machine_selected=id_machine_to_update.split(" ")[0].split(":")[1]
	#### recuperation information machine ####
	info_ordi2wipe=glpi.getObject(itemtype='Computer',id=id_machine_selected)

	if debug:
		print (10 * "-")
		print (info_ordi2wipe )


	#### Modification de la machine dans GLPI
	# Objectif modifier l'ordi pour que le state id soit  'states_id': '16'.
	params= {
	        'Computer': [
	            {
	            'id': info_ordi2wipe['id'],
	            'states_id': glpi_rebut_state_id,
	            }
		]
	}


	update_result=glpi.updateObjects(fields=params)
	if update_result != None:
		message_to_user="Le numero de serie : " + SSN_2_WIPE + " \n"
		message_to_user+="L'etat de la machine fut mis a jour sur le serveur : " + glpi_server + "\n"
		message_to_user+="Est-ce que nous procedons avec la suppression du/des disque(s) ? \n" 
	else:
		message_to_user="Le numero de serie : " + SSN_2_WIPE + " \n"
		message_to_user+="ERREUR >> L'etat de la machine ne fut PAS  mis a jour sur le serveur : " + glpi_server + "\n"
		message_to_user+="un probleme est survenu , peut-etre un probleme de droit ou le script !"
		message_to_user+="Est-ce que nous procedons avec la suppression du/des disque(s) ? \n" 
	
		
else:
	message_to_user="Le numero de serie : " + SSN_2_WIPE + " \n"
	message_to_user+="ERREUR >> Ne fut PAS trouver sur le serveur GLPI : " + glpi_server + "\n"
	message_to_user+="Ceci est soit un problem ou la machine n'est pas dans GLPI \n\n"
	message_to_user+="Est-ce que nous procedons avec la suppression du/des disque(s) ? \n" 

	print (message_to_user)

	

# END if ordi2wipe != null

mydialog=DialogDisplay(message_to_user,0,0);

mydialog.add_buttons([    ("Yes", 0), ("No", 1) ])


# Run it
exitcode, exitstring = mydialog.main()

if exitcode == 0 :
	print (" KILL nwipe !!!" )
	mydialog=DialogDisplay("Kill Wipe ",0,0)
	mydialog.add_buttons([    ("OK", 0) ])
	mydialog.main()
	call(["reset"])
	# call(["nwipe","--autonuke"])
else:
	mydialog=DialogDisplay("Vous avez choisi de ne pas wiper la machine cette derniere sera donc eteinte , MERCI",0,0)
	mydialog.add_buttons([    ("OK", 0) ])
	mydialog.main()
	call(["reset"])
	#call(["shutdown","-h now"])

# END
