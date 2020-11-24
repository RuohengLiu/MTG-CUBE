# -*- coding: utf-8 -*-
import os, sys
sys.path.append('./')
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import json

card_name = "Jace, Vryn's Prodigy"
# card_name = "Snapcaster Mage"

try:
    url = "https://api.scryfall.com/cards/search?q=%21"+card_name.replace(',', '%2C').replace(' ', '%22').replace("'", '%27')+"&unique=prints&order=released"
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    card_info = json.loads(res_data.read())
    for card in card_info['data']:
        if not card['reprint']:
            s = card['name']+'\t'+card['type_line']+'\t'+card['set']+'\t'+card['set_name']+'\t'+card['released_at']+'\t'+str(card['collector_number'])+'\t'+card['rarity']+'\t'+card['mana_cost']+'\t'+str(card['cmc'])
            s += '\t'+','.join(card['colors'])
            s += '\t'+','.join(card['color_identity'])
            if card['reserved']:
                s += '\tTrue'
            else:
                s += '\tFalse'
except:
    url = "https://api.scryfall.com/cards/named?fuzzy="+card_name.replace(',', '').replace(' ', '%22').replace("'", '')
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req)
    card = json.loads(res_data.read())
    if not card['reprint']:
        s = card['card_faces'][0]['name']+'\t'+card['card_faces'][0]['type_line']+'\t'+card['set']+'\t'+card['set_name']+'\t'+card['released_at']+'\t'+str(card['collector_number'])+'\t'+card['rarity']+'\t'+card['card_faces'][0]['mana_cost']+'\t'+str(card['cmc'])
        s += '\t'+','.join(card['card_faces'][0]['colors'])
        s += '\t'+','.join(card['color_identity'])
        if card['reserved']:
            s += '\tTrue'
        else:
            s += '\tFalse'

print s
