# -*- coding: utf-8 -*-
import os, sys
sys.path.append('./')
reload(sys)
sys.setdefaultencoding('utf-8')


cnt_add = 0
cnt_del = 0
cnt_rep = 0

cube_cards = {}
change_log_file = open("../[720][Powered] wtwlf123's Cube - change_log.txt")
for line in change_log_file:
    line = line.strip()
    if not line or line[0] not in ['>', '+', '-']:
        continue
    if line[0] == '+':
        cnt_add += 1
        card_name = line[1::].strip()
        try:
            assert card_name not in cube_cards or cube_cards[card_name] == 0
        except:
            print 'add already in', card_name
        cube_cards[card_name] = 1
    elif line[0] == '-':
        cnt_del += 1 
        card_name = line[1::].strip()
        try:
            assert card_name in cube_cards
        except:
            print 'erase not in', card_name
        cube_cards[card_name] = 0
    elif line[0] == '>':
        cnt_rep += 1
        card_name1, card_name2 = line.split('>')[1:3]
        card_name1 = card_name1.strip()
        card_name2 = card_name2.strip()
        try:
            assert card_name1 in cube_cards and cube_cards[card_name1] == 1
        except:
            print 'replace not in', card_name1
        try:
            assert card_name2 not in cube_cards or cube_cards[card_name2] == 0
        except:
            print 'replace already in', card_name2
        cube_cards[card_name1] = 0
        cube_cards[card_name2] = 1
change_log_file.close()

assert cnt_add - cnt_del == 720

cur_cube_list = set()
cur_cube_list_file = open("../[720][Powered] wtwlf123's Cube.txt")
for line in cur_cube_list_file:
    cur_cube_list.add(line.strip())
cur_cube_list_file.close()

for card in cur_cube_list:
    if card not in cube_cards or cube_cards[card] != 1:
        print "change log don't get", card
for card in cube_cards:
    if cube_cards[card] == 1 and card not in cur_cube_list:
        print "change log extra", card

power720_cube_list_file = open("../[720][Powered] wtwlf123's Cube - all.txt", 'w')
for card in cube_cards:
    power720_cube_list_file.write(card+'\n')
power720_cube_list_file.close()
