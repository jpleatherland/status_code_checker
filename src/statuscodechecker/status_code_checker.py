from statuscodechecker.status_codes import status_codes

def explain_status_code(status_codes_to_explain: list[int]):
    for status_code in status_codes_to_explain:
        code_info = status_codes.get(status_code)
        if code_info:
            print(f"{status_code} - {code_info['title']}: {code_info['description']}")
        else:
            print(
                f"{status_code} - Unknown status code, it may be a customer error defined on the server"
            )
