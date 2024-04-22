# odoo-docker-compose
To run simply download the file [docker-compose.yml](https://raw.github.com/dtsoden/odoo-docker-compose/main/docker-compose.yml), and in a command line where this file is located run

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
- REMOVE POWERED BY on the login box
- locate "Login Layout"
- remove or comment out line 19 ````<a href="https://www.odoo.com?utm_source=db&amp;utm_medium=auth" target="_blank">Powered by <span>Odoo</span></a>````
- dissable dev mode

## Special notes
- There seams to be some bug that is unknown how to resolve in that you can only edite the website module locally using http://localhost
- The site is usable once configured, just not editable outside of the LAN on the internet

## The Community Edition is good for most things, but not every thing 

Here is a matrix of what you can install in the Community Edition.
Uninstallable means you need the paid Enterprise editions and Studio* or on-prem installs need the most expensive upgrade.
See [Odoo Pricing](https://www.odoo.com/pricing-plan) for full details.

| Status        | Module Name                        | Category        |
| ------------- | ---------------------------------- | --------------- |
| Uninstallable | Studio*                            | Administration  |
| Uninstallable | Android & iPhone                   | Administration  |
| Uninstallable | Appraisal                          | Appraisals      |
| Not Installed | Attendances                        | Attendances     |
| Not Installed | Calendar                           | Calendar        |
| Not Installed | Employee Contracts                 | Contracts       |
| Not Installed | CRM                                | CRM             |
| Not Installed | Contacts                           | CRM             |
| Not Installed | Data Recycle                       | Data Cleaning   |
| Not Installed | Discuss                            | Discuss         |
| Not Installed | eLearning                          | eLearning       |
| Not Installed | Email Marketing                    | Email Marketing |
| Not Installed | SMS Marketing                      | Email Marketing |
| Uninstallable | Marketing Automation               | Email Marketing |
| Not Installed | Employees                          | Employees       |
| Not Installed | Skills Management                  | Employees       |
| Not Installed | Events                             | Events          |
| Not Installed | Expenses                           | Expenses        |
| Uninstallable | Field Service                      | Field Service   |
| Not Installed | Fleet                              | Fleet           |
| Uninstallable | Helpdesk                           | Helpdesk        |
| Not Installed | Inventory                          | Inventory       |
| Not Installed | Repairs                            | Inventory       |
| Uninstallable | Barcode                            | Inventory       |
| Not Installed | Invoicing                          | Invoicing       |
| Uninstallable | Accounting                         | Invoicing       |
| Not Installed | Live Chat                          | Live Chat       |
| Not Installed | Lunch                              | Lunch           |
| Not Installed | Maintenance                        | Maintenance     |
| Not Installed | Manufacturing                      | Manufacturing   |
| Uninstallable | MRP II                             | Manufacturing   |
| Uninstallable | Quality                            | Manufacturing   |
| Uninstallable | Product Lifecycle Management (PLM) | Manufacturing   |
| Uninstallable | Social Marketing                   | Marketing       |
| Uninstallable | Appointments                       | Marketing       |
| Not Installed | Restaurant                         | Point of Sale   |
| Not Installed | Point of Sale                      | Point of Sale   |
| Uninstallable | Knowledge                          | Productivity    |
| Not Installed | Project                            | Project         |
| Uninstallable | Planning                           | Project         |
| Not Installed | Purchase                           | Purchase        |
| Not Installed | Recruitment                        | Recruitment     |
| Not Installed | Sales                              | Sales           |
| Uninstallable | Subscriptions                      | Sales           |
| Uninstallable | VoIP                               | Sales           |
| Uninstallable | Amazon Connector                   | Sales           |
| Uninstallable | eBay Connector                     | Sales           |
| Uninstallable | Sign                               | Sign            |
| Not Installed | Surveys                            | Surveys         |
| Not Installed | Time Off                           | Time Off        |
| Uninstallable | Timesheets                         | Timesheets      |
| Not Installed | To-Do                              | To-Do           |
| Not Installed | Website                            | Website         |
| Not Installed | eCommerce                          | Website         |
| Not Installed | Online Jobs                        | Website         |
