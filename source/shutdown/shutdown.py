import subprocess as sub


def shutdown(time=0,force=False,warning_off=False):
    # TODO: solve unix version problem
    '''

    :param time: int , Time in second for shutdown
    :param force: bool ,True for Force shutdown
    :param warning_off: bool , True for shutdown without any warning , this option ignore time
    :return: bool , True (Successfully) False(Unsuccessfully)
    '''
    if warning_off==True:
        command="shutdown -p "
    else:
        command="shutdown -s "
    try:
        if force==True:
            command+="-f "
        if warning_off==False:
            response=sub.Popen(command+"-t "+str(time),shell=True,stdin=sub.PIPE,stderr=sub.PIPE,stdout=sub.PIPE)
        else:
            response = sub.Popen(command ,shell=True, stdin=sub.PIPE, stderr=sub.PIPE,stdout=sub.PIPE)
        response=list(response.communicate())
        if len(response[0])!=0 or (str(response[1]).find("1190")!=-1):
            return False
        else:
            return True
    except:
        return False
def restart(time=0,force=False):
    # TODO: solve unix version problem
    '''

    :param time: int , Time in second for restart
    :param force: bool ,True for Force restart
    :return: bool , True (Successfully) False(Unsuccessfully)
    '''
    command="shutdown -r "
    try:
        if force==True:
            command+="-f "
        response=sub.Popen(command+"-t "+str(time),shell=True,stdin=sub.PIPE,stdout=sub.PIPE,stderr=sub.PIPE)
        response = list(response.communicate())
        if len(response[0])!=0 or (str(response[1]).find("1190")!=-1):
            return False
        else:
            return True
    except :
        return False
def hibernate(force=False):
    # TODO: solve unix version problem
    '''

    :param force: bool ,True for Force hibernate
    :return: bool , True (Successfully) False(Unsuccessfully)
    '''
    command="shutdown -h"
    try:
        if force==True:
            command+=" -f"
        response=sub.Popen(command,shell=True,stderr=sub.PIPE,stdout=sub.PIPE,stdin=sub.PIPE)
        response = list(response.communicate())
        if len(response[0])!=0 or (str(response[1]).find("1190")!=-1):
            return False
        else:
            return True
    except:
        return False
def logoff(force=False):
    # TODO: solve unix version problem
    '''

    :param force: bool ,True for Force logoff
    :return: bool , True (Successfully) False(Unsuccessfully)
    '''
    command="shutdown -l"
    try:
        if force==True:
            command+=" -f"
        response=sub.Popen(command,shell=True,stdin=sub.PIPE,stdout=sub.PIPE,stderr=sub.PIPE)
        response = list(response.communicate())
        if len(response[0]) != 0 or (str(response[1]).find("1190") != -1):
            return False
        else:
            return True
    except:
        return False

def cancel():
    # TODO: solve unix version problem
    '''

    :return: bool , True (Successfully) False(Unsuccessfully)
    '''
    command="shutdown -a"
    try:
        response=sub.Popen(command,shell=True,stderr=sub.PIPE,stdin=sub.PIPE,stdout=sub.PIPE)
        response = list(response.communicate())
        if len(response[0]) != 0 or (str(response[1]).find("1116") != -1):
            return False
        else:
            return True
    except:
        return False