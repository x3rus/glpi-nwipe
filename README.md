== Description ==

French version available here : README-FR.md

This script was originally created when we had to wipe hundred computers and 
update the inventory system (GLPI : http://www.glpi-project.org) with the new status. 

Boot with the  dban cd (http://www.dban.org) and manually updated GLPI, it's ok for 
one or two computer but after ... 

This script should be use with a PXE server, you boot the computer on the network and   
this scripts will :
	- Retrieve the serial with OCS inventory agent (available from the PXE boot)
	- Search for the computer in your GLPI with webservices plugins
	- Ask you to selected the computer (sometime serial number are associate to more than one computer)
	- Update the status of the computer
	- And wipe the Hard drive 

What you need to run this script :
- a DHCP server
- a PXE server  ( it must be a Linux system)
- an NFS server (to provide an OS with the script)
- a GLPI server with webservices-plugins installed.

Big Thanks to ... for the class glpi_client !

== Installation ==

- The DHCP server is not in the scope, but I wrote a little documentation to setup it, maybe it will
 help you , but I'm sure you can find a better documentation on Internet.
	- Setup a DHCP server

- The PXE server, this procedure setup a Debian system bootable with all requirement to run this 
script
	- Setup PXEserver


== Screenshot ===

Yeahh because what ever the features people want to see screenshot :P.



