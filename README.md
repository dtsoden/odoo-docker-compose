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

*CURRENT AS OF 4/22/2024*
| Status        | Module Name                        | Category        |
| ------------- | ---------------------------------- | --------------- |
| UPGRADE       | Studio*                            | Administration  |
| UPGRADE       | Android & iPhone                   | Administration  |
| UPGRADE       | Appraisal                          | Appraisals      |
| FREE IN CE    | Attendances                        | Attendances     |
| FREE IN CE    | Calendar                           | Calendar        |
| FREE IN CE    | Employee Contracts                 | Contracts       |
| FREE IN CE    | CRM                                | CRM             |
| FREE IN CE    | Contacts                           | CRM             |
| FREE IN CE    | Data Recycle                       | Data Cleaning   |
| FREE IN CE    | Discuss                            | Discuss         |
| FREE IN CE    | eLearning                          | eLearning       |
| FREE IN CE    | Email Marketing                    | Email Marketing |
| FREE IN CE    | SMS Marketing                      | Email Marketing |
| UPGRADE       | Marketing Automation               | Email Marketing |
| FREE IN CE    | Employees                          | Employees       |
| FREE IN CE    | Skills Management                  | Employees       |
| FREE IN CE    | Events                             | Events          |
| FREE IN CE    | Expenses                           | Expenses        |
| UPGRADE       | Field Service                      | Field Service   |
| FREE IN CE    | Fleet                              | Fleet           |
| UPGRADE       | Helpdesk                           | Helpdesk        |
| FREE IN CE    | Inventory                          | Inventory       |
| FREE IN CE    | Repairs                            | Inventory       |
| UPGRADE       | Barcode                            | Inventory       |
| FREE IN CE    | Invoicing                          | Invoicing       |
| UPGRADE       | Accounting                         | Invoicing       |
| FREE IN CE    | Live Chat                          | Live Chat       |
| FREE IN CE    | Lunch                              | Lunch           |
| FREE IN CE    | Maintenance                        | Maintenance     |
| FREE IN CE    | Manufacturing                      | Manufacturing   |
| UPGRADE       | MRP II                             | Manufacturing   |
| UPGRADE       | Quality                            | Manufacturing   |
| UPGRADE       | Product Lifecycle Management (PLM) | Manufacturing   |
| UPGRADE       | Social Marketing                   | Marketing       |
| UPGRADE       | Appointments                       | Marketing       |
| FREE IN CE    | Restaurant                         | Point of Sale   |
| FREE IN CE    | Point of Sale                      | Point of Sale   |
| UPGRADE       | Knowledge                          | Productivity    |
| FREE IN CE    | Project                            | Project         |
| UPGRADE       | Planning                           | Project         |
| FREE IN CE    | Purchase                           | Purchase        |
| FREE IN CE    | Recruitment                        | Recruitment     |
| FREE IN CE    | Sales                              | Sales           |
| UPGRADE       | Subscriptions                      | Sales           |
| UPGRADE       | VoIP                               | Sales           |
| UPGRADE       | Amazon Connector                   | Sales           |
| UPGRADE       | eBay Connector                     | Sales           |
| UPGRADE       | Sign                               | Sign            |
| FREE IN CE    | Surveys                            | Surveys         |
| FREE IN CE    | Time Off                           | Time Off        |
| UPGRADE       | Timesheets                         | Timesheets      |
| FREE IN CE    | To-Do                              | To-Do           |
| FREE IN CE    | Website                            | Website         |
| FREE IN CE    | eCommerce                          | Website         |
| FREE IN CE    | Online Jobs                        | Website         |
