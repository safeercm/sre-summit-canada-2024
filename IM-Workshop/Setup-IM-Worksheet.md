# SRE Summit Canada 2024 - 
# Incident Management Workshop - Part One
# Setup Incident Management Process

Based on the Incident Management Checklist and the background information ( refer [README](README.md)), create documents for the checklist items given below.  An example items is added in every checklist for reference 

## 1a. Critical Functions of Business.  

Typically a critical  business function will be served by one domain, but to complete the functionality it will have to depend on components from other domains.  While it is good to be able to associate functions with domains and BUs, in the absence of such constructs within the org, it is also ok to start with just functions and the team that is primarily responsible for the function.



| Function | Primary Domain | Domain dependency list | Owner Team/Business Unit |
|---|---|---|---|
| Checkout a chosen product ( that is already added to the shopping cart ) | Checkout | Checkout, Inventory, Payment | Cart and Checkout Team |
|<br>||||
|<br>||||

## 1b. Component/Service List

Create a list of components with ownership information.  Make logical assumptions on the components that are part of each domain

|Component Name|Type|Stateful/Stateless|Owner|
|---|---|---|---|
|catalog-api|REST API|Stateless|Catalog Backend Team|
|<br>||||
|<br>||||

## 1c. Oncall Calendar and Escalation Matrix 

Ideally there should be tools for oncall calendar and  alerting.  But if the org/team are at early stages in SRE/IM maturity, the following should help as a reference.


### Catalog Backend Team - Oncall 
| | | |
|---|---|---|
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   |Week of 17-June-2024&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Week of 24 June 2024&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |

|   |  |  | | | | | | | | | | | ||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | 17 | 18 |19 |20 |21 |22 |23 |24 |25 |26 |27 |28 |29 |30|
| Jon Doe | | | | | | | |x|x|x|x|x|x|x|
| Foo Bar |x|x|x|x|x|x|x| | | | | | | |
| Jane Doe| | | | | | | | | | | | | | |
| <br>| | | | | | | | | | | | | | |

### Escalation Matrix

|Level|Name|Role|
|---|---|---|
|Level 1|Adam|Manager|
|Level 2|Jacob|Sr Manager|


## 1d. Categorize services into tiers.

This table can be merged with service ownership table from 1b


|Service Name|Tier|
|---|---|
|K8S-as-a-Service|Tier 0|
|Payment|Tier 0|
|Shipping|Tier 1|
|<br>| |
|<br>| |


## 1e.  Incident Classification

Think of potential incident scenarios that can occur in this e-commerce infrastructure and categorize them as Sev-0, Sev-1.  Feel free to add more severity levels 

|Sev 0|Sev 1|
|---|---|
|Unable to checkout products that are added to the cart already|User signup is not working|
|Data corruption impacting all users from a big geographical area|Credit card payment not working for only one bank|
|<br>||
|<br>||

