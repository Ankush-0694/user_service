
def check_token(auth_header):
    if not auth_header or auth_header == "null":
        raise PermissionError("You need to pass token in header")

    