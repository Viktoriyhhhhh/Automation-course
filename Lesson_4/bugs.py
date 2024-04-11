1. По итогу этого тестирования Функция capitilize приняла бы цифры в значении, что не допустимо (Actual result: 444а)

    def test_capitilize(string, result):
        string_util = StringUtils()
        print(f"Input string: {string}")
        print(f"Expected result: {result}")
        res = string_util.capitilize(string)
        print(f"Actual result: {res}")
>       assert res == result
E       AssertionError: assert '444а' == '456а'
E
E         - 456а
E         + 444а

Lesson_4\test_string_utils.py:25: AssertionError
---------------------------------------------------------------------------------------- Captured stdout call ----------------------------------------------------------------------------------------- 
Input string: 444а
Expected result: 456а
Actual result: 444а


2. Функция "delete_symbol" не предусматривает вариант когда удаляется пробел после слова:
__________________________________________________________________________________ test_delete_symbol[park --park] ___________________________________________________________________________________ 

string = 'park ', symbol = '', result = 'park'
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
>       assert res == result
E       AssertionError: assert 'park ' == 'park'
E
E         - park
E         + park 
E         ?     +
Lesson_4\test_string_utils.py:112: AssertionError