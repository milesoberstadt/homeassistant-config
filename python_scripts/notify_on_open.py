service_data = {"event": "ha_notify", "value1": "Watching Ginny's state..."}
hass.services.call('ifttt', 'trigger', service_data, False)

notifyCalled = False
while not notifyCalled:
    garage_state = hass.states.get('cover.left_garage_door').state
    phone_state = hass.states.get('device_tracker.ginnyotosiphone').state
    if garage_state == 'open' or phone_state == 'home':
        hass.services.call('ifttt', 'trigger', {"event": "ha_notify", "value1": "She's home!"}, False)
        notifyCalled = True
    else:
        time.sleep(5)
