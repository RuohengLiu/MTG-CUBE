# -*- coding: UTF-8 -*-
import os, sys
import requests
import json
# Orcish Lumberjack 0 GR Creature — Orc ice Ice Age 1995-06-03 210 common 1.0 False
src_file = open('cards/card_all_infos')
dst_file = open('cards/zhs_card_names', 'w')
for line in src_file:
    name, collected, color_identity, type_line, set_code, set_name, released_at, collector_number, rarity, cmc, reserved = line.strip('\n').split('\t')
    url = 'https://api.scryfall.com/cards/'+set_code+'/'+collector_number+'/zhs'
    while True:
        try:
            res_data = requests.get(url)
            break
        except:
            print(name)
            continue
    card_info = json.loads(res_data.text)
    if 'name' not in card_info or 'printed_name' not in card_info:
        dst_file.write(name + '\t\t' + '\t'.join(line.strip('\n').split('\t')[1::]) +'\n')
    else:
        dst_file.write(name + '\t' + card_info['printed_name'] + '\t' + '\t'.join(line.strip('\n').split('\t')[1::]) +'\n')
    dst_file.flush()
