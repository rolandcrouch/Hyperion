#!/bin/bash

# Create 3 folders
mkdir FolderOne FolderTwo FolderThree

# Navigate into FolderOne
cd FolderOne || exit

# Create 3 subfolders
mkdir SubFolder1 SubFolder2 SubFolder3

# Remove 2 subfolders
rm -r SubFolder2 SubFolder3

# Return to original directory
cd ..