def init_logger(logger_type, data):
    logger_profile = []
    log_header = 'run_time,read_time,'
    # what sesnors are we logging?
    for k, v in data.items():
        if(data[k]['device'] != ''): # check to see if our device is setup
            for kk, vv in data[k]['sensors'].items():
                if(data[k]['sensors'][kk]['read'] == True and data[k]['sensors'][kk]['log_on'] == True):
                    log_header += data[k]['sensors'][kk]['log_name'] + ","
                    logger_profile.append((k,'sensors',kk))
    print(log_header.strip(","))
    return logger_profile

def logger(logger_profile, data, start_read, end_read):
    log = ''
    i = 0
    log += ("{0:0.4f},{1:0.4f},").format(start_read, end_read)
    for x in logger_profile:
        if(type(data[x[0]][x[1]][x[2]]['value']) is tuple or type(data[x[0]][x[1]][x[2]]['value']) is map):
            y = list(data[x[0]][x[1]][x[2]]['value'])
            # this isnt the best thing to do here, lets clean it up later
            log += (data[x[0]][x[1]][x[2]]['log_format'] + ",").format(y[0], y[1], y[2])
        elif(type(data[x[0]][x[1]][x[2]]['value']) is int):
            log += ("{},").format(data[x[0]][x[1]][x[2]]['value'])
        else: 
            log += (data[x[0]][x[1]][x[2]]['log_format'] + ",").format(data[x[0]][x[1]][x[2]]['value'])


    print(log.strip(","))
