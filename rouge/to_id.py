# coding:utf8
import sys

s = "/home/yueyongjiao/gitProject/python2_workplace/openNMT/openNMT/EventTeller/test_target.txt"
wd = {}
f = open('word_dic')
wid = 0
for line in f:
    res = line.strip().split(' ')
    wd[res[0]] = wid
    wid += 1
f.close()
wd['<unk>'] = wid
print(len(wd))
wd[''] = 0

# f = open(s, 'r', 'utf-8')

f = open(s)
fw = open(s + '_id', 'w')
for line in f:
    res = line.strip().split(' ')
    res = res.encode('utf-8')
    for i in range(len(res) - 1):
        fw.write(str(wd[res[i]]) + ' ')
    fw.write(str(wd[res[-1]]) + '\n')
fw.close()
f.close()

