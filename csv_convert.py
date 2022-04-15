
#_*_ coding: utf-8 _*_

import codecs



infile = codecs.open('ad_list.csv', 'r', encoding='utf-8')
outfile = codecs.open('광고.csv', 'w', encoding='cp949')
#outfile = codecs.open('DaDo2.csv', 'w', encoding='cp949')

for line in infile:
    line = line.replace(u'\u0107',' ').replace(u'\u015b', ' ').replace(u'\u200b', ' ').replace(u'\ufeff',' ').replace(u'\xf6',' ').replace(u'\U0001f379',' ').replace(u'\U0001f35c',' ').replace(u'\U0001f9c0',' ').replace(u'\U0001f37a',' ').replace(u'\u2013',' ')

    outfile.write(line)

infile.close()
outfile.close()

