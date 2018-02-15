#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

'''
経歴を全てA.D.に変換したlistを返すメソッド
昭和、平成を西暦に変換
平成→西暦：西暦 = 2000 + 平成 - 12 ※元年は1年に変換
昭和→西暦：西暦 = 1900 + 昭和 + 25
'''
def conv_AD(box):
    box2=[] #変換後の経歴を格納するリスト
    for row in box:
        if row.find('平成') != -1:
            #マッチングパターンの設定
            if row.find('年') != -1:
                heisei = re.compile('(平成(.|..)年)')
            match = heisei.findall(row)

            #変換
            for i in match:
                AD = str(2000 + int(i[1].replace('元','1')) - 12) + '年'
                row = row.replace(i[0],AD)
            #格納
            box2.append(row)

        elif row.find('H') != -1:
            #マッチングパターンの設定
            if row.find('年') != -1:
                H = re.compile('(H(.|..)年)')
            match = H.findall(row)

            #変換
            for i in match:
                AD = str(2000 + int(i[1]) - 12) + '年'
                row = row.replace(i[0],AD)
            #格納
            box2.append(row)


        elif row.find('昭和') != -1:
            #マッチングパターンの設定
            if row.find('年') != -1:
                showa = re.compile('(昭和(.|..)年)')
            match = showa.findall(row)

            #変換
            for i in match:
                AD = str(1900 + int(i[1]) + 25) + '年'
                row = row.replace(i[0],AD)
            #格納
            box2.append(row)

        elif row.find('S') != -1:
            #マッチングパターンの設定
            if row.find('年') != -1:
                H = re.compile('(S(.|..)年)')
            match = H.findall(row)

            #変換
            for i in match:
                AD = str(1900 + int(i[1]) + 25) + '年'
                row = row.replace(i[0],AD)
            #格納
            box2.append(row)

        else:
            box2.append(row)
    return box2

'''
月を削除するメソッド
'''
def del_month(box):
    box2 = []
    for i in box:
        if i.find('月') != -1:
            #マッチングパターンの設定
            patarn = re.compile('((.|..)月)')
            match = patarn.findall(i)

            #削除
            for j in match:
                i = i.replace(j[0],'')
            #格納
            box2.append(i)
        else:
            box2.append(i)
    return box2


def remove_other_retirement(box):
    for row in box:
        if '退' in row:
            #リストから削除
            box.remove(row)
    return box
