import requests
from bs4 import BeautifulSoup
import json
import argparse
import os

#Get confluence url and application name
argparser = argparse.ArgumentParser(prog='service-getter',
                                    description='To read table content from confluence page and providing output to jenkins pipeline')
argparser.add_argument('-u', '--url', type=str, metavar='', required=True, help='url to access confluence page')
argparser.add_argument('-t', '--table_index', type=str, metavar='', required=True, help='Table index to read from confluence page')
argparser.add_argument('-p', '--column_app', type=str, metavar='', required=True, help='Table application header name to read from confluence page')
argparser.add_argument('-s', '--column_service', type=str, metavar='', required=True, help='Table service name header to read from confluence page')
argparser.add_argument('-a', '--appname', type=str, metavar='', required=True, help='Application name')

args = argparser.parse_args()
confluence_rest_api = args.url
table_index = args.table_index
column_app = args.column_app
column_service = args.column_service
application_name = args.appname

# Confluence Username and Apitoken
username = os.environ["CONFLUENCE_USERNAME"]
confluence_apitoken = os.environ["CONFLUENCE_APITOKEN"]

def get_confluence_page_html(username, confluence_apitoken):
    """Get the confluence page to read the table data.

    Args:
        username (str) : email id
        confluence_apitoken (str) : confluence api token
        
    Returns:
        page_body : confluence page body where table resides
    """
    params = {"expand": "body.view"}
    auth = (username, confluence_apitoken)

    response = requests.get(confluence_rest_api, params=params, auth=auth)
    if response.status_code == 200:
        data = response.json()
        storage_content = data.get("body", {}).get("storage", {}).get("value", "")
        page_body = decode_confluence_storage(storage_content)
        return page_body
    else:
        print(
            f"Failed to retrieve Confluence page. Status code: {response.status_code}"
        )
        return None

def decode_confluence_storage(storage_content):
    """Get the decode confluence storage data.

    Args:
        storage_content (str) :html parser
          
    Returns:
        soup : decode html parser confluence storage.
    """
    soup = BeautifulSoup(storage_content, "html.parser")
    return str(soup)

def extract_table_data(html_content):
    """Get the table data.

    Args:
        html_content (str) : content of html
          
    Returns:
        table_data : Extract table data as a list.
    """  
    soup = BeautifulSoup(html_content, "html.parser")
    tables = soup.find_all("table")
    table = None
    index = int(table_index)
    if index < len(tables):
        table = tables[index]
    
    if table:
        # Extract table data as a list of lists
        table_data = []
        header = [th.get_text(strip=True) for th in table.find_all('th')]
        # for row in table.find_all("tr"):
        for row in table.find_all('tr')[1:]:
            # row_data = [
                # cell.get_text(strip=True) for cell in row.find_all(["td", "th"])
            row_data = [str(td) for td in row.find_all(['td', 'th'])]
            # table_data.append(row_data)
            table_data.append(dict(zip(header, row_data)))
        return table_data
    else:
        print("No table found on the Confluence page.")
        return None

def clean_text(text):
    """Remove HTML tags and additional characters
  
    Returns:
        Data with no paragraphs, line breaks, and additional HTML tags
    """    
    # Remove HTML tags
    cleaned_text = BeautifulSoup(text, 'html.parser').get_text(separator=' ')
    # Remove additional characters
    cleaned_text = cleaned_text.replace('<br/>', '').replace('<p>', '').replace('</p>', '').replace('</td>', '').strip()
    return cleaned_text


def find_service_name(table_data, target_application_name, applications_key, service_name_key):
    """Get the service name from confluence page table

    Args:
        table_data (list): List of dictionaries representing the table data from confluence
        target_application_name (str): The name of the application to search for
        applications_key (str): Key for the 'Applications' column in the table_data
        service_name_key (str): Key for the 'ServiceName' column in the table_data

    Returns:
        dict: A dictionary containing the application name as key and the corresponding service names as value
    """
    app_source = {}
    for row in table_data:
        # Check if applications_key is present in the row
        if applications_key  in row:
            application_name = row[applications_key]
            if target_application_name.lower() in application_name.lower():
                # Clean application name
                application_name = clean_text(application_name)

                # Check if service_name_key key is present in the row
                if service_name_key in row:
                    service_name_data = row[service_name_key]
                    # Extract service names and corresponding values
                    service_names = [item.split(':') for item in service_name_data.split('<p>') if ':' in item]
                    service_data = {name.strip(): clean_text(value) for name, value in service_names if len(name) > 0 and len(value) > 0}
                    
                    app_source[application_name] = service_data
    return app_source

#  To get confluence page data
html_content = get_confluence_page_html(username, confluence_apitoken)

def write_service_output(service_names):
    """
    Write the service names to an output file in JSON format.

    Args:
        service_names (list): A list of service names.

    Returns:
        None
    """
    with open('output.json', 'w') as f:
        json.dump(service_names, f)
        # print(json.dumps(service_names, indent=2))

if html_content:
    table_data = extract_table_data(html_content)
    if table_data:
        service_names = find_service_name(table_data, application_name, column_app, column_service) 
        if service_names:
            write_service_output(service_names)

            # Read the content of the JSON file
            json_file_path = 'service-job-mapping.json'
            with open(json_file_path, 'r') as file:
                service_mapping = json.load(file)

            # Extract jobs from service_names
            service_names_data = service_names[application_name]
            # Create a list to store the updated service_mapping entries

            updated_service_mapping = []
            # Update the 'version' field in the JSON with corresponding version from service_names_data
            for service_name, version in service_names_data.items():
                # Check if the service_name is present in service_mapping
                if service_name in service_mapping:
                    # Check if 'parameters' is present before updating 'version'
                    if 'parameters' in service_mapping[service_name]:
                        service_mapping[service_name]['parameters']['version'] = version
                    # Remove the outer key and append to the list
                    updated_service_mapping.append(service_mapping[service_name])

            # print(f"service_mapping  {service_mapping}")
            # print(f"updated_service_mapping  {updated_service_mapping}")

            # Print the updated JSON content
            # updated_json_content = json.dumps(updated_service_mapping, indent=2)
            updated_json_content = json.dumps(service_mapping, indent=2)
            print(updated_json_content)

            # version updated accordingly 
            with open('jobs.json', 'w') as updated_file:
                updated_file.write(updated_json_content)

        else:
            print(f"Applications / Service names not found ")
