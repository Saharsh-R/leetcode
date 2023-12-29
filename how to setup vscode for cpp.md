# The following resources were helpful.

https://www.youtube.com/watch?v=Qw5qjRNlC-Y
https://stackoverflow.com/a/53995912

Add the following to the vscode json
```
"code-runner.executorMap":{
    "cpp": "cd $dir && g++ -std=c++17 $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
},
```