#/usr/bin/python2

from glpi_client.XMLRPCClient import XMLRPCClient

glpi = XMLRPCClient('http://goban.x3rus.com/glpi')
glpi.connect("adm-glpi", "4dmPkPas4dmin")



ordi=glpi.getObject(
        itemtype='Computer',
        id=1,
)


print ordi

