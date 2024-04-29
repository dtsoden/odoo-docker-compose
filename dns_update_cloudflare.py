import requests
import json
import datetime

# Cloudflare API credentials
api_key = "Bearer ***YOUR KEY HERE***"
api_email = "***YOUR EMAIL HERE***"

# Zone ID and DNS record details
zone_id = "***YOUR ZONE_ID HERE***"
dns_record_id = "***YOUR RECORD_ID HERE***"
dns_record_type = "A"
dns_record_name = "@" # Be sure to add a CNAME record of WWW, pointing to @
dns_record_comments = "Last updated on " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Get your current IP address
def get_current_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    return ip_data['ip']

# Update the DNS record with your dynamic IP
def update_dns_record(ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record_id}"
    headers = {
        "X-Auth-Email": api_email,
        "Authorization": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "type": dns_record_type,
        "name": dns_record_name,
        "content": ip,
        "comment": dns_record_comments
    }
    response = requests.patch(url, headers=headers, data=json.dumps(data))
    return response.json()

# Main script
if __name__ == "__main__":
    current_ip = get_current_ip()
    response = update_dns_record(current_ip)
    if response['success']:
        print("DNS record updated successfully!")
    else:
        print("Failed to update DNS record:", response['errors'])
