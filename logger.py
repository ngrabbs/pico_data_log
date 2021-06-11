def init_logger(logger_type, data):
    logger_profile = []
    log_header = 'run_time,read_time,'
    # what sesnors are we logging?
    for k, v in data.items():
        if(data[k]['device'] != ''): # check to see if our device is setup
            for kk, vv in data[k]['sensors'].items():
                if(data[k]['sensors'][kk]['read'] == True and data[k]['sensors'][kk]['log_on'] == True):
                    print('read sensor: ' + data[k]['sensors'][kk]['name'])
                    log_header += data[k]['sensors'][kk]['log_name']
                    logger_profile.append((k,'sensors',kk))
    print(log_header.strip(","))
    return logger_profile

def logger(logger_profile, data, start_read, end_read):
    log = ''
    i = 0
    log += ("{0:0.4f},{1:0.4f},").format(start_read, end_read)
    for x in logger_profile:
        if(type(data[x[0]][x[1]][x[2]]['value']) != 'str' and type(data[x[0]][x[1]][x[2]]['value']) != 'int'):
            my_list = list(data[x[0]][x[1]][x[2]]['value'])
            # this isnt the best thing to do here, lets clean it up later
            log += ("{0:0.4f},{1:0.4f},{2:0.4f},").format(my_list[0], my_list[1], my_list[2])
        else:
            log += ("{0}", data[x[0]][x[1]][x[2]]['value'])

    print(log.strip(","))
