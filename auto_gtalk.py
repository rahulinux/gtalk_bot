#!/usr/bin/env python
import re
import xmpp
 
user="loginrahul90@gmail.com"
password=''
server="gmail.com"


notondesk = """ Sorry,deary I am away from my desk...
		I'll be back later"""

 
hi = '(hi|hello)'
def reply_hi():
	return "Yes tell me..."

how_are_you = '(how|hw)\s+(are|r)\s+(you|u)(\?+|\s+|)'
def reply_howareyou():
	return "I'm fine. thanks yaar.., what about you?"

buzy = '(are|r)\s+(u|you)\s+(buzy|busy)(\?+|\s+|)'
def reply_buzy():
	return """Yes, Little bit...
		catch you soon"""

fine = "(im|i\'m|m|\s+|)(\s+|)(fine|good|f9|gud)(\s+|)"
def reply_fine():
	return "dats gud.."

def match(regex,msg):
    mo = re.match(regex,msg)
    try:
	return mo.group()
    except AttributeError:
	pass
	 

def chat_reply(msg):
    try:
        action = {
            match(how_are_you,msg) : reply_howareyou(),
            match(buzy,msg)	   : reply_buzy(),
            match(fine,msg)	   : reply_fine(),
            match(hi,msg)	   : reply_hi()
            }.get(msg,notondesk)
        return action
    except KeyError:
	pass
        #return "what was that?"



def message_handler(connect_object,message_node):
	message = str(message_node.getBody()).lower()
	#print match(how_are_you,message)
	if message != "none":
		print message
		reply = chat_reply(message)
		print reply
		connect_object.send( xmpp.Message( message_node.getFrom(),reply))
	#elif "are you busy" in msg or "r u buzy" in msg or "are you buzy" in msg or "busy" in msg:
	#    reply = """yes.. litle bit.
	#         catch you soon"""
	#       connect_object.send( xmpp.Message( message_node.getFrom() ,reply))


 
jid = xmpp.JID(user)
connection = xmpp.Client(server)
connection.connect()
result = connection.auth(jid.getNode(), password, "LFY-client")
connection.RegisterHandler('message', message_handler)
 
connection.sendInitPresence()
 
while connection.Process(1):
    pass
