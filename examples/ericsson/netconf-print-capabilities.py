import ncclient

print ncclient.__version__

from ncclient import manager

manager.logging.basicConfig(filename='ncclient.log', level=manager.logging.DEBUG)

m = manager.connect(host="10.32.66.78", port=830, username="vepc", password="vepc", hostkey_verify=False, allow_agent=False, look_for_keys=False, device_params={'name':'ericsson'})

for c in m.server_capabilities:
	print c

for c in m.client_capabilities:
	print c

m.close_session()
