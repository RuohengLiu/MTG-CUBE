import os, sys
import requests
import json

# card_name = "Jace, Vryn's Prodigy"
card_name = "Uro, Titan of Nature's Wrath"

url = "https://api.scryfall.com/cards/search"
def fetch_card_info(card_name):
    params = { "q" : card_name, "unique" : "prints", "order" : "released" }
    res_data = requests.get(url, params=params)
    card_info = json.loads(res_data.text)
    ret = []
    for card in card_info['data']:
        if not card['reprint']:
            s = ''
            s += card['name']
            s += '\t0'
            s += '\t'+(''.join(card['color_identity']) if card['color_identity'] else 'C')
            s += '\t'+card['type_line']
            s += '\t'+card['set']
            s += '\t'+card['set_name']
            s += '\t'+card['released_at']
            s += '\t'+str(card['collector_number'])
            s += '\t'+card['rarity']
            s += '\t'+str(card['cmc'])
            s += '\tTrue' if card['reserved'] else '\tFalse'
            s += '\n'
            ret.append(s)
    return s

src_file = open('cards/names')
dst_file = open('cards/card_infos', 'w')
for line in src_file:
    ret = fetch_card_info(line.strip())
    for s in ret:
        dst_file.write(s)
src_file.close()
dst_file.close()
