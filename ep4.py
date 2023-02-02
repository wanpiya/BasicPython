Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> friend = []
>>> friend.append('somsak')
>>> friend.append('somsri')
>>> #เพิ่ม user
>>> print (friend)
['somsak', 'somsri']
>>> 
>>> friend.insert(0,'sompong')
>>> #เพิ่ม user แบบเลือกตำแหนง
>>> print (friend)
['sompong', 'somsak', 'somsri']
>>> 
>>> del friend[-1]
>>> #ลบ user
>>> print (friend)
['sompong', 'somsak']
>>> 
>>> friend.remove('somsak')
>>> #ลบ user แบบระบุชื่อ
>>> print (friend)
['sompong']
>>> 
>>> friend.insert(1,'somsri')
>>> #เพิ่ม user แบบเลือกตำแหนง
>>> print (friend)
['sompong', 'somsri']
>>> 
>>> friend.insert(0,friend.pop(1))
>>> #ย้ายตำแหน่ง user
>>> print (friend)
['somsri', 'sompong']
type(friend)
<class 'list'>
teacher = ('korkai','khorkai','korkwai' )
teacher.append('sorn')
type (teacher)
<class 'tuple'>#tuple มีฟังชั่นแค่ count,index
coin = (5,1,10,2,5,1,2,15,5,2,1,10,10,5,5,2,1,)
coin.count(10)
3
#ใช้หาจำนวน
teacher = ('korkai','khorkai','korkwai' )
teacher.index('korkai')
0
#ใช้หาตำแหน่ง
character = ['a','z','c','x','y']
type (character)
<class 'list'>#list สามารถใช้ฟังชั้นได้หลากหลายแก้ไขได้
>>> character.sort()
>>> print(character)
['a', 'c', 'x', 'y', 'z']
>>> # sort() ใช้เรียงลำดำใหม่
>>> character.append('b')
>>> print(character)
['a', 'c', 'x', 'y', 'z', 'b']
>>> character.sort()
>>> print(character)
['a', 'b', 'c', 'x', 'y', 'z']
>>> character.sort(reverse=True)
>>> print(character)
['z', 'y', 'x', 'c', 'b', 'a']
>>> # สลับการเรียงลำดับ sort(reverse=True)
>>> character.sort(reverse=True)
>>> print(character)
['z', 'y', 'x', 'c', 'b', 'a']
>>> character.sort()
>>> print(character)
['a', 'b', 'c', 'x', 'y', 'z']
>>> character = ['a','z','c','x','y']
>>> sorted(character)
['a', 'c', 'x', 'y', 'z']
>>> #print แบบเรียงให้ชั่วคราว
>>> print(character)
['a', 'z', 'c', 'x', 'y'] #สุดท้าค่า list ยังเรียงเหมือนเดิม
