#!/usr/bin/env python3
"""
Exemple pédagogique : comprendre ce qui est signé par Technocore.

Ce script ne publie rien. Il montre uniquement la construction
du message qui doit être signé selon la documentation officielle.

Source :
https://github.com/flop-labs/technocore-chat
"""

room = "lobby"
nonce = "1234567890"
text = "Bonjour Technocore !"

# Technocore documente la chaîne signée sous la forme :
# <room>|<nonce>|<text>
message_to_sign = f"{room}|{nonce}|{text}"

print("Chaîne signée :")
print(message_to_sign)
