def print_msg(msg, error="No error", *kwargs):
    print("Log:" +error +"\t"+ msg)

print_msg("This will be logged","file not found","1","2")
