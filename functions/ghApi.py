import os
from shutil import copyfile


def gh_repo(projectname, filePath,appdir):
    os.system(f'gh repo create {projectname}')
    os.chdir(filePath)
    open('README.md', 'w')
    print(os.listdir())
    # # CEfr = filePath + '/.git/COMMIT_EDITMSG'
    # CEf = filePath + '/.git/COMMIT_EDITMSG'
    # CEfm = appdir + '/functions/COMMIT_EDITMSG'
    # # os.remove(CEfr)
    # # copyfile(CEfm, CEf)
    # # os.system('git commit -a --force')
    # # copyfile(CEfm, CEf)
    # os.system('git commit --all')
    # os.system('git-add README.md')
    # # os.system('git-add README.md')
    # os.system('git commit -a')
    # os.system('git push --all')
    # # os.system('git fetch origin master')
    # # os.system('git merge origin master')