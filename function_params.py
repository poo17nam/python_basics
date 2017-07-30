def print_msg(msg, error="No error", *args, **kwargs):
    print("Log:" +error +"\t"+ msg)
    print("Args:", args)
    print("kwargs: ",  kwargs)
    
print_msg("This will be logged","file not found","1","2",key_1="1,2,3,4",key_2="5,6,7,8")
