import os,sys,subprocess
SIGNATURE_FILE=os.path.expanduser("~/.mutt/sig")
FORTUNE_COMMAND="fortune -n 200 -s wisdom"
def delete_previous():
    fp  = open(SIGNATURE_FILE,"r")
    lines = fp.readlines()
    fp.close()
    fp = open(SIGNATURE_FILE,"w")
    for line in lines:
        if line.startswith('\"\"'):
            break
        fp.write(line)
    fp.close()
        
def add_quote():
    x=subprocess.getstatusoutput(FORTUNE_COMMAND)
    if x[0]==0:
        delete_previous()
        fp = open(SIGNATURE_FILE,"a")
        fp.writelines("\"\" "+x[1]+" \"\"")
        fp.close()
        print_signature()
    else:
        print("Some problem with the fortune program ,, see if it is installed")
        exit(-1)
def print_signature():
    fp = open(SIGNATURE_FILE,"r")
    lines=fp.readlines()
    fp.close()
    print(''.join(lines))
if __name__=='__main__':
    add_quote()
