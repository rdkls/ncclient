from ncclient import manager

manager.logging.basicConfig(filename='ncclient.log', level=manager.logging.DEBUG)

m = manager.connect(host="10.32.66.78", port=830, username="vepc", password="vepc", hostkey_verify=False, allow_agent=False, look_for_keys=False, device_params={'name':'ericsson'})

a = m.get_config('running', ('subtree', '<ManagedElement xmlns="urn:com:ericsson:ecim:ComTop"><managedElementId>1</managedElementId><Epg xmlns="urn:com:ericsson:ecim:Epg_epg"><epgID>1</epgID><Pgw xmlns="urn:com:ericsson:ecim:Epg_Pgw"><pgwID>1</pgwID><Apn xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn"><apnId>telstra.internet</apnId></Apn></Pgw></Epg></ManagedElement>'))

print a.data_xml

a = m.edit_config(target='running', config='<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0"><ManagedElement xmlns="urn:com:ericsson:ecim:ComTop"><managedElementId>1</managedElementId><Epg xmlns="urn:com:ericsson:ecim:Epg_epg"><epgID>1</epgID><Pgw xmlns="urn:com:ericsson:ecim:Epg_Pgw"><pgwID>1</pgwID><Apn xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn"><apnId>telstra.internet</apnId><PdpContext><pdpContextID>1</pdpContextID><creation>blocked</creation></PdpContext></Apn></Pgw></Epg></ManagedElement></config>')

#print a.xml

a = m.get_config('running', ('subtree', '<ManagedElement xmlns="urn:com:ericsson:ecim:ComTop"><managedElementId>1</managedElementId><Epg xmlns="urn:com:ericsson:ecim:Epg_epg"><epgID>1</epgID><Pgw xmlns="urn:com:ericsson:ecim:Epg_Pgw"><pgwID>1</pgwID><Apn xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn"><apnId>telstra.internet</apnId></Apn></Pgw></Epg></ManagedElement>'))

#print a.xml

a = m.edit_config(target='running', config='<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0"><ManagedElement xmlns="urn:com:ericsson:ecim:ComTop"><managedElementId>1</managedElementId><Epg xmlns="urn:com:ericsson:ecim:Epg_epg"><epgID>1</epgID><Pgw xmlns="urn:com:ericsson:ecim:Epg_Pgw"><pgwID>1</pgwID><Apn xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn"><apnId>telstra.internet</apnId><PdpContext><pdpContextID>1</pdpContextID><creation>unblocked</creation></PdpContext></Apn></Pgw></Epg></ManagedElement></config>')

#print a.xml

m.close_session()
