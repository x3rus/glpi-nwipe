#/usr/bin/python2

from glpi_client.XMLRPCClient import XMLRPCClient


def search_serial(serial, list_of_machines):
    return [element for element in list_of_machines if element['serial'] == serial]

glpi = XMLRPCClient('http://goban.x3rus.com/glpi')
glpi.connect("adm-glpi", "*****")


# par default limit de 15
# toto=glpi.listObjects(itemtype="Computer",start=1,limit=20000)

lst_ordis=glpi.listObjects(
        itemtype='Computer',
)

print 10 * "-"
print lst_ordis 

# Pour extraire l'info du systeme
#$ sudo  ocsinventory-agent --stdout | grep -i --color SSN
#[info] [download] Agent is running in local mode...disabling module
#Disk /dev/md2 doesn't contain a valid partition table
#Disk /dev/md1 doesn't contain a valid partition table
#      <SSN>A7 06 02 00 FF FB EB BF</SSN>
#      <CMD>grep -i --color SSN</CMD>
##
## sudo  ocsinventory-agent --stdout 2>/dev/null | grep "<SSN>" | sed 's/\s*<SSN>\(.*\)<\/SSN>/\1/'
##

ordi2wipe=search_serial('92OAAQ048009',lst_ordis)

print 10 * "-"
print ordi2wipe


