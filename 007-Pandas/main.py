import pandas as pd

data = pd.Series([6, 21, 8, 1])
print(data)
# 輸出結果為兩行。第一行為索引，第二行為Series資料。
# 輸出的每一個row由index標籤（label）及其對應的值所組成。
# 0     6
# 1    21
# 2     8
# 3     1
# dtype: int64

ser = pd.Series([3,6])
ser.iloc[0] = 999
print(ser)
# 0    999
# 1      6
# dtype: int64

users = pd.DataFrame({
    "id": [1,2,3,4], 
    "name": ["John", "Amy", "Tom", "Kelly"],
    "age": [21,24,23,22]
})
print(users)
# dtype: int64
#    id   name  age
# 0   1   John   21
# 1   2    Amy   24
# 2   3    Tom   23
# 3   4  Kelly   22


users = pd.DataFrame({
    "id": [1,2,3,4], 
    "name": ["John", "Amy", "Tom", "Kelly"],
    "age": [21,24,23,22]
}, index=[3,2,1,0])

print(users)
#    id   name  age
# 3   1   John   21
# 2   2    Amy   24
# 1   3    Tom   23
# 0   4  Kelly   22

print(users.iloc[0])
# id         1
# name    John
# age       21

print(users.loc[0])
# id          4
# name    Kelly
# age        22



users = pd.DataFrame([
    [1, "John", 21], 
    [2, "Amy",  24], 
    [3, "Tom",  23], 
    [4, "Kelly",22], 
], index=[3,2,1,0], columns=["id", "name", "age"])

print(users)
#    id   name  age
# 3   1   John   21
# 2   2    Amy   24
# 1   3    Tom   23
# 0   4  Kelly   22

print(users.T)