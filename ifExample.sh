#!/bin/bash

# Check if new_folder exists
if [ -d "new_folder" ]; then
    mkdir if_folder
fi

# Check if if_folder exists
if [ -d "if_folder" ]; then
    mkdir hyperionDev
else
    mkdir new-projects
fi