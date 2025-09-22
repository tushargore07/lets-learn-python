def http_status(status):
    match status:
        case 200:
            return("OK")
        case 404:
            return("Not found ")
        case 500:
            return("Internal server error")
        case _:
            return("unkown status")
        
print(http_status(200))