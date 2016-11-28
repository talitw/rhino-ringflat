#!/bin/bash

install_path="$HOME/Library/Application Support/McNeel/Rhinoceros/MacPlugins/PythonPlugins/RingFlat{c079b327-5ac5-4133-8ca6-5909661ac833}/dev"
mkdir -p "$install_path"
cp RingFlat_cmd.py "$install_path"
