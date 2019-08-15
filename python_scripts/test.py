service_data = {"event": "ha_notify", "value1": "Test"}
hass.services.call('ifttt', 'trigger', service_data, False)