from jinja2 import Template

from ncclient import manager

manager.logging.basicConfig(filename='ncclient.log', level=manager.logging.DEBUG)

create_jinja2 = r'''<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
	<ManagedElement xmlns="urn:com:ericsson:ecim:ComTop">
		<managedElementId>1</managedElementId>
		<Epg xmlns="urn:com:ericsson:ecim:Epg_epg">
			<epgID>1</epgID>
			<Pgw xmlns="urn:com:ericsson:ecim:Epg_Pgw">
				<pgwID>1</pgwID>
				<LogicalApn xmlns="urn:com:ericsson:ecim:Epg_Pgw_LogicalApn">
					<logicalApnId>{{ logicalApnId }}</logicalApnId>
					<AccessRestrictions>
						<accessRestrictionsID>1</accessRestrictionsID>
						<selectionMode>public</selectionMode>
					</AccessRestrictions>
					<Apn>
						<apnID>1</apnID>
						<default>{{ apnId }}</default>
					</Apn>
				</LogicalApn>
			</Pgw>
		</Epg>
	</ManagedElement>
</config>'''

logicalApnId = "npv3.telstra.wap"
apnId = "telstra.wap"

create_template = Template(create_jinja2)

create_xml = create_template.render(apnId = apnId, logicalApnId = logicalApnId)
 
search_jinja2 = r'''<ManagedElement xmlns="urn:com:ericsson:ecim:ComTop">
	<Epg xmlns="urn:com:ericsson:ecim:Epg_epg">
		<epgID>1</epgID>
		<Pgw xmlns="urn:com:ericsson:ecim:Epg_Pgw">
			<pgwID>1</pgwID>
			<LogicalApn xmlns="urn:com:ericsson:ecim:Epg_Pgw_LogicalApn">
				<logicalApnId>{{ logicalApnId }}</logicalApnId>
			</LogicalApn>
		</Pgw>
	</Epg>
</ManagedElement>'''

search_template = Template(search_jinja2)

search_xml = search_template.render(logicalApnId = logicalApnId)

m = manager.connect(host="10.32.66.78", port=830, username="vepc", password="vepc", hostkey_verify=False, allow_agent=False, look_for_keys=False)

a = m.get_config('running', ('subtree', search_xml)) 

try:
	print a.data_xml
except:
	print "Not Found"

a = m.edit_config(target = 'running', config = create_xml) 

print a

a = m.get_config('running', ('subtree', search_xml)) 

try:
	print a.data_xml
except:
	print "Not Found"

delete_jinja2 = r'''<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
	<ManagedElement xmlns="urn:com:ericsson:ecim:ComTop">
		<managedElementId>1</managedElementId>
		<Epg xmlns="urn:com:ericsson:ecim:Epg_epg">
			<epgID>1</epgID>
			<Pgw xmlns="urn:com:ericsson:ecim:Epg_Pgw">
				<pgwID>1</pgwID>
				<LogicalApn xmlns="urn:com:ericsson:ecim:Epg_Pgw_LogicalApn" xc:operation="delete">
					<logicalApnId>{{ logicalApnId }}</logicalApnId>
				</LogicalApn>
			</Pgw>
		</Epg>
	</ManagedElement>
</config>'''

delete_template = Template(delete_jinja2)

delete_xml = delete_template.render(logicalApnId = logicalApnId)

a = m.edit_config(target = 'running', config = delete_xml) 

print a

a = m.get_config('running', ('subtree', search_xml)) 

try:
	print a.data_xml
except:
	print "Not Found"
