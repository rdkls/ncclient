"""
Handler for Huawei device specific information.

Note that for proper import, the classname has to be:

    "<Devicename>DeviceHandler"

...where <Devicename> is something like "Default", "Huawei", etc.

All device-specific handlers derive from the DefaultDeviceHandler, which implements the
generic information needed for interaction with a Netconf server.

"""
#from ncclient.operations.third_party.ericsson.rpc import *

from ncclient.xml_ import BASE_NS_1_0

from .default import DefaultDeviceHandler

class EricssonDeviceHandler(DefaultDeviceHandler):
    """
    Ericsson handler for device specific information.
    """
    _EXEMPT_ERRORS = []


    def __init__(self, device_params):
        super(EricssonDeviceHandler, self).__init__(device_params)
        
        
    # TODO: Implement Ericsson specific operations

    #def add_additional_operations(self):
    #    dict = {}
    #    dict["cli"] = CLI
    #    dict["action"] = Action
    #    return dict


    def get_capabilities(self):
        c = [
            'urn:ietf:params:netconf:base:1.0',
            'urn:com:ericsson:ebase:0.1.0',
            'urn:com:ericsson:ebase:1.1.0',
            'urn:com:ericsson:ebase:1.2.0',
            'urn:ietf:params:netconf:capability:writable-running:1.0',
            'urn:ietf:params:netconf:capability:rollback-on-error:1.0',
            'urn:ietf:params:netconf:capability:notification:1.0',
            'urn:ericsson:com:netconf:action:1.0',
            'urn:ericsson:com:netconf:heartbeat:1.0',
            'urn:com:ericsson:netconf:operation:1.0',
            'urn:ietf:params:netconf:capability:startup:1.0',
            'urn:com:ericsson:ipos:exec-cli:1.0',
            'urn:com:ericsson:ipos:invoke-cli:1.0'
        ]

        return c


    def perform_qualify_check(self):
        return False

    # These functions were added to remove namespace from RPC as MME does
    # accept them and returns a 'bad-request' response

    def get_xml_base_namespace_dict(self):
        return {None: BASE_NS_1_0}


    def get_xml_extra_prefix_kwargs(self):
        d = self.get_xml_base_namespace_dict()
        return {"nsmap": d}
    
