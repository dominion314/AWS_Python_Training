IAM - Allows you to manage users and their level of access.

Features: Centralized control, shared access, granualr permissions, Idenitity federation like active directory or Facebook. MFA, temp access for users and devices when necessary like on phone apps. Password rotation and PCI DSS policies.

Users - end users
Groups - Users withina group inherit permissions
Policies - Policy docs in JSON give permissions to users/group/roles
Roles - Assign roles and assign them to resources. 

IAM is universal, it doesnt apply just to regions

Root account has complete admin access

New Users have no permissions when first created

New users are assigned an Access Key ID and Secret Access Keys. These are not the same as a passsowrd. 