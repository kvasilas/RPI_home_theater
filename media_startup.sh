#!/bin/bash

start_dir=`pwd`

file_addr='/home/greenport/documents/RPI_home_theater/'
cd $file_addr
git pull
sleep 1
python3 rpi_gui.py

cd start_dir
