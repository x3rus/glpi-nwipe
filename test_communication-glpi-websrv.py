#/usr/bin/python2

from glpi_client.XMLRPCClient import XMLRPCClient

glpi = XMLRPCClient('http://goban.x3rus.com/glpi')
glpi.connect("adm-glpi", "4dmPkPas4dmin")



ordi=glpi.listObjects(
        itemtype='Computer',
	serial='92OAAQ048009x2',
)

print ordi

print 10 * "-"
ordi=glpi.listInventoryObjects(
	serial='92OAAQ048009',
)
print ordi

#ordi=glpi.getObject(
#        itemtype='Computer',
#        id=1,
#)


