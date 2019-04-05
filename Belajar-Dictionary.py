member1={"id":101,
         "nama":"Dany",
         "pekerjaan":"Mahasiswa",
         "status":"Gold"
         }

member2={"id":103,
         "nama":"Candra",
         "pekerjaan":"Mahasiswa",
         "status":"Silver"
         }

print(member1["pekerjaan"])
print(member1.keys())
print(member1.values())
print(member1.items())

print(member2["pekerjaan"])
print(member2.keys())
print(member2.values())
print(member2.items())

memberList={101:member1,102:member2}

print(memberList[101])


