bicycles = ['trek','cannondale','redline','specialized']
#访问列表
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
# -1 最后一个 -2 倒数第二个
print(bicycles[-1])

#修改
bicycles[0] = 'trek_red'
print(bicycles)

#添加
bicycles.append('blueline')
print(bicycles)
bicycles.insert(1,'kkkk')
print(bicycles)

#删除
del bicycles[-1]
print(bicycles)



