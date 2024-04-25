from HomeLLM import loopConversation, initializeModel

import logging
import sys

logger = logging.getLogger("HomeLLM")
logging.basicConfig(level=logging.INFO, stream=sys.stdout, force=True)


def startCommandLineMode():
    chat = initializeModel()
    while True:
        cmd = ""
        inp = input("Activate convo? y/n/exit ")
        if inp == "y":
            inp = input("Initial command? y/n ")
            if inp == "y":
                cmd = input("Enter initial command: ")
            loopConversation(chat,cmd,logger=logger,breakTimeThreshold=10)
        else:
            if inp == "exit":
                break

startCommandLineMode()