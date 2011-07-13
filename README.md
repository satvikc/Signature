#Description#
I wondered if it was possible to include some wise quotes at the end of my email signature and then I found this wonderful linux program called "fortune". So here I wrote my own python script which includes a random wise quote at the end of my mutt's signature file.

##Requirements##
You need python3.x , mutt and fortune installed on your system.
Athough the script will work for python 2.7 but I recommend python 3.x for it.
##Variables##
You just nee to change the following Variable:

* SIGNATURE_FILE : Path to your signature file which you usually include in your muttrc file. eg if your signature file is at "~/.mutt/signature" then you should have SIGNATURE_FILE = os.path.expanduser("~/.mutt/signature")
* FORTUNE_COMMAND : fortune command to execute . I only included quotes from the wisdom category , you can use "fortune -f" to see the categories available and add them , eg if you want wisdom and love you can use "fortune -n 200 -s wisdom love" . -n 200 and -s options are to keep quotes short and not to include long quotes. 

##muttrc configuration##
Change the signature line to :
set signature = "python ~/.mutt/Signature.py|"

My script is located at "~/.mutt/Signature.py" . You can change this path to wherever your script is located. Don't forget to add |(pipe) at the end of the path , otherwise this will not be executed. Remember your signature file must not contain anything starting with "" otherwise anything afterthat will be truncated.
