def init_logger(logger_type, data):
    logger_profile = []
    log_header = 'run_time,read_time,'
    # what sesnors are we logging?
    for k, v in data.items():
        for kk, vv in data[k].items():
            if(kk != 'device' and data[k][kk]['read'] == True):
                for kkk, vvv in data[k][kk].items():
                    if(kkk != 'read' and data[k][kk][kkk]['log_on'] == True):
                        logger_profile.append((k,kk,kkk))
                        log_header += kkk + ","
    print(log_header.strip(","))



    return logger_profile

def logger(logger_profile, data, start_read, end_read):
    log = ''
    i = 0
    log += ("{0:0.4f},{1:0.4f},").format(start_read, end_read)
    for blah in logger_profile:
        log += ("{0:" + data[blah[0]][blah[1]][blah[2]]['log_format'] + "},").format(data[blah[0]][blah[1]][blah[2]]['value'])

    print(log.strip(","))


