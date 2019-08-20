import re
import os

from fbchat import Client
from fbchat.models import Message

from roller import buildResponse

class Roll20Bot(Client):
  def __init__(self,username,password):
    super().__init__(username,password)

  def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
    if '!!roll' in message_object.text.lower():
      responseContent = buildResponse(message_object.text)
      self.send(message=Message(text=responseContent),thread_id=thread_id, thread_type=thread_type)

if __name__ == "__main__":
    YOUR_FACEBOOK_USERNAME = ""
    YOUR_FACEBOOK_PASSWORD = ""

    with open('credentials.txt') as fyl:
        YOUR_FACEBOOK_USERNAME = fyl.readline().strip()
        YOUR_FACEBOOK_PASSWORD = fyl.readline().strip()

    client = Roll20Bot(YOUR_FACEBOOK_USERNAME, YOUR_FACEBOOK_PASSWORD)
    client.listen()
