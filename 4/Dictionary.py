# dictionary문법 : key와 value값이 1:1
# get() : key 추출

query = input("\n프로그래밍 언어 입력 : ")
query = query.lower()
if "c" in query :
    print("C언어는 1972년에 태어났어요.")
elif "java" in query :
    print("java는 1995년에 태어났어요.")
elif "java" in query:
    print("Python 1991년에 태어났어요.")
else :
    print("등록되지 않은 언어입니다.")

dic = { 'c' : 1972,
        'java' : 1991,
        'python' : 1991,
        'go':2009,
        'pascal':1969}

query = input("\n프로그래밍 언어 입력 : ")
k = query.lower()

if k in dic :
    year = dic.get(k)
    print("{}언어는 {}년에 태어났어요.".format(query,year))
else:
    print("등록되지 않은 언어입니다.")