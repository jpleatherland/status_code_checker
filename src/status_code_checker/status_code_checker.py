from status_code_checker.status_codes import status_codes

def explain_status_code(status_codes_to_explain: list[int]):
    result: list[str] = [] 

    for status_code in status_codes_to_explain:
        code_info = status_codes.get(status_code)
        if code_info:
            result.append(f"{status_code} - {code_info['title']}: {code_info['description']}")
        else:
            result.append(f"{status_code} - Unknown: Status code may be a custom error defined on the server.")
                    
    return result
