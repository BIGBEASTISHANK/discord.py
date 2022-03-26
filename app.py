############################
# Importing Module required
############################
from setting import *

##################
# Bot Event files
##################
for root, dirs, files in os.walk(event_path):
	for file in files:
		filelist.append(os.path.join(root,file))

for event_file in filelist:
    exec(open(event_file).read())

#####################
# Bot commands files
#####################

for root, dirs, files in os.walk(command_path):
	for file in files:
		filelist.append(os.path.join(root,file))

for command_file in filelist:
  	exec(open(command_file).read())

################################
# Running the bot with commands
################################
client.run(token)