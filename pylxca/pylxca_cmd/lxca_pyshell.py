'''
@since: 5 Feb 2016
@author: Prashant Bhosale <pbhosale@lenovo.com>, Girish Kumar <gkumar1@lenovo.com>
@license: Lenovo License
@copyright: Copyright 2016, Lenovo
@organization: Lenovo 
@summary: This module provides scriptable interfaces and scriptable python shell.
'''

import os, time,code
import signal, logging, sys
import traceback

from pylxca import __version__
from pylxca.pylxca_cmd import lxca_ishell
from pylxca.pylxca_cmd.lxca_cmd import fanmuxes

#shell is a global variable
shell_obj = None
logger = logging.getLogger(__name__)


def pyshell(shell=lxca_ishell.InteractiveShell()):
    '''
    @summary: this method provides scriptable python shell
    '''
    global shell_obj
    shell_obj = shell
    shell_obj.set_ostream_to_null()

def set_interactive():
    '''
    @summary: This method set the shell in interactive mode
    '''
    ns = {"connect": connect,
          "disconnect": disconnect,
          "chassis": chassis,
          "cmms": cmms,
          "fans": fans,
          "fanmuxes": fanmuxes,
          "switches": switches,
          "powersupplies": powersupplies,
          "nodes": nodes,
          "scalablesystem": scalablesystem,
          "discover": discover,
          "manage": manage,
          "unmanage": unmanage,
          "jobs": jobs,
          "users": users,
          "lxcalog": lxcalog,
          "ffdc": ffdc,
          "updatecomp": updatecomp,
          "updatepolicy": updatepolicy,
          "updaterepo": updaterepo,
          "configpatterns": configpatterns,
          "configprofiles": configprofiles,
          "configtargets": configtargets,
          "tasks": tasks,
          "manifests": manifests,
          "osimages": osimages,
          "resourcegroups": resourcegroups, 
          "help": help}
    ns.update()
    global __version__
    code.interact('Interactive Python Shell for Lenovo XClarity Administrator v' + __version__ + '\nType "dir()" or "help(lxca command object)" for more information.', local=ns)


def connect(*args, **kwargs):

    '''

@summary:
    Use this function to connect to Lenovo XClarity Administrator
    run this function as  
    
    con_variable = connect( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['url','user','pw','noverify']

@param
    The parameters for this command are as follows 
    
        con          Connection Object to Lenovo XClarity Administrator
        url          url to Lenovo XClarity Administrator Example. https://a.b.c.d
        user         User Id to Authenticate Lenovo XClarity Administrator
        pw           Password to Authenticate Lenovo XClarity Administrator
        noverify     flag to indicate to not verify server certificate

@example 
    con1 = connect( con = "https://10.243.12.142",user = "USERID", pw = "Password", noverify = "True")
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    keylist = ['url','user','pw','noverify']
    if len(args) == 0 and len(kwargs) == 0:
        return
    
    for i in range(len(args)):
        kwargs[keylist[i]]= args[i]
    
    con = shell_obj.handle_input_args(command_name, args=args, kwargs=kwargs)
    
    return con 
def disconnect(*args, **kwargs):

    '''

@summary:
    Use this function to disconnect from Lenovo XClarity Administrator
    run this function as  
        disconnect()  

@param
    The parameters for this command are as follows
        
        con      Connection Object to Lenovo XClarity Administrator
    
@example 
    disconnect()
    '''

    global shell_obj
    command_name = sys._getframe().f_code.co_name
    keylist = ['con']
    if len(args) == 0 and len(kwargs) == 0:
        return
    
    for i in range(len(args)):
        #print args[i]
        kwargs[keylist[i]]= args[i]
    
    con = shell_obj.handle_input_args(command_name, args=args, kwargs=kwargs)
    
    return con 

def cmms(*args, **kwargs):
    '''

@summary:
    Use this function to get CMMs information
    run this function as  
    
    data_dictionary = cmms( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','uuid','chassis']

@param
    The parameters for this command are as follows 
    
    con       Connection Object to Lenovo XClarity Administrator
    uuid      cmm uuid
    chassis   chassis uuid  

@example 
    cmm_list = cmms( con = con1 ,uuid = 'fc3058cadf8b11d48c9b9b1b1b1b1b57', pw = 'Password', noverify = "True")
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    long_short_key_map = {'uuid': 'u', 'chassis': 'c'}
    keylist = ['con','uuid','chassis']
    optional_keylist = ['con', 'uuid','chassis']
    mutually_exclusive_keys = ['uuid','chassis']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map,  mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def chassis(*args, **kwargs):
    '''

@summary:
    Use this function to get Chassis information
    run this function as  
    
    data_dictionary = chassis( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','uuid','status']

@param
    The parameters for this command are as follows 
    
    con        Connection Object to Lenovo XClarity Administrator
    uuid       chassis uuid
    status     chassis manage status (managed/unmanaged)
    

@example 
    
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    long_short_key_map = {'uuid': 'u', 'status': 's'}
    keylist = ['con','uuid','status']
    optional_keylist = ['con', 'uuid','status']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map,  mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def fans(*args, **kwargs):
    '''

@summary:
    Use this function to get fans information
    run this function as  
    
    data_dictionary = fans( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','uuid','chassis']

@param
    The parameters for this command are as follows 
    
    con           Connection Object to Lenovo XClarity Administrator
    uuid          uuid of fan
    chassis       chassis uuid
    
@example 
    
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    long_short_key_map = {'uuid': 'u', 'chassis': 'c'}
    keylist = ['con','uuid','chassis']
    optional_keylist = ['con', 'uuid','chassis']
    mutually_exclusive_keys = ['uuid','chassis']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def fanmuxes(*args, **kwargs):
    '''

@summary:
    Use this function to get fanmuxes information
    run this function as  
    
    data_dictionary = fanmuxes( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','uuid','chassis']

@param
    The parameters for this command are as follows 
    
    con           Connection Object to Lenovo XClarity Administrator
    uuid          uuid of fanmux
    chassis       chassis uuid
    
@example 
    
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    long_short_key_map = {'uuid': 'u', 'chassis': 'c'}
    keylist = ['con', 'uuid', 'chassis']
    optional_keylist = ['con', 'uuid', 'chassis']
    mutually_exclusive_keys = ['uuid', 'chassis']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def nodes(*args, **kwargs):
    '''

@summary:
    Use this function to get nodes information
    run this function as  
    
    data_dictionary = nodes( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','uuid','chassis','status']

@param
    The parameters for this command are as follows 
    
    con           Connection Object to Lenovo XClarity Administrator
    uuid          uuid of node
    chassis       chassis uuid
    status        nodes manage status (managed/unmanaged)
    
@example 
    
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    long_short_key_map = {'uuid':'u' , 'chassis':'c', 'status':'s'}
    keylist = ['con','uuid','chassis','status']
    optional_keylist = ['con', 'uuid', 'chassis','status']
    mutually_exclusive_keys = ['uuid', 'chassis']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def switches(*args, **kwargs):
    '''

@summary:
    Use this function to get switches information
    run this function as  
    
    data_dictionary = switches( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','uuid','chassis','ports','action']

@param
    The parameters for this command are as follows 
    
    con      Connection Object to Lenovo XClarity Administrator
    uuid          uuid of switch
    chassis       chassis uuid
    ports         empty ports string list all ports for uuid, comma separated ports
    action        enable/disable ports
    
@example 
    
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None

    long_short_key_map = {'uuid': 'u', 'chassis': 'c'}  # other parameter don't have short option
    keylist = ['con', 'uuid', 'chassis', 'ports', 'action']
    optional_keylist = ['con', 'uuid', 'chassis', 'ports', 'action']
    mutually_exclusive_keys = ['uuid', 'chassis']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def powersupplies(*args, **kwargs):
    '''

@summary:
    Use this function to get powersupplies information
    run this function as  
    
    data_dictionary = powersupplies( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','uuid','chassis']

@param
    The parameters for this command are as follows 
    
    con      Connection Object to Lenovo XClarity Administrator
    uuid          uuid of power supply
    chassis       chassis uuid
    
@example 
    
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None
    long_short_key_map = {'uuid': 'u', 'chassis': 'c'}
    keylist = ['con', 'uuid', 'chassis']
    optional_keylist = ['con', 'uuid', 'chassis']
    mutually_exclusive_keys = ['uuid', 'chassis']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def scalablesystem(*args, **kwargs):
    '''

@summary:
    Use this function to get scalablesystem information
    run this function as  
    
    data_dictionary = scalablesystem( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','id','type']

@param
    The parameters for this command are as follows 
    
    con      Connection Object to Lenovo XClarity Administrator
    id        scalable complex id
    type      type (flex/rackserver)

@example 
    
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None

    long_short_key_map = {'id': 'i', 'type': 't'}
    keylist = ['con','id','type']
    optional_keylist = ['con', 'id','type']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def discover(*args, **kwargs):
    '''

@summary:
    Use this function to discover endpoint from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = discover( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','ip','job']

@param
    The parameters for this command are as follows 
    
    con    Connection Object to Lenovo XClarity Administrator
    ip     One or more IP addresses for each endpoint to be discovered.
    job    Job ID of discover request


@example
 
    For Getting Maangement job status
        
        job_data = discover(con=con1,job=jobid)
            
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    long_short_key_map = {'ip': 'i', 'job': 'j'}
    keylist = ['con','ip','job']
    optional_keylist = ['con', 'ip','job']
    mutually_exclusive_keys = ['ip','job']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)
    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def manage(*args, **kwargs):
    '''

@summary:
    Use this function to manage endpoint from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = manage( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','ip','user','pw','rpw','job','force']

@param
    The parameters for this command are as follows 
    
        con      Connection Object to Lenovo XClarity Administrator
        ip       One or more IP addresses for each endpoint to be managed.
        user     user ID to access the endpoint
        pw       The current password to access the endpoint.
        rpw      The recovery password to be used for the endpoint.
        force     force manage
        job       Job ID of existing manage request
        
        Note : mp, type and epuuid parameters are dedpriciated and only kept for backword compatibility. 

@example 

        jobid = manage(con=con1,ip="10.243.6.68",user="USERID",pw="PASSW0RD",rpw="PASSW0RD")
    
    or with named variable it can be represented as
    
        jobid = manage(con= con1,ip="10.243.6.68",user="USERID","PASSW0RD","PASSW0RD",True)
            
    For Getting Maangement job status
        
        manage_data = manage(con=con1,job=jobid)
    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None

    long_short_key_map = {'ip': 'i', 'user':'u', 'pw':'p', 'rpw':'r', 'job': 'j', 'force':'f'}
    keylist = ['con','ip','user','pw','rpw','job','force']
    optional_keylist = ['con', 'ip','user','pw','rpw','job','force']
    mutually_exclusive_keys = ['ip', 'job']
    mandatory_options_list = {'ip':['user','pw'], 'job':[]}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def unmanage(*args, **kwargs):
    '''

@summary:
    Use this function to unmanage endpoint from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = unmanage( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','ip','force','job']

@param
    The parameters for this command are as follows 
    
        ip          one or more endpoints to be unmanaged.
                    This is comma separated list of multiple endpoints, each endpoint should
                    contain endpoint information separated by semicolon.
                    endpoint's IP Address(multiple addresses should be separated by #), UUID of the endpoint and
                    Type of endpoint to be unmanaged ,This can be one of the following values:
                          Chassis
                          ThinkServer
                          Storage
                          Rackswitch
                          Rack-Tower
        force       Indicates whether to force the unmanagement of an endpoint (True/False)
        job         Job ID of unmanage request

@example 

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    long_short_key_map = {'ip': 'i', 'job': 'j', 'force': 'f'}
    keylist = ['con','ip','force','job']
    optional_keylist = ['con', 'ip','force','job']
    mutually_exclusive_keys = ['ip', 'job']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def configpatterns(*args, **kwargs):
    '''

@summary:
    Use this function to Retrieve information and deploy all server and category patterns
            that have been defined in the Lenovo XClarity Administrator
            
    run this function as  
    
    data_dictionary = configpatterns( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','id', 'includeSettings', 'endpoint','restart','type', pattern_update_dict]

@param
    The parameters for this command are as follows 
    
        id          The unique ID that was assigned when the server pattern was created
        
        endpoint    List of one or more UUIDs for the target servers,If a target is an empty bay,
                      specify the location ID; otherwise, specify the server UUID
        
        restart     When to activate the configurations. This can be one of the following values:
                      defer - Activate IMM settings but do not restart the server.
                      immediate - Activate all settings and restart the server immediately.
                      pending - Manually activate the server profile and restart the server.
        
        type        Type of the server, It can be one of the following
                      flex -  Flex System Placeholder chassis empty bays
                      Node
                      Rack
                      Tower

        pattern_update_dict  dictionary of category_pattern to import.

        status      check config status for given uuid in endpoint
                    True

@example 

    '''    
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None
    # some of them don't have short options
    long_short_key_map = {'id': 'i', 'endpoint': 'e', 'restart': 'r', 'type': 't', 'name': 'n','status':'s'}
    keylist = ['con', 'id', 'includeSettings', 'endpoint', 'restart', 'type', 'pattern_update_dict', 'name', 'status']
    optional_keylist = ['con', 'id', 'includeSettings', 'endpoint', 'restart', 'type', 'pattern_update_dict', 'name', 'status']
    mutually_exclusive_keys = ['id', 'pattern_update_dict']
    mandatory_options_list = {'id': [], 'pattern_update_dict': [],
                              'includeSettings': ['id']}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                        param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def configprofiles(*args, **kwargs):
    '''

@summary:
    Use this function to Retrieve information server configuration profiles
            that have been defined in the Lenovo XClarity Administrator
    
    run this function as  
    
    data_dictionary = configprofiles( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con', 'id', 'name', 'endpoint', 'restart', 'delete', 'unassign', 'powerdown', 'resetimm', 'force']

@param
    The parameters for this command are as follows 
    
        id          The unique ID that was assigned when the server profile was created
        name        profile name
        endpoint    endpoint  UUID of the server or location id for flex system
        restart     restart server to activate profile ( immediate / defer )
        delete      True for delete id
        unassign    unassign specified id
                    options for unassign
        powerdown   powerdown server
        resetIMM    reset IMM
        force       force unassign operation

@example 

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None
    # some of keys don't have short option
    long_short_key_map = {'id': 'i', 'name': 'n', 'endpoint': 'e', 'restart': 'r', 'delete': 'd', 'unassign': 'u',
                          'powerdown':'p', 'force':'f'}
    keylist = ['con', 'id', 'name', 'endpoint', 'restart', 'delete', 'unassign', 'powerdown', 'resetimm', 'force']
    optional_keylist = ['con', 'id', 'name', 'endpoint', 'restart', 'delete', 'unassign', 'powerdown', 'resetimm', 'force']
    mutually_exclusive_keys = []
    mandatory_options_list = {'id': [], 'endpoint': ['restart'], 'delete': ['id'],
                              'unassign': ['id']}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def configtargets(*args, **kwargs):
    '''

@summary:
    Use this function to get config pattern targets from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = configtargets( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','id']

@param
    The parameters for this command are as follows 
        id    config target id

@example 

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None
    long_short_key_map = {'id': 'i'}
    keylist = ['con','id']
    optional_keylist = ['con']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def updatepolicy(*args, **kwargs):
    '''

@summary:
    Use this function to read Firmwar update Policy from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = updatepolicy( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','info','job','uuid',policy','Type']

@param
    The parameters for this command are as follows 

    info    Specifies the type of information to return. This can be one of the following values:
                FIRMWARE- Returns information about firmware that is applicable to each managed endpoint
                RESULTS- Returns persisted compare result for servers to which a compliance policy is assigned

    jobid    Job ID of assign compliance policy operation

    uuid     UUID of the device to which you want to assign the compliance policy

    policy   Policyname, Name of the compliance-policy to be assigned to device

    Type     Device type. This can be one of the following values.
                    CMM - Chassis Management Module
                    IOSwitch - Flex switch
                    RACKSWITCH - RackSwitch switch
                    STORAGE - Lenovo Storage system
                    SERVER - Compute node or rack server

@example

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None
    long_short_key_map = {'info': 'i','job': 'j', 'uuid': 'u', 'policy': 'p', 'type': 't'}
    keylist = ['con', 'info', 'job', 'uuid', 'policy','type']
    optional_keylist = ['con', 'info', 'job', 'uuid', 'policy','type']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def updaterepo(*args, **kwargs):
    '''

@summary:
    Use this function to get repository info from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = updaterepo( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','key']

@param
    The parameters for this command are as follows 
    
    key    Returns the specified type of update. This can be one of the following values.
                supportedMts - Returns a list of supported machine types
                size - Returns the repository size
                lastRefreshed - Returns the timestamp of the last repository refresh
                importDir - Returns the import directory for the repository.
                publicKeys - Returns the supported signed keys
                updates - Returns information about all firmware updates
                updatesByMt - Returns information about firmware updates for the specified machine type
                updatesByMtByComp - Returns the update component names for the specified machine type

    action    The action to take. This can be one of the following values.
                read - Reloads the repository files. The clears the update information in cache and reads the update file again from the repository.
                refresh - Retrieves information about the latest available firmware updates from the Lenovo Support website,
                         and stores the information to the firmware-updates repository.
                acquire - Downloads the specified firmware updates from Lenovo Support website, and stores the updates to the firmware-updates repository.
                delete - Deletes the specified firmware updates from the firmware-updates repository.
                export.not supported

     mt        comma separated machine types
     scope     scope of operation
     fixids    comma separated fixids
     type      filetype for PUT opertaion
@example 

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None

    long_short_key_map = {'key': 'k', 'action': 'a', 'mt': 'm', 'scope': 's', 'fixids': 'f', 'type':'t'}
    keylist = ['con', 'key', 'action', 'mt', 'scope', 'fixids', 'type']
    optional_keylist = ['con', 'key', 'action', 'mt', 'scope', 'fixids', 'type']
    mutually_exclusive_keys = ['key','action']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def updatecomp(*args, **kwargs):
    '''

@summary:
    Use this function to update firmware of endpoint from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = updatecomp( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
    
    USAGE:

        keylist = ['con','query','mode','action','cmm','switch','server','storage']

@param
    The parameters for this command are as follows 
    
    query   The data to return. This can be one of the following values.
                components - Returns a list of devices and components that can be updated.
                status - Returns the status and progress of firmware updates. This is the default value
    
    mode    Indicates when to activate the update. This can be one of the following values.
                immediate - Uses Immediate Activaton mode when applying firmware updates to the selected endpoints.
                delayed - Uses Delayed Activaton mode when applying firmware updates to the selected endpoints.
    
    action  The action to take. This can be one of the following values.
                apply - Applies the associated firmware to the submitted components.
                power - Perform power action on selected endpoint.
                cancelApply - Cancels the firmware update request to the selected components.

    cmm     cmms information
    switch  switch information
    server  servers information
    storage storages information

            For action = apply/cancelApply, Device information should contain following data separated by comma
                UUID - UUID of the device
                Fixid - Firmware-update ID of the target package to be applied to the component. If not provided assigned policy would be used.
                Component - Component name

            For action = power, Device information should contain following data separated by comma
                UUID - UUID of the device
                powerState - One of the power state values. Possible values per device type are
                    Server: powerOn, powerOff, powerCycleSoft, powerCycleSoftGraceful, powerOffHardGraceful
                    Switch: powerOn, powerOff, powerCycleSoft
                    CMM: reset
                    Storage:powerOff,powerCycleSoft



@example 

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None
    long_short_key_map = {'query': 'q', 'mode': 'm', 'action': 'a', 'cmm': 'c', 'switch': 'w','server':'s',
                          'storage':'t'}
    keylist = ['con', 'query','mode','action','cmm','switch','server','storage']
    optional_keylist = ['con', 'query','mode','action','cmm','switch','server','storage']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj



def users(*args, **kwargs):
    '''

@summary:
    Use this function to get users data from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = users( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','id']

@param
    The parameters for this command are as follows 
    
        id    unique ID of the user to be retrieved

@example 

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None
    long_short_key_map = {'id':'i'}
    keylist = ['con','id']
    optional_keylist = ['con', 'id']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def ffdc(*args, **kwargs):
    '''

@summary:
    Use this function to Collect and export specific endpoint data 
        from Lenovo XClarity Administrator
    
    run this function as  
    
    data_dictionary = ffdc( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','uuid']

@param
    The parameters for this command are as follows 
    
        uuid    UUID of the target endpoint

@example 

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None
    long_short_key_map = {'uuid':'u'}
    keylist = ['con','uuid']
    optional_keylist = ['con', 'uuid']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def log(*args, **kwargs):
    '''

@summary:
    Use this function to get Lenovo XClarity Administrator LOG information
    run this function as

    data_dictionary = log( key1 = 'val1', key2 = 'val2', ...)

    Where KeyList is as follows

        keylist = ['con','filter']

@param
    The parameters for this command are as follows

        filter  filter for the event

@example

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    keylist = ['lvl']

    for i in range(len(args)):
        kwargs[keylist[i]] = args[i]

    ch = shell_obj.handle_input_args(command_name, args=args, kwargs=kwargs)
    return ch

def lxcalog(*args, **kwargs):
    '''

@summary:
    Use this function to get Lenovo XClarity Administrator LOG information
    run this function as  
    
    data_dictionary = lxcalog( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','filter']

@param
    The parameters for this command are as follows 
    
        filter  filter for the event

@example 

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None

    long_short_key_map = {'filter':'f'}
    keylist = ['con','filter']
    optional_keylist = ['con', 'filter']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def jobs(*args, **kwargs):
    '''

@summary:
    Use this function to get jobs information from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = jobs( key1 = 'val1', key2 = 'val2', ...)
    
    Where KeyList is as follows
        
        keylist = ['con','id','uuid','state','cancel','delete']

@param
    The parameters for this command are as follows 
    
        id=         job id
        uuid=       uuid of endpoint for which jobs should be retrieved
        state=      job state to retrieve jobs in specified state.
                      The state can be one of the following
                      Pending
                      Running
                      Complete
                      Cancelled
                      Running_With_Errors
                      Cancelled_With_Errors
                      Stopped_With_Error
                      Interrupted
        cancel=     cancel job of specified id
        delete=     delete job of specified id

@example 

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None

    long_short_key_map = {'id': 'i', 'uuid':'u', 'state':'s','cancel':'c', 'delete':'d'}
    keylist = ['con','id','uuid','state','cancel','delete']
    optional_keylist = ['con', 'id','uuid','state','cancel','delete']
    mutually_exclusive_keys = ['id','cancel','delete']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def manifests(*args, **kwargs):
    '''

@summary:
    Use this function to send solution manifest to and retreive manifests from Lenovo XClarity Administrator
    run this function as  
    
    data_dictionary = manifests( conn_handle, input_args_dictionary{key,value} )
    
    Where KeyList is as follows
        
        keylist = [id','file']

@param
    The parameters for this command are as follows 
    
        id=         solution id
        file=       path to manifest file

@example 

    '''
    global shell_obj

    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None

    long_short_key_map = {'id':'i', 'file':'f'}
    keylist = ['con', 'id', 'file']
    optional_keylist = ['con', 'file']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    #return out_obj
    return True


def tasks(*args, **kwargs):
    '''

@summary:
    Use this function to get tasks information
    run this function as

     = tasks( con, data_dictionary)

    Where data_dictionary contain input arguments as follows

        keylist = ['jobUID','children','action', 'updateList']

@param
    The parameters for this command are as follows

    con      Connection Object to Lenovo XClarity Administrator
    jobUID          uuid of job
    children        result will include children if True
    action          cancel/update
    updateList      required for update action

@example

    '''
    global shell_obj
    con = None
    param_dict = {}

    command_name = sys._getframe().f_code.co_name

    param_dict = {}
    con = None

    long_short_key_map = {'jobUID':'j','children':'c','action':'a', 'updateList':'u'}
    keylist = ['con','jobUID','children','action', 'updateList']
    optional_keylist = ['con', 'jobUID','children','action', 'updateList']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def resourcegroups(*args, **kwargs):
    '''

@summary:
    Use this function to Create, modify, delete or read resource group from Lenovo XClarity Administrator
    run this function as

    data_dictionary = resourcegroups( con_handle,uuid, name, desc, type, solutionVPD, members, criteria )

    Where KeyList is as follows

        keylist = ['uuid', 'name','description','type','solutionVPD','members','criteria']

@param
    The parameters for this command are as follows

        uuid=         UUID of already created Group 
        name=         Name of Resource Group
        desc=         Description of Resource Group
        type=         Type of Resource Group. <{"static", "dynamic", "solution"}>,
        solutionVPD": { "id": <UUID string>,
                        "machineType": <machine type string>,
                        "model": <model string>,
                        "serialNumber": <serial number string>,
                        "manufacturer": <string>
                      },

        "members": [ "uri","uri",....],
        "criteria":[]

@example

    '''
    global shell_obj
    con = None
    param_dict = {}

    command_name = sys._getframe().f_code.co_name

    long_short_key_map = {'uuid':'u', 'name':'n','description':'d','type':'t','solutionVPD':'s',
                          'members':'m','criteria':'c'}

    keylist = ['con','uuid','name','description','type','solutionVPD','members','criteria']
    optional_keylist = ['con', 'uuid','name','description','type','solutionVPD','members','criteria']
    mutually_exclusive_keys = ['uuid', 'name']
    mandatory_options_list = {'uuid':[],'name':['type']}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)
    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys, param_dict, *args, **kwargs):
    '''
     this function will create param_dict and con from args and kwargs, param_dict will have only long options for keys,
     it will convert short option to long option key and finally validate parameters
    :param arglist: list of arguments derived from args

    :param keylist: keylist of name of fields
    :param mandatory_options_list:
    :param optional_keylist:
    :param mutually_exclusive_keys:
    :param param_dict: append to param_dict
    :return: connection object
    '''
    arglist = list(args)
    arglist = arglist[::-1]
    con = None
    for key in keylist:
        short_key = long_short_key_map.get(key)
        if (key in list(kwargs.keys())):
            param_dict[key] = kwargs[key]
        elif short_key and (short_key in list(kwargs.keys())):
            param_dict[key] = kwargs[short_key]

        elif len(arglist) >= 1:
            value = arglist.pop()
            if value != None:
                param_dict[key] = value
        elif key not in optional_keylist:
            logger.error(" Invalid Input args %s is not in optional list %s" %(key, str(mandatory_options_list)))
            raise ValueError("Invalid Input Arguments")

        if key == 'con':
            if key in param_dict:
                con = param_dict.pop(key)

    #if not con:
    #    raise AttributeError("Invalid command invocation: Connection Object missing.")

    logger.debug(" Parameter dict %s " %str(param_dict))

    me_key_found = False
    for me_key in list(param_dict.keys()):
        # Checking mandatory option_list presence
        if me_key in list(mandatory_options_list.keys()):
            if not set(mandatory_options_list[me_key]).issubset(set(param_dict.keys())):
                logger.error(" Invalid command invocation %s of mandatory list %s is not in arguments parovided" % (me_key, str(mandatory_options_list)))
                raise AttributeError("Invalid command invocation")

        # Checking mutually exclusive key presense
        if me_key in mutually_exclusive_keys:
            if me_key_found:
                logger.error(" Invalid command invocation %s of mutual exclusive list %s " % (
                me_key, str(mutually_exclusive_keys)))
                raise AttributeError("Invalid command invocation")
            me_key_found = True
    return con

def osimages(*args, **kwargs):
    '''
    @summary:
        Use this function to retrieve information about, delete, and import OS images, OS-image profiles, device driver, and boot-options files.
        data_dictionary = osimages(input_args, key=values )

        Where KeyList is as follows

            keylist = [fileName, Id, profile,remoteFileServer,imageType,jobId, ...]

    @param

        - osimages(hostplatforms)
        - osimages(hostplatforms, **kwargs)

        - osimages(osdeployment, items=[])
        - osimages(osdeployment, action=<>,mac=<>,nodeName=<>)

        - osimages(connection)

        - osimages(globalSettings)
        - osimages(globalSettings, **kwargs)

        - osimages()
        - osimages(imageType=<DUD,BOOT,OS,OSPROFILE>)

        - osimages(fileName=<>)

        - osimages(id=<>)
        - osimages(id=<>, **kwargs)

        - osimages(jobid = <>)

        - osimages(remoteFileServers)
        - osimages(remoteFileServers, **kwargs)

        - osimages(remoteFileServers, id=<>)
        - osimages(remoteFileServers, putId/deleteId=<>, **kwargs)
    @example
        osimage()                   : shows osimages
        osimage(imageType='BOOT')   : POST osimage with imageType='BOOT'
        osimages(fileName='foo')    : shows osimages for fileName='foo'
    '''

    global shell_obj
    # #con = None
    # param_dict = {}
    # command_name = sys._getframe().f_code.co_name
    #
    # # con = kwargs.get('con')
    # # if not con:
    # #     raise ValueError("Invalid Input Arguments")
    #
    # logger.info(" osimages got kwargs %s " % str(kwargs))
    # if args:
    #     kwargs['osimages_info'] = args[0]
    # #param_dict = (args, kwargs)
    # logger.info(" osimages got param_dict %s " % str(kwargs))
    # # handle_input_dict only takes param_dict as input argument
    # ch = shell_obj.handle_input_dict(command_name, con, kwargs)
    #  return ch


    con = None
    param_dict = {}

    command_name = sys._getframe().f_code.co_name

    long_short_key_map = {'osimages_info':'i'}
    keylist = ['con', 'osimages_info']
    optional_keylist = ['con', 'osimages_info']
    mutually_exclusive_keys = []
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def managementserver(*args, **kwargs):
    '''

@summary:
    Use this function to get repository info from Lenovo XClarity Administrator
    run this function as

    data_dictionary = managementserver( key1 = 'val1', key2 = 'val2', ...)

    Where KeyList is as follows

        keylist = ['con', 'key', 'fixids', 'type', 'action', 'files','jobid']

@param
    The parameters for this command are as follows

    key    Returns the specified type of update. This can be one of the following values.
                all. Returns all information. This is the default value.
                currentVersion. Returns the current version of Lenovo XClarity Administrator.
                history. Returns the history of management-server updates.
                importDir. Returns the directory for the management-server updates repository.
                size. Returns the repository size (in bytes).
                updates. Returns information about all updates packages.
                updatedDate. Returns the date when the last update was performed.

    action    The action to take. This can be one of the following values.
                apply   - install a management-server update.
                refresh - Retrieves information (metadata) about the latest available management-server updates from the Lenovo XClarity Support website.
                acquire - Downloads the specified management-server update packages from the Lenovo XClarity Support website.
                delete  - Use the DELETE method to delete update packages. - removeMetadata not supported
                import  - import fixids files

     fixids    comma separated fixids
     type      Type for Get with fixids
                changeHistory. Returns the change-history file for the specified management-server update.
                readme. Returns the readme file for the specified management-server update
     jobid     jobid for import
     files     files to be imported with fullpath and comma separated
@example

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    # some paramters don't have short options
    long_short_key_map = {'key':'k', 'fixids':'f', 'type':'t', 'action':'a','jobid':'j'}

    keylist = ['con', 'key', 'fixids', 'type', 'action', 'files','jobid']
    optional_keylist = ['con', 'key', 'fixids', 'type', 'action', 'files', 'jobid']
    mutually_exclusive_keys = ['key','action']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj

def rules(*args, **kwargs):
    '''

@summary:
    Use this function to get and set complaince rules on Lenovo XClarity Administrator
    run this function as

    data_dictionary = managementserver( key1 = 'val1', key2 = 'val2', ...)

    Where KeyList is as follows

        keylist = ['con', 'id', 'name', 'targetResourceType', 'targetGroup', 'content']

@param
    The parameters for this command are as follows


@example

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    # some paramters don't have short options
    long_short_key_map = { 'id':'i', 'name':'n', 'targetResourceType':'t', 'targetGroup':'g', 'content':'c'}

    keylist = ['con', 'id',  'name', 'targetResourceType', 'targetGroup', 'content']
    optional_keylist = ['con', 'id',  'name', 'targetResourceType', 'targetGroup', 'content']
    mutually_exclusive_keys = ['id','name']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj


def compositeResults(*args, **kwargs):
    '''

@summary:
    Use this function to get and set complaince rules on Lenovo XClarity Administrator
    run this function as

    data_dictionary = managementserver( key1 = 'val1', key2 = 'val2', ...)

    Where KeyList is as follows

        keylist = ['con', 'id', 'solutionGroup']

@param
    The parameters for this command are as follows


@example

    '''
    global shell_obj
    command_name = sys._getframe().f_code.co_name
    param_dict = {}
    con = None

    # some paramters don't have short options
    long_short_key_map = { 'id':'i', 'solutionGroup':'s'}

    keylist = ['con', 'id',  'solutionGroup']
    optional_keylist = ['con', 'id',  'solutionGroup']
    mutually_exclusive_keys = ['id','solutionGroup']
    mandatory_options_list = {}

    con = _validate_param(keylist, long_short_key_map, mandatory_options_list, optional_keylist, mutually_exclusive_keys,
                          param_dict, *args, **kwargs)

    out_obj = shell_obj.handle_input_dict(command_name, con, param_dict)
    return out_obj
