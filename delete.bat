cd PATH_TO_YOUR_REPO

REM -- Variable declerations
set "textFile=tempBranchInfo.txt"
set "branchToKeep=master"
set "branchToReplaceWith="
git branch --merged > %textFile%

REM -- remove "master" from list to keep the branch
for /f "delims=" %%i in ('type "%textFile%" ^& break ^> "%textFile%" ') do (
    set "line=%%i"
    setlocal enabledelayedexpansion
    >>"%textFile%" echo(!line:%branchToKeep%=%branchToReplaceWith%!
    endlocal
)

REM -- execute branch delete commands
for /f "delims=" %%a in (%textFile%) do (
    git branch -D %%a
)

REM -- remove temp-file with branch information inside
DEL %textFile%

REM -- show local branches after the cleaning
echo Local branches:
git branch

pause 
exit