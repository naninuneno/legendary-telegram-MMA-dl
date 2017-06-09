call python navigateToVideo.py %1 %2 > store.txt

set /p firsturl= < store.txt

call slimerjs fetchVideoUrl.js "%firsturl%" > store.txt

for /F "delims=" %%a in (store.txt) do (
   set "videourl=%%a"
)

set vidname= %1_%2.mkv

call ffmpeg -i "%videourl%" -c copy %vidname%