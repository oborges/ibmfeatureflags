from ibm_appconfiguration import AppConfiguration, Feature, Property, ConfigurationType
app_configuration_client = AppConfiguration.get_instance()
app_configuration_client.init(region='us-south',
               guid='2863271a-cfa1-44ff-8cd0-89b21c61cc0a',
               apikey='PEsQkYW90e520ZAwpUnvYCDn3GGP8HQ7nHdJILyw1bB4')

## Initialize configurations 
app_configuration_client.set_context(collection_id='studycase4-collection', environment_id='dev')


mockbackend = app_configuration_client.get_feature('mockbackend')

if mockbackend.is_enabled():
    print("The backend is MOCKED")
else:
    print("The backend is NOT mocked")


