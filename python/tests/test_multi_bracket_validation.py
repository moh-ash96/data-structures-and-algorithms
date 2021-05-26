from code_challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_one_type_brackets():

    assert multi_bracket_validation('[]') == True
    assert multi_bracket_validation('[') == False
    assert multi_bracket_validation(']') == False

    assert multi_bracket_validation('{}') == True
    assert multi_bracket_validation('{') == False
    assert multi_bracket_validation('}') == False

    assert multi_bracket_validation('()') == True
    assert multi_bracket_validation('(') == False
    assert multi_bracket_validation(')') == False

def test_several_types():
    assert multi_bracket_validation('{}(){}') == True

    assert multi_bracket_validation('()[[Extra Characters]]') == True

    assert multi_bracket_validation('(){}[[]]') == True
    assert multi_bracket_validation('{}{Code}[Fellows](())') == True

    assert multi_bracket_validation('[({}]') == False

    assert multi_bracket_validation('(](') == False

    assert multi_bracket_validation('{(})') == False

    assert multi_bracket_validation('[}') == False


