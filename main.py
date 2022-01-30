from unittest import result


print("输入文件名称，并确保当前文件夹下没有result.txt文件！")
name_f = input()
print('输入飞花令关键词文件名称')
name_key = input()
# name_f = 'Poetry.txt'
# name_key = 'key.txt'
fp = open(name_f, encoding='utf-8', mode = 'r')
keyfp = open(name_key, encoding='utf-8', mode = 'r')
resultfp = open('result.txt', encoding='utf-8', mode = 'w+') #保存文件
keywordlist = keyfp.read()

keywordlist = keywordlist.split(' ')


this_line = fp.readline() #保存当前这一行的语句
poem_line = '0' #保存诗词的那一句
topOFpoem = '0' #保存诗名

while this_line != '':
    if this_line[0] == '《':
        topOFpoem = this_line
        poem_line = fp.readline()
        while poem_line[0]!='《':
            for key in keywordlist:
                if poem_line.find(key) != -1:
                    resultfp.write(key+'：'+poem_line[0:-1]+'————'+topOFpoem)
            poem_line = fp.readline()
            if poem_line == '':
                print('结束')
                resultfp.close()
                break
    this_line = poem_line
print('END')