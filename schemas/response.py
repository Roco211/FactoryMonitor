

def base_response(code, status, message, data = None):
    if data is None:
        data = []

    result = {
        "code": code,
        "status": status,
        "message": message,
        "data": data
    }
    return result

