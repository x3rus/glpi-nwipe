== Description ==

French version available here : README-FR.md

This script was originaly created when we had to wipe hundred computers and 
update the inventory system GLPI (URL-project) with the new status. 

We used the  dban cd (URL-project) for one or two computer it's ok , and manually updated the
GLPI web site. I use the glpi webservice plugins (URL) to communicate with the GLPI installation.

This script should be use with a PXE server, you boot the computer on the network and   
this scripts will :
	- Retrieve the serial with OCS inventory agent
	- Search for the computer in your GLPI installation (URL) 
	- Ask you to selected the computer (sometime serial number are associate to more than one computer)
	- Update the status of the computer
	- And wipe the Hard drive 

What you need to run use this script :
- a DHCP 
- a PXE server  ( it must be a Linux system)
- a GLPI server with webservices-plugins installed.

Big Thanks to ... for the classe glpi_client !

== Installation ==

- The DHCP server is not in the scope, but I wrote a little documentation to setup it, maybe it will
 help you , but I'm sure you can find a better documentation on Internet.
	- Setup a DHCP server

- The PXE server, this procedure setup a Debian system bootable with all requirement to run this 
script
	- Setup PXEserver

- Script installation and Configuration of the script 

== Screenshot ===

Yeahh because what ever the features people want to see screenshot :P.



