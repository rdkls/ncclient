from ncclient import manager

manager.logging.basicConfig(filename='ncclient.log', level=manager.logging.DEBUG)

m = manager.connect(host="10.32.66.78", port=830, username="vepc", password="vepc", hostkey_verify=False, allow_agent=False, look_for_keys=False)

a = m.get_config('running')

print a.data_xml

m.close_session()
