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
				<Apn xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn">
					<apnId>{{ apnId }}</apnId>
					<msToMsUnblocked/>
					<pgwEnabled/>
					<routingInstance>vepg</routingInstance>
					<AccessRestrictions>
						<accessRestrictionsID>1</accessRestrictionsID>
						<selectionMode>public</selectionMode>
					</AccessRestrictions>
					<NameServer>
						<nameServerId>10.32.59.36</nameServerId>
						<priority>20</priority>
					</NameServer>
					<NameServer>
						<nameServerId>10.32.59.38</nameServerId>
						<priority>10</priority>
					</NameServer>
					<PdpContext>
						<pdpContextID>1</pdpContextID>
						<addressAllocation>shared-ip-pool</addressAllocation>
						<creation>blocked</creation>
						<pdpType>ipv4</pdpType>
						<sharedIpPool>telstra.internet</sharedIpPool>
						<Policing>
							<policingID>1</policingID>
							<noPolicing/>
						</Policing>
						<SessionControl>
							<sessionControlID>1</sessionControlID>
							<IdleTimeout>
								<idleTimeoutID>1</idleTimeoutID>
								<Default xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn_Pdp_SC_Idle_Def">
									<defaultID>1</defaultID>
									<measurementType>since-creation</measurementType>
									<timeout>60</timeout>
								</Default>
							</IdleTimeout>
							<SessionTimeout>
								<sessionTimeoutID>1</sessionTimeoutID>
								<Default>
									<defaultID>1</defaultID>
									<measurementType>since-creation</measurementType>
									<timeout>60</timeout>
								</Default>
							</SessionTimeout>
						</SessionControl>
					</PdpContext>
					<Radius xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn_Radius2">
						<radiusID>1</radiusID>
						<retryMethod>single-server</retryMethod>
						<reusePrimary/>
						<Accounting xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn_Rad_Accounting">
							<accountingID>1</accountingID>
							<sharedServer>Shared-Radius</sharedServer>
							<InterimUpdate>
								<interimUpdateID>1</interimUpdateID>
								<transferInterval>15</transferInterval>
								<transferOnUpdate/>
							</InterimUpdate>
							<MessageAttributes>
								<messageAttributesID>1</messageAttributesID>
								<acctInputOctets/>
								<acctInputPackets/>
								<acctOutputOctets/>
								<acctOutputPackets/>
								<apnIdentifier/>
								<apnSelectionMode/>
								<chargingCharacteristics/>
								<chargingGateway/>
								<chargingIdentifier/>
								<eventTimestamp/>
								<ggsnAddress/>
								<ggsnPlmnId/>
								<imeiSv/>
								<imsi/>
								<msTimezone/>
								<nasPort/>
								<nsapi/>
								<pdpType/>
								<ratType/>
								<sessionStop/>
								<sgsnPlmnId/>
								<signalingSgsn/>
								<userLocationInfo/>
								<userPlmnId/>
								<userValue>void</userValue>
								<Msisdn>
									<msisdnID>1</msisdnID>
								</Msisdn>
							</MessageAttributes>
						</Accounting>
					</Radius>
				</Apn>
			</Pgw>
		</Epg>
	</ManagedElement>
</config>'''

apnId = "telstra.wap"

create_template = Template(create_jinja2)

create_xml = create_template.render(apnId = apnId)
 
search_jinja2 = r'''<ManagedElement xmlns="urn:com:ericsson:ecim:ComTop">
	<managedElementId>1</managedElementId>
	<Epg xmlns="urn:com:ericsson:ecim:Epg_epg">
		<epgID>1</epgID>
		<Pgw xmlns="urn:com:ericsson:ecim:Epg_Pgw">
			<pgwID>1</pgwID>
			<Apn xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn">
				<apnId>{{ apnId }}</apnId>
			</Apn>
		</Pgw>
	</Epg>
</ManagedElement>'''

search_template = Template(search_jinja2)

search_xml = search_template.render(apnId = apnId)

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
				<Apn xmlns="urn:com:ericsson:ecim:Epg_Pgw_Apn" xc:operation="delete">
					<apnId>{{ apnId }}</apnId>
				</Apn>
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
