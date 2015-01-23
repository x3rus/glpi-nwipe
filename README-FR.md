== Description ==

Version anglaise disponible ici : README.MD

Le script fut developpe a l'origine car nous renouvellions l'ensemble de notre parc informatique 
resultat un nombre important de machine dut etre formater proprement (wipe) , de plus nous devions
mettre a jour l'inventaire (GLPI : URL-PROJECT) .

Nous utilisions un cd de dban (URL) pour le formatage et realisions la mise a jour manuellement sur le serveur GLPI. Pour un ou deux  ordinateurs a la fois ceci est convenable mais pas pour un nombre important.

Le script glpi-nwipe devrait etre utilise avec un serveur PXE afin de permettre a plusieurs machine de demarrer sur le reseaux et de realiser l'operation de mise a jour de l'inventaire et de formatage. Le script realise les operations suivantes:
	- Recuperation du numero de serie ( utilisation de OCSinventory agent)
	- Recherche de l'ordinateur dans GLPI grace au plugin webservice
	- Demande de selection de l'ordinateur / confirmation ( il est arrive qu'un numero de serie soit assigner a plus d'une machine)
	- Mise a jour de son status
	- Formatage propre de la machine


Les requis pour utiliser le script :
	- Un serveur DHCP
	- Un serveur PXE  ( ce doit etre un Linux)
	- Un serveur GLPI avec le plugin des webservices

Un Gros merci a .... pour la classe glpi_client !


== Installation ==

-  Le serveur  peut etre n'importe quoi l'important et surtout de pouvoir configurer les options 
suivante : 
Si vous n'avez pas de serveur DHCP ou que vous desiriez tous definir sur la meme machine voici une documetation , en anglais, que j'ai realise. Il y a probablement mieux mais ceci vous offre un point de depart.
	- Setup a DHCP server

- Le serveur PXE, la procedure configure un systeme Debian bootable avec l'ensemble des utilitaires requis pour l'utilisation du scripts. La documentation est ausssi en anglais.
        - Setup PXEserver

- Installation et configuration du script.

== Screenshot ===

Et Oui , car peut importe la listes des fonctionnalites identifies les personnes veulent savoir sa
 c'est beau !!! Non c'est pas tres beau mais ca fonctionne bien :P.

