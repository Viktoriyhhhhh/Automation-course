import pytest

from string_utils import StringUtils
string_util = StringUtils()

#Test Case 1: Tests if function "capitilize" makes the first letter capital
@pytest.mark.parametrize('string, result', [
    #positive test cases:
    ("ваня", "Ваня"),
    ("алла Виктория", "Алла виктория"),
    #("вариант ", "Вариант")
    #negative test cases:
    ("", ""),
    ("Ирина", "Ирина"),
    ("ООО", "Ооо"), 
    ("444а", "456а") # other alphabets
])

def test_capitilize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitilize(string)
    print(f"Actual result: {res}")
    assert res == result

#Test Case 2: Tests if function "trim" removes empy space before the string
@pytest.mark.parametrize('string, result', [
    #positive test cases:
    (" питон", "питон"),
    (" ПИТОН", "ПИТОН"),
    (" Алла-Виктория", "Алла-Виктория"),
    (" Vika1", "Vika1"),
    #negative test cases:
    ("", ""),
    ("всере дине", "всере дине"),
    ("вконце ", "вконце "),
    (0, 0)
])
def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result

#Test Case 3: Tests if function "to_list" converst string to list
@pytest.mark.parametrize('string, divider, result', [
    #positive test cases:
    ("цветок,дерево,лес", ",", ["цветок", "дерево", "лес"]),
    ("слово:текст:предложение", ":", ["слово", "текст", "предложение"]),
    ("p,y,t,h,o,n", ",", ["p", "y", "t", "h", "o", "n"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    #negative test cases:
    ("", None, []),
    ("  ", None, [  ]),
    ])

def test_to_list(string, divider, result):
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    
    if divider is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, divider)
    
    print(f"Actual result: {res}")
    
    assert res == result

#Test Case 4: Tests if function "contains" correctly checks that a string contains a symbol
@pytest.mark.parametrize('string, symbol, result', [
    #positive test cases:
    ("flower", "f", True),
    (" питон", "и", True),
    ("урок  ", "о", True),
    ("+*--", "+", True),
    #negative test cases:
    ("hello", "x", False),  
    ("Почта", "@", False), 
    ("привет", " ", False),  
    (" ", "з", False)
])

def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result

#Test Case 5: Tests if function "delete_symbol" delets indicated symbol
@pytest.mark.parametrize('string, symbol, result', [
    #positive test cases:
    ("test", "t", "es"),
    ("Урок", "У", "рок"),
    ("123", "1", "23"),
    ("КОШКА", "КО", "ШКА"),
    #negative test cases:
    ("испания", "О", "испания"),
    ("кошка", "", "кошка"),
    ("park ", "", "park"),
    ("", "r", "")
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result

#Test Case 6: Tests if function "starts_with" identifies the beggining symbol
@pytest.mark.parametrize('string, symbol, result', [
    #positive test cases:
    ("Эксель", "Э", True),
    ("sun", "s", True),
    (" cat", "", True),
    ("6789", "6", True),
    #negative test cases:
    ("Cool", "l", False),
    ("море", "М", False),
    ("", "Л", False),
    (" ", "", False)
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result

#Test Case 7: Tests if function "end_with" identifies the ending symbol
@pytest.mark.parametrize('string, symbol, result', [
    #positive test cases:
    ("холод", "д", True),
    ("GREAT", "T", True),
    ("кошка ", " ", True),
    ("1238", "8", True),
    #negative test cases:
    ("ночь", "д", False),
    ("Кошка", "5", False),
    ("балкон", "Н", False),
    ("", "ж", False)
])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result

#Test Case 8: Tests if function "is_empty" identifies an empty string
@pytest.mark.parametrize('string, result', [
    #positive test cases:
    ("", True),
    (" ", True),
    ("  ", True),
    #negative test cases:
    ("p", False),
    ("yt", False),
    (" hon", False),
    ("9 ", False)   
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result

#Test Case 9: Tests if function "list_to_string" converts a list to a string
@pytest.mark.parametrize('lst, joiner, result', [
    #positive test cases:
    (["a", "b", "c"], ",", "a,b,c"),
    ([-1, -2, -3, -4, -5], ",", "-1,-2,-3,-4,-5"),
    (["Mary", "Anne"], "-", "Mary-Anne"),
    #negative test cases:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    print(f"Input list: {lst}")
    print(f"Expected result: {result}")
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    print(f"Actual result: {res}")
    assert res == result