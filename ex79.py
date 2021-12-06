# 字符串排序

if __name__=='__main__':
    list1=[]
    str1=input('请输入第一个字符串：')
    str2=input('请输入第二个字符串：')
    str3=input('请输入第三个字符串：')
    list1.extend([str1,str2,str3])
    str1_sorted = sorted(str1)
    list2=sorted(list1)
    print(str1_sorted)
    print(list2)
