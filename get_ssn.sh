#!/bin/bash
#
###############################

sudo /usr/bin/ocsinventory-agent ocsinventory-agent --stdout 2>/dev/null | grep "<SSN>" | sed 's/\s*<SSN>\(.*\)<\/SSN>/\1/'
