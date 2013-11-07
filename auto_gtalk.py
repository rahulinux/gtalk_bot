#!/usr/bin/env python
# -*- conding: UTF-8 -*-
import re
import xmpp
 
user="daily.server.report@gmail.com"
password=''


notondesk = """ Sorry dear, I am away from my desk...
		I'll be back later"""

diwali = 'happy\s*(diwali|dipawli|dipawali)(\s*|)'
def reply_diwali():
	return """l''l________
--/ l__l Delivery
| | ________
L(o)__l___(o)__|
This van is loaded with
LOVE n CARE,
Wishing U and your family
A HAPPY DIWALI"""

 
hi = '(hi|hello)'
def reply_hi():
	return "Yes tell me..."

thanks = '(thanks|thank you|thnx|10q|thank|thx|thank u)'
def reply_thanks():
	return "You are always welcome..."

how_are_you = '(how|hw)\s+(are|r)\s+(you|u)(\s*|)(\?+|\s+|)'
def reply_howareyou():
	return "I'm fine. thanks yaar.., what about you?"

buzy = '(are|r)\s+(u|you)\s+(buzy|busy)(\s*|)(\?+|\s+|)'
def reply_buzy():
	return """Yes, Little bit...
		catch you soon"""

fine = "(i m|im|i\'m|m|\s+|)(\s+|)(fine|good|f9|gud)(\s+|)"
def reply_fine():
	return "dats gud.."

smily = '(ha ha|:-\)|:\))'
def reply_smile():
	return ";D lol"

cry = "(:-\(|:\()"
def reply_cry():
	return "what happen dear?"

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
            match(smily,msg)	   : reply_smile(),
            match(cry,msg)	   : reply_cry(),
            match(diwali,msg)	   : reply_diwali(),
            match(thanks,msg)	   : reply_thanks(),
            match(hi,msg)	   : reply_hi()
            }.get(msg,notondesk)
        return action
    except KeyError:
	pass



def message_handler(connect_object,message_node):
	message = str(message_node.getBody()).lower()
	if message != "none":
		print message
		reply = chat_reply(message)
		print reply
		connect_object.send( xmpp.Message( message_node.getFrom(),reply))

 
jid = xmpp.JID(user)
#connection = xmpp.Client(server,debug=[])
connection = xmpp.Client(server)
connection.connect()

result = connection.auth(jid.getNode(), password, "Pythonista!!")
connection.RegisterHandler('message', message_handler)
 
connection.sendInitPresence()
 
while connection.Process(1):
    pass
