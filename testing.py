from HomeLLM import initializeModel, initializeChatHistory, sendMessage, loopConversation

import logging
import sys

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, stream=sys.stdout, force=True)


def testBasicMessagingFunctionality(msg="Hi, how are you doing?"):
    model = initializeModel()
    chat_history = initializeChatHistory()
    print("\n Initial Chat History:")
    print(chat_history)
    response, chat_history = sendMessage(model, chat_history, msg)

    print("\n Subsequent Chat History:")
    print(chat_history)

    print("\n Response:")
    print(response.content)

def testInitialChatHistoryMessageGeneration():
    model = initializeModel()
    chat_history = initializeChatHistory(chat=model,generateInitialMessage=True)
    print("\n Generated initial chat history:")
    print(chat_history)

def testConversationLoop(msg="What's your name?"):
    model = initializeModel()
    loopConversation(model, msg,verbose=True,logger=logger,breakTimeThreshold=8)
    print("conversation loop exited")


#testBasicMessagingFunctionality()
#testInitialChatHistoryMessageGeneration()
testConversationLoop()



#### PLAYGROUND

#model = initializeModel()
#chat_history = initializeChatHistory()
#response, chat_history = sendMessage(model, chat_history, "Hi, who is this?")
#print(chat_history.messages[0])
