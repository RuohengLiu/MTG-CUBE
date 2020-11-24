# -*- coding: utf-8 -*-
import os, sys
sys.path.append('./')
reload(sys)
sys.setdefaultencoding('utf-8')
import json

def color_change(color):
    color = color.split(',') if color else []
    if len(color) == 0:
        return 'C'
    if len(color) == 5:
        return 'WUBRG'
    if len(color) == 1:
        return color[0]
    if len(color) == 2:
        for color_combine in ['WU', 'UB', 'BR', 'RG', 'GW', 'WB', 'UR', 'BG', 'RW', 'GU']:
            not_in = False
            for c in color:
                if c not in color_combine:
                    not_in = True
                    break
            if not not_in:
                return color_combine
    if len(color) == 3:
        for color_combine in ['WUB', 'UBR', 'BRG', 'RGW', 'GWU', 'WBG', 'URW', 'BGU', 'RWB', 'GUR']:
            not_in = False
            for c in color:
                if c not in color_combine:
                    not_in = True
                    break
            if not not_in:
                return color_combine
    if len(color) == 4:
        for color_combine in ['WUBR', 'UBRG', 'BRGW', 'RGWU', 'GWUB']:
            not_in = False
            for c in color:
                if c not in color_combine:
                    not_in = True
                    break
            if not not_in:
                return color_combine
    raise


class Card:

    def __init__(self, name, type_line, set_code, set_name, released_at, collector_number, rarity, mana_cost, cmc, colors, color_identity, reserved):
        self.name = name
        self.type_line = type_line
        self.released_at = '/'.join([item.zfill(2) for item in released_at.split('/')])
        self.collector_number = collector_number
        self.colors = color_change(colors)
        self.color_identity = color_change(color_identity)
        self.line = '\t'.join([name, type_line, set_code, set_name, self.released_at, collector_number, rarity, mana_cost, cmc, self.colors, self.color_identity, reserved])+'\n'


def cmp_card(c1, c2):
    color_sort = {
        'W' : 0,
        'U' : 1,
        'B' : 2,
        'R' : 3,
        'G' : 4,
        'WU' : 5,
        'UB' : 6,
        'BR' : 7,
        'RG' : 8,
        'GW' : 9,
        'WB' : 10,
        'UR' : 11,
        'BG' : 12,
        'RW' : 13,
        'GU' : 14,
        'WUB' : 15,
        'UBR' : 16,
        'BRG' : 17,
        'RGW' : 18,
        'GWU' : 19,
        'WBG' : 20,
        'URW' : 21,
        'BGU' : 22,
        'RWB' : 23,
        'GUR' : 24,
        'WUBR' : 25,
        'UBRG' : 26,
        'BRGW' : 27,
        'RGWU' : 28,
        'GWUB' : 29,
        'WUBRG' : 30,
        'C' : 31,
    }
    if c1.color_identity != c2.color_identity:
        if color_sort[c1.color_identity] < color_sort[c2.color_identity]:
            return -1
        else:
            return 1
    elif c1.color_identity == 'C':
        if 'Land' in c1.type_line and 'Land' not in c2.type_line:
            return 1
        if 'Land' in c2.type_line and 'Land' not in c1.type_line:
            return -1
        if 'Creature' in c1.type_line and 'Creature' not in c2.type_line:
            return -1
        if 'Creature' in c2.type_line and 'Creature' not in c1.type_line:
            return 1
        if 'Planeswalker' in c1.type_line and 'Planeswalker' not in c2.type_line:
            return -1
        if 'Planeswalker' in c2.type_line and 'Planeswalker' not in c1.type_line:
            return 1
    if c1.released_at != c2.released_at:
        if c1.released_at < c2.released_at:
            return -1
        else:
            return 1
    else:
        try:
            if int(c1.collector_number) < int(c2.collector_number):
                return -1
            else:
                return 1
        except:
            if int(c1.collector_number[0:-1]) < int(c2.collector_number[0:-1]):
                return -1
            else:
                return 1

if __name__ == '__main__':
    card_list = []
    card_info_file = open('list')
    for line in card_info_file:
        name, type_line, set_code, set_name, released_at, collector_number, rarity, mana_cost, cmc, colors, color_identity, reserved = line.strip('\n').split('\t')
        card_list.append(Card(name, type_line, set_code, set_name, released_at, collector_number, rarity, mana_cost, cmc, colors, color_identity, reserved))
    card_info_file.close()

    card_list = sorted(card_list, cmp_card)
    dst_file = open('sorted_cards', 'w')
    for card in card_list:
        dst_file.write(card.line)
    dst_file.close()
