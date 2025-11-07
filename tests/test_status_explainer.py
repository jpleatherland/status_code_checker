from status_code_checker.status_code_checker import explain_status_code

def test_explain_known_status_code():
    # assuming 200 exists in status_codes
    result = explain_status_code([200])
    assert isinstance(result, list)
    assert any("200" in line and "Unknown" not in line for line in result)

def test_explain_unknown_status_code():
    # assuming 9999 does not exist in status_codes
    result = explain_status_code([9999])
    print(result)
    assert isinstance(result, list)
    assert any("9999 - Unknown" in line for line in result)

def test_explain_mixed_status_codes():
    # assuming 200 exists and 9999 does not
    result = explain_status_code([200, 9999])
    print(result)
    assert len(result) == 2
    assert any("200" in line and "Unknown" not in line for line in result)
    assert any("9999 - Unknown" in line for line in result)
