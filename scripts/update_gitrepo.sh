#!/bin/bash

#
# update git repo batches
#
#

for i in `ls .`;
do
    if [ -d $i ]; then
        if [ -d "./$i/.git" ]; then
            pushd ./$i/
            git pull
            popd
            continue
        fi
        for j in  `ls ./$i`;
        do
            if [ -d "./$i/$j" ]; then
                echo '======================='
                echo ./$i/$j
                echo '======================='
                if [ -d "./$i/$j/.git" ]; then
                    pushd ./$i/$j/
                    git pull
                    popd
                    continue
                fi
            fi
        done
    fi
done
