#การสร้างฟังก์ชัน
def hello():
    print("hello world")
    print("Peeranat")
#เรียกใช้งานฟังก์ชัน
hello()
#ส่งค่าผ่านparameter
def sum(x,y):
    ans = x+y
    print(ans)
sum(7,8)
sum(5,9)
#ส่งค่าาผ่านparameter+return
def sum(x,y):
    return x + y
ans = sum(8,6)/2
print(ans)