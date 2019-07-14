#!/bin/bash

helpFunction()
{
   echo "Function usage"
   echo "Usage: rename [oldname]  [newname] "
   echo -e "\tOld name of the branch"
   echo -e "\tNew name of the branch"
}

rename(){
    RED='\033[0;31m'
    NONE='\033[0m'
    GREEN='\033[0;32m'    
    if [ -z "$1" ] || [ -z "$2" ]
    then
        helpFunction
        return
    fi
    if git show-ref -q --heads $1 && ! git show-ref -q --heads $2; then
        git branch -m $1 $2
        git push origin :$1 $2
        git push origin -u $2
        echo -e "${GREEN}Rename complete${NONE}"
    fi
    echo -e "Invalid branch name ${RED}$1${NONE} and ${RED}$2${NONE}"
}

push(){
    protected=('develop' 'master')
    branch=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)
    if [ "$1" = "-f" ]; then
        echo "Good luck"
        git add . && git commit --amend --no-edit &&git push -f
    elif [[ " ${protected[*]} " != *" $branch "* ]];then
        echo 'Pushing to branch' $branch 
        git add . && git commit --amend --no-edit &&git push -f
    else
        echo "You are pushing to a protected branch ${branch}"
    fi
}
