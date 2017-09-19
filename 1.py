import jieba
f = jieba.cut('我是中国人')

print(','.join(f))