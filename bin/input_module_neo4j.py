
# encoding = utf-8

import os
import sys
import time
import datetime
import base64    

'''
    IMPORTANT
    Edit only the validate_input and collect_events functions.
    Do not edit any other part in this file.
    This file is generated only once when creating
    the modular input.
'''
def validate_input(helper, definition):
    """Implement your own validation logic to validate the input stanza configurations"""
    # This example accesses the modular input variable
    # strURI = definition.parameters.get('strURI', None)
    # strQuery = definition.parameters.get('strQuery', None)
    pass

def collect_events(helper, inputs, ew):
    """Implement your data collection logic here"""
    # The following example accesses the configurations and arguments
    # Get the arguments of this input
    # opt_strURI = helper.get_arg('strURI')
    # opt_strQuery = helper.get_arg('strQuery')
    # Get options from setup page configuration
    # Get the loglevel from the setup page
    # loglevel = helper.get_log_level()
    # Proxy setting configuration
    # proxy_settings = helper.get_proxy()
    # User credentials
    # account = helper.get_user_credential("username")
    # Global variable configuration
    # global_userdefined_global_var = helper.get_global_setting("userdefined_global_var")
    # Write to the log for this modular input
    # helper.log_error("log message")
    # helper.log_info("log message")
    # helper.log_debug("log message")
    # Set the log level for this modular input
    # helper.set_log_level('debug')
    # helper.set_log_level('info')
    # helper.set_log_level('warning')
    # helper.set_log_level('error')
    # helper function to send http request
    url = '''http://localhost:7474/db/data/cypher'''
    method = 'post'
    payload = ''' 
    {"query": "match (n) return n"}
    '''
    headers = {"Accept": "application/json; charset=UTF-8", "Content-Type": "application/json"}
    auth = base64.b64encode('neo4j'+':'+'password')
    headers['Authorization']="Basic "+auth

    
    response = helper.send_http_request(url, method, parameters=None, payload=payload,
                             headers=headers, cookies=None, verify=True, cert=None, timeout=30, use_proxy=False)
    r_headers = response.headers
    r_text = response.text
    helper.log_info('text:'+r_text)
    r_json = response.json()
    r_cookies = response.cookies
    historical_responses = response.history
    r_status = response.status_code
    response.raise_for_status()

    event = helper.new_event(source=helper.get_input_name(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=r_text)
    try:
        ew.write_event(event)
    except Exception as e:
        raise e
    
    # response = helper.send_http_request(url, method, parameters=None, payload=None,
    #                          headers=None, cookies=None, verify=True, cert=None, timeout=None, use_proxy=True)
    # get the response headers
    # r_headers = response.headers
    # get the response body as text
    # r_text = response.text
    # get response body as json. If the body text is not a json string, raise a ValueError
    # r_json = response.json()
    # get response cookies
    # r_cookies = response.cookies
    # get redirect history
    # historical_responses = response.history
    # get response status code
    # r_status = response.status_code
    # check the response status, if the status is not sucessful, raise requests.HTTPError
    # response.raise_for_status()
    #
    # checkpoint related helper functions
    # save checkpoint
    # helper.save_check_point(key, state)
    # delete checkpoint
    # helper.delete_check_point(key)
    # get checkpoint
    # state = helper.get_check_point(key)
    #

    '''
    # The following example writes a random number as an event
    import random
    data = str(random.randint(0,100))
    event = helper.new_event(source=helper.get_input_name(), index=helper.get_output_index(), sourcetype=helper.get_sourcetype(), data=data)
    try:
        ew.write_event(event)
    except Exception as e:
        raise e
    '''
