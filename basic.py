import sys
from chatgpt_wrapper import ChatGPT

bot = ChatGPT()


def ask_chatgpt(message):
    return bot.ask(message)


response = ask_chatgpt(sys.argv[1])
print(response)
