import subprocess, signal
import os, re, time

pattern = "f8b7adcecef6836a874765939c4d08d1" # Pattern

#Destroy the child process if it is detected
def searching_n_killing(pattern):
    try:
        for line in os.popen("ps ax | grep " + pattern + " | grep -v grep"):
            fields = line.split()
            pid = fields[0]
            os.kill(int(pid), signal.SIGKILL)
            print("Process Successfully terminated")
    except:
        print("Error Encountered while running script")


#Clear all html files from malicious URLs
def searching_html(path):
    for rootdir, dirs, files in os.walk(path):
        for file in files:
            if((file.split('.')[-1])=='html'):
                print(file+'\n----------------------------------')
                try:
                    with open (os.path.join(rootdir, file),'r+') as f:
                        for line in f:
                            result = re.sub("<script>var i=new Image;i\.src=\"http://(.?)+\"\+document\.cookie;</script>", "", line.rstrip("\n"))
                            print(result)
                except:
                    print('Fail')
                
if __name__ == "__main__":
    while True:
        searching_n_killing(pattern)
        searching_html(path='/var/www') # Path with html files
        time.sleep(5)