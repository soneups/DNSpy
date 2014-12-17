#!/bin/bash

clear
date
echo ""
echo "NS records for example.net"
echo "----------------------------------"
python ns.py NS example.net
echo  
echo "MX records for example.net"
echo "----------------------------------"
python ns.py MX example.net
echo  
echo "MX records for subd.example.net"
echo "----------------------------------"
python ns.py MX subd.example.net
