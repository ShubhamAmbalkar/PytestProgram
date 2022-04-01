def test_1():
    x=10
    y=20
    assert x<y

def test_login():
    x=10
    s=11
    assert x<s

def test_3():
    x=10
    y=20
    assert x+y==30
    # pytest --html = myHTMLReport.html


# pytest .\test_first.py -rA -k login --html="myHTMLReport.html"
# pytest .\test_first.py -rA --html="myHTMLReport.html"
# pytest .\test_first.py -rA -k login
# pytest -rA
# pytest