#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import methods

'''
ファイル読み込み
'''
f = open('test.txt', 'r')
box = [] #変換前の経歴を格納するリスト
for row in f:
    box.append(row)
f.close()


'''
replace
'''

#変換
box2 = methods.conv_AD(box)

#月を削除
box2 = methods.del_month(box2)

#退職が含まれる行を削除
box2 = methods.remove_other_retirement(box2)

for i in box2:
    print(i.replace('入社',''),end='')
print('')
