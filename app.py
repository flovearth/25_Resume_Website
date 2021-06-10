import os

## Number of days you want to make commits
for i in range(1,200,9):
    d = str(i) + ' check the code tasks to be done:'
    ## Open a text file and modify it
    with open('Stage3Updates.txt', 'a') as file:
        file.write(d+'\n')
    ## Add CodeTasksToDo.py to staging area
    os.system('git add StageUpdates.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "Stage 1-2 changes applied."')

## push the commit to github
os.system('git push')