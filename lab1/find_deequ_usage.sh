#!/bin/bash

# Step 1: install nbconvert library that can be used to covert jupyter notebooks to Python files

sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt install python3-dev python3-pip python3-venv -y
 # Only create a virtual envrioment if it does not exist
if [ ! -d ".venv" ]; then
  python3 -m venv .venv 
fi

. .venv/bin/activate  # for why . instead of source see https://stackoverflow.com/questions/13702425/source-command-not-found-in-sh-shell
pip install nbconvert

# Step 2: create a director deequ and go to it
mkdir deequ
cd deequ

# Step 3: clone Github repositories in repos.txt

input="${1:-"../repos_subset.txt"}"  # Getting the repos lit from your input - the default value is ../repos_subset.txt
while read -r repo; do
  echo "${repo}.git"| git clone $repo
done < "$input"
              
# Step 4: Get the paths of all jupyter notebooks 
find . -name '*ipynb' > "notebooks.txt" 


# Step 5: Convert jupyter notebooks to  python files

while read -r file; do
  jupyter nbconvert --to script $file
done < "notebooks.txt"

# Step 6: Merge all Python files into a single file

find . -name '*.py' -exec cat {} \; > all_deequ.py
wc -l all_deequ.py

# Step 7: Count the occurrence of each keyword in the merged Python file. keywords in keywords.txt 

keywords_list="../keywords.txt"
while read -r keyword; do
  grep -oh "$keyword" all_deequ.py | wc -w | awk -v var="$keyword" '{printf "%s:%s\n",var,$1;}' >> ../results_deeque.txt
done < "$keywords_list"