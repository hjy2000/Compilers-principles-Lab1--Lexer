# -*- coding: utf-8 -*-
"""
编译原理C++实验一 20182131055 侯佳耀
@author: ASUS
"""

#导入tk相关包

import tkinter as tk
from tkinter.filedialog import askopenfilename

#关键字字典
KeyWord=['asm','else','new','this','auto','enum','operator',
          'throw','bool','explicit','private','true','break','exprot','protected','try'
          ,'case','extern','public','typedef','catch','false','register','typeid',
          'char','float','int','reinterpret_cast','typename',
          'class','for','return','union','const','friend',
          'short','unsigned','const_cast','goto','signed','using',
          'continue','if','sizeof','virtual','default','inline','static','void',
          'delete','static_cast','volatile','do','long','struct','wchar_t','double',
          'mutable','switch','while','dynamic_cast','namespace','template']
    
#运算符字典
Operator=['+','-','*','/','%','++','--','==','!=','>','<','>=','<=','&&','||','!','&',
          '|','^','~','<<','>>','=','+=','-=','*=','/=','%=','<<=','>>=','&=','^=','|=']

#特殊符号
Special_symbol=['\\','#',',','(',')','{','}',';','::']

#定义read函数

def read():
    filename = askopenfilename(initialdir = 'd:/ASUS') #此处为弹出文件选取框的默认目录
    f = open(filename,encoding='utf-8') #使用utf-8解码，可根据文件类型更改
    files=f.read()
    
    print(files)
    return files
    f.close()

#定义主函数

def main(f):
    length_of_files=len(f)
    resultList=[]
    i=0#i用于计数
    
    while(i<length_of_files):
        
        if f[i]=='/':
            ObjectString='/'
            if f[i+1]=='/':
                ObjectString+='/'
                k=i+1
                while(True):
                    if f[k+1]!='\n' and f[k+1]!='\r':
                        ObjectString+=f[k+1]
                        k+=1
                    else:
                        break
                    
                resultString=ObjectString+' 注释'
                resultList.append(resultString)
                print(resultString)
                i+=len(ObjectString)
                
            elif f[i+1]=='*':
                 k=i+1
                 ObjectString+='*'
                 while(True):
                    if f[k+1]!='*' and f[k+2]!='/':
                        ObjectString += f[k+1]
                        k=k+1
                    else:
                        break
                 resultString=ObjectString+'*/'+' 注释'
                 resultList.append(resultString)
                 print(resultString)
                 i=i+len(ObjectString)+2#由于跳过了*/两位故为下标增加len+2位
                
                
        elif f[i]=='“':
            
            ObjectString='“'
            k=i+1
            while(True):
                
                if f[k]!='”':
                    ObjectString+=f[k]
                    k+=1
                else:
                    break
                
            ObjectString+='”'
            
            resultString=ObjectString+' 字符串'
            resultList.append(resultString)
            print(resultString)
            i+=len(ObjectString)
            
        elif f[i] in Operator:
            
            if f[i+1] in['+','-','=','&','|','>','<']:
                if f[i+2]=='=':
                    resultString=f[i]+f[i+1]+f[i+2]+'运算符'
                    i=i+2
                else:
                    resultString=f[i]+f[i+1]+'运算符'
                    i=i+1
            else:
                resultString=f[i]+'运算符'
            
            resultList.append(resultString)
            print(resultString)
            i+=1#统一补充向后位移一位（后面的+=1也是这个用途）
            
        elif f[i] in Special_symbol:
            if f[i]=='}':
                resultString=f[i]+'特殊符号'
            else:
                if f[i+1]==':':
                    resultString=':: 特殊符号'
                    i=i+1
                else:
                    resultString=f[i]+'特殊符号'
            
            resultList.append(resultString)
            print(resultString)
            i+=1
            
        elif f[i].isalpha()==True or f[i]=='_':
            ObjectString=''
            k=i
            while(True):
                if f[k]=='_' or f[k].isalpha()==True or f[k].isdigit()==True or f[k]=='.':
                    ObjectString+=f[k]
                    k+=1
                else:
                    
                    break
            if ObjectString in KeyWord:
                resultString=ObjectString+'关键字'
            else:
                resultString=ObjectString+'标识符'
            resultList.append(resultString)
            print(resultString)
            i+=len(ObjectString)
            
        elif f[i].isdigit()==True:
            ObjectString=f[i]
            k=i+1
            while(True):
                if f[k].isdigit()==True:
                    ObjectString+=f[k]
                    k=k+1
                elif f[k]=='.':
                    if f[k+1]=='.':
                        break
                    else:
                        ObjectString+=f[k]
                        k=k+1
                        
                elif f[k] in ['e','E']:
                    if f[k+1].isdigit()==True or (f[k+1] in ['+','-'] and f[k+2].isdigit()==True):
                        ObjectString+=f[k]
                        k+=1
                    else:
                        break
                else:
                    break
                
            resultString=ObjectString+' 数'
            resultList.append(resultString)
            print(resultString)
            i+=len(ObjectString)
            
        else:
            i+=1#暂时忽略其他特殊情况
            
    return resultList

#TK对象实例化及初始化

window = tk.Tk()
window.title('C++词法分析器')
 
#设定窗口的大小(长 * 宽)

window.geometry('650x720')  # 这里的乘是小x
lable1 = tk.Label(window, text='欢迎使用C++词法分析器', bg='grey', font=('Arial', 15), width=60, height=2)

lable1.pack()


# 放置lable的方法有：1）l.pack(); 2)l.place(); 说明：bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

#定义show函数

def show():
    c=read()
    t = tk.Text(window,width=500,height=500)
    t.pack()
    #t.insert(tk.INSERT,'分词结果如下：\n\n')
    for i in main(c):
        t.insert(tk.INSERT,i)
        t.insert(tk.INSERT,'\n')
print()
b = tk.Button(window, text="analyze", command=show,width=100,height=2)
b.pack()
lable2 = tk.Label(window, text='词法分析结果如下：', bg='grey', font=('Arial', 15), width=60, height=2)
lable2.pack()
window.mainloop()

