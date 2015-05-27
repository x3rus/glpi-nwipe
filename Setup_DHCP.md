== Description ==

A basic dhcp setup, it's not the best tutorial on Internet but it will give you a start.

I will setup a DHCP server for the network 192.168.10.0/24.
The PXEServer have the IP : 192.168.10.5.
DNS server : 192.168.10.10

I tested it on a Centos 6

== Installation ==

* Install dhcp package 
	$ sudo yum install dhcp

* Configure the dhcp , /etc/dhcp/dhcpd.conf 

# specify your domain name 
option domain-name "example.com"

# specify name server's hostname or IP address
# Use your internal DHCP server
option domain-name-servers  192.168.10.10

# default lease time
default-lease-time 600;

# max lease time
max-lease-time 7200;

# this DHCP server to be declared valid
authoritative;

# specify network address and subnet mask
subnet 192.168.10.0 netmask 255.255.255.0 {
   
	# specify the range of lease IP address
	range dynamic-bootp 192.168.10.200 192.168.10.254;
   
	# specify broadcast address
	option broadcast-address 192.168.10.255;
   
	# specify default gateway
	option routers 192.168.10.1;
}

* start service and enable it when system boot
	sudo /etc/rc.d/init.d/dhcpd start
	sudo chkconfig dhcpd on 

* That's the basic setup , now enable configuration for the PXE server. Edit again 
the file 
and change subnet definition with those 3 lignes:

subnet 192.168.10.0 netmask 255.255.255.0 {

        # specify the range of lease IP address
        range dynamic-bootp 192.168.10.200 192.168.10.254;

        # specify broadcast address
        option broadcast-address 192.168.10.255;

        # specify default gateway
        option routers 192.168.10.1;

	# PXE configuration
	filename "pxelinux.0";
	next-server 192.168.10.5;
	option root-path "192.168.10.5:/pxeroot";
}

* Of course restart DHCP server. 

* Now configure the PXE serveur 
Setup_PXEserver.md

== Reference ==
* http://www.server-world.info/en/note?os=CentOS_6&p=dhcp
* https://www.howtoforge.com/pxe_booting_debian
