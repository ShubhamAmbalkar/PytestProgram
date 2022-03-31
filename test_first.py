def test_1():
    x=10
    y=20
    assert x==y

def test_login():
    x=10
    s=11
    assert x==s

def test_3():
    x=10
    y=20
    assert x+y==30
    # pytest --html = myHTMLReport.html

def test_4():
    a=14
    b=17
    c=14
    assert a<b
    assert a!=c

def test_login_1():
    a='Shubham'
    b= 'Ajinkya'
    # assert type(a)==int
    assert type(b)==int

# pytest .\test_first.py -rA -k login --html="myHTMLReport.html"
# pytest .\test_first.py -rA --html="myHTMLReport.html"
# pytest .\test_first.py -rA -k login
# pytest -rA
# pytest