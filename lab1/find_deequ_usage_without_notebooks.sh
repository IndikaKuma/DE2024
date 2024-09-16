#!/bin/bash

# Step 1 : create a director deequ and go to it

mkdir deequ
cd deequ

# Step 2: clone Github repositories in repos.txt. Clone into a new directory, say deequ

input="../repos.txt"
while read -r repo; do
  echo "${repo}.git"| git clone $repo
done < "$input"

# Step 3: Merge all Python files into a single file

find . -name '*.py' -exec cat {} \; > all_deequ.py
wc -l all_deequ.py

# Step 4: Count the occurrence of each keyword in the merged Python file. keywords in keywords.txt 
keywords_list="../keywords.txt"
while read -r keyword; do
  grep -oh "$keyword" all_deequ.py | wc -w | awk -v var="$keyword" '{printf "%s:%s\n",var,$1;}' >> ../results_deeque_without_notebooks.txt
done < "$keywords_list"
