# odoo-docker-compose
To run simply download the file "docker-compose.yml", and in a command line where this file is located run

````
docker-compose up -d
````

## (Option A:) Secure the installation (Docker Desktop GUI)
- Using Docker Desktop open the container web-1 and go to the Files tab
- using the file editor, edit the file /etc/odoo/odoo.conf
- add a line a line #3 --> list_db = False
- Save the file and closse
- restart the container

## (Option B:) Secure the installation (using the CLI)
- get the first 4-6 characters of the container called odoo-web-1 and replace the #### below with the characters
- In a command line run the following --> docker exec -it -u root #### /bin/bash
- run --> apt get update
- run --> apt install nano
- run --> nano /etc/odoo/odoo.conf
- add a line a line #3 --> list_db = False
- save/write the file
- restart the container

## Expose the web UI to the internet
- use a [CloudFlare Tunnel](https://developers.cloudflare.com/cloudflare-one)

## Remove Template Powered By odoo Branding
- Enable dev mode
- From Settings a new menu dropdown at the top appears called, Technical.
- about mid way down locate the section group called "User Interface" and select "Views"
- select "Brand Promotion Message" and the only code needed is ````<t name="Brand Promotion Message" t-name="web.brand_promotion_message"/>```` or put your own code
- save the file changes manually or nav away 

## Special notes
- There seams to be some bug that is unknown how to resolve in that you can only edite the website module locally using http://localhost
- The site is usable once configured, just not editable outside of the LAN on the internet
