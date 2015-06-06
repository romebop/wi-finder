from sodapy import Socrata
client = Socrata("sandbox.demo.socrata.com", "FakeAppToken", username="fakeuser@somedomain.com", password="ndKS92mS01msjJKs")

client.get("/resource/nimj-3ivp.json", limit=2)

client.get("/resource/nimj-3ivp.json", where="depth > 300", order="magnitude DESC", exclude_system_fields=False)

client.get("/resource/nimj-3ivp/193.json", exclude_system_fields=False)

{u'geolocation': {u'latitude': u'21.6711', u'needs_recoding': False, u'longitude': u'142.9236'}, u'version': u'C', u':updated_at': 1348778988, u'number_of_stations': u'136', u'region': u'Mariana Islands region', u':created_meta': u'21484', u'occurred_at': u'2012-09-13T11:19:07', u':id': 193, u'source': u'us', u'depth': u'300.70', u'magnitude': u'4.4', u':meta': u'{\n}', u':updated_meta': u'21484', u':position': 193, u'earthquake_id': u'c000cmsq', u':created_at': 1348778988}  