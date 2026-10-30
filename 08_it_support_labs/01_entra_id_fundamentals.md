# Microsoft Entra ID Fundamentals: Users, Groups, Roles and MFA

> Study notes and hands-on lab log · Date: 2026-10-30
> Sources: Microsoft Learn ("What is Microsoft Entra ID?", "Manage users and groups in Microsoft Entra ID") and my own lab tenant.
> Note: This is a learning record. Things I did **not** do or did **not** verify are listed explicitly in sections 10 and 11.

---

## 1. Goal and scenario

**Learning goal:** Understand how a company manages user accounts and access, and be able to explain it in English in an IT support interview.

**Scenario used for study:**
A new warehouse employee starts on Monday. They need access to Microsoft 365, but they must **not** get administrator rights.

**Key idea:** *Just enough access* (least privilege). Give people only the permissions they need for their job, and no more.

---

## 2. What is Microsoft Entra ID?

- Microsoft Entra ID (formerly **Azure Active Directory / Azure AD**) is Microsoft's cloud-based **identity and access management (IAM)** service.
- It provides authentication, policy enforcement and protection for users, devices, apps and resources.
- Microsoft 365, Azure, Intune and Dynamics 365 all use the same Entra ID directory to sign users in.
- Features it provides include **single sign-on (SSO)** and **multifactor authentication (MFA)**.

### Active Directory (AD DS) vs Entra ID

| | Active Directory (AD DS) | Microsoft Entra ID |
|---|---|---|
| Location | On-premises servers | Cloud |
| Structure | Domains, OUs, Group Policy | Flat structure, no OUs |
| Device settings | Group Policy | Intune (device management) |
| Protocols | Kerberos, NTLM, LDAP | SAML, OAuth 2.0, OpenID Connect |
| Typical use | Office PCs, file servers | Microsoft 365 and SaaS apps |

- Entra ID can work **without** an on-premises AD (small companies often do this).
- Many companies use both. This is called a **hybrid** environment.

### Hybrid identity: Microsoft Entra Connect

- A free tool that **synchronizes** an on-premises AD with Entra ID.
- Users can then use **one identity** for both on-premises resources and cloud apps.
- Components: sync services, health monitoring, AD FS (optional, for complex setups), and two sign-in methods:
  - **Password hash synchronization (PHS):** a hash of the password is copied to the cloud; the cloud checks the login.
  - **Pass-through authentication (PTA):** the login request is passed to the on-premises AD, which checks the password.
- It replaced older tools (DirSync, Azure AD Sync).
- Installing it needs planning and is not a trivial task.

---

## 3. Tenant, directory and subscription

- **Tenant = Directory:** a company's dedicated identity database (users, groups, roles).
- **Subscription:** a billing agreement for Azure services.
- Relationship:
  - One subscription trusts **exactly one** directory.
  - One directory can have **many** subscriptions (many-to-one).
- An organization can have more than one directory (for example, a separate one for testing).
- Analogy: the directory is the employee list; subscriptions are department credit cards that all rely on the same list.
- When creating a directory, the country/region cannot be changed later. The initial domain looks like `name.onmicrosoft.com`.

---

## 4. Users

**User types (as shown in the Learn module):**

| Type | Description |
|---|---|
| Cloud identity | Created directly in Entra ID (for example, a new warehouse employee) |
| Directory-synchronized | Synced from on-premises AD through Entra Connect |
| Guest | External person (vendor, contractor, consultant), invited by email, limited access |

**Ways to create users:**
1. Sync from on-premises AD (Entra Connect)
2. Microsoft Entra admin center (web GUI), best for one or a few users
3. Command line (PowerShell / Azure CLI), best for bulk creation, often with a **CSV** file
4. Microsoft Graph API (automation)

**Good practices**
- Use a naming convention for user names.
- Generate random temporary passwords and require a change at first sign-in.
- Remove access immediately when someone leaves (**offboarding**).
- Creating users requires an admin role such as **User Administrator**.

---

## 5. Groups

- **Security group:** gives a set of users access to resources. The most common type.
- **Microsoft 365 group:** for collaboration (shared mailbox, calendar, SharePoint, Teams). Can include external people.

**Membership types**

| Type | How it works | License needed |
|---|---|---|
| Assigned | Admin adds and removes members manually | Free |
| Dynamic user | Rule-based (for example, `department = Warehouse`); members are added and removed automatically | **P1** |
| Dynamic device | Rule-based on device attributes | **P1** |

**Principle:** assign permissions to **role-based groups** (based on job duties), not to individuals.
This is faster, less error-prone, easier to audit and easier to clean up when people change roles or leave.

---

## 6. Licenses

| Plan | Notes |
|---|---|
| Entra ID Free | Included with Microsoft 365 / Azure. Users, groups, basic sign-in |
| Entra ID P1 (paid) | Adds dynamic groups, Conditional Access, group-based license assignment, custom roles (per the Learn module) |
| Entra ID P2 (paid) | P1 plus advanced protection and governance features |

- Microsoft 365 Business Premium includes Entra ID P1.
- **Conditional Access** = policies that require things like MFA depending on conditions (needs P1).
- In my Free lab tenant, license assignment is done in the **Microsoft 365 admin center**, not in the Entra admin center, and it needs a Microsoft 365 subscription.

---

## 7. Roles and access control

**Two separate systems (easy to confuse):**
- **Microsoft Entra roles** (directory roles): manage the identity system itself, for example **Global Administrator**, **User Administrator**.
- **Azure roles (Azure RBAC):** manage Azure resources such as servers and storage, for example **Owner**, **Contributor**, **Reader**.

**Azure RBAC built-in roles**

| Role | Can do |
|---|---|
| Owner | Manage everything **and** grant access to others |
| Contributor | Create and manage everything, but **cannot** grant access |
| Reader | View only |

**Role definition basics (Azure)**
- `Actions`: allowed management operations
- `NotActions`: operations **subtracted** from `Actions` (not a deny rule)
- `DataActions`: allowed operations on the data itself (for example, reading a file)
- `AssignableScopes` / **scope**: where the role can be applied (subscription → resource group → single resource). A longer scope path means a narrower scope.
- `IsCustom`: whether the role is a custom role or a built-in one
- **RBAC** = Role-Based Access Control. Custom roles require P1 or P2 (per the Learn module).

**Security concepts**
- **Least privilege:** give only what is needed for the job.
- **Blast radius:** how much damage a compromised account can cause. Smaller permissions mean a smaller blast radius.
- **Authentication** (who you are) comes before **authorization** (what you may do). In IT English, use *permissions* or *access* rather than "authority".

**Important nuance:** having **0 admin roles** does not mean having no permissions. Every member user still has default user permissions (for example, viewing their own profile).

---

## 8. MFA

- MFA = password **plus** a second verification method (for example, an authenticator app).
- The administrator **requires** MFA; the employee **registers** a method.
- Options in Entra: Security defaults (basic, for Free tenants) or Conditional Access (flexible, needs P1). I observed the registration prompt but did not verify which one my tenant uses (see section 11).

---

## 9. Scenario answer: new warehouse employee

1. Confirm the request with the manager and HR, and check the job duties.
2. Create the user account following the naming convention.
3. Add the user to a **role-based group** (for example, "Warehouse Staff").
4. Assign a Microsoft 365 license (ideally through the group).
5. Require MFA so the employee registers a second sign-in method.
6. Do **not** assign any admin role (least privilege).
7. Document everything in a ticket and escalate issues to management.

**Why not give Global Administrator?** The employee could change important settings by mistake, and if the account were compromised, an attacker would gain full control of the whole tenant.

---

## 10. Hands-on lab log (what I actually did)

Environment: personal Azure account, Entra ID **Free** tenant (the Microsoft 365 Developer Program sandbox was not available to me).

- Registered MFA (Microsoft Authenticator) for my own admin account.
- Created the user `warehouse_test` (type: Member) with job title and department, **no roles**.
- Created a **Security** group `Warehouse Staff` (membership type: **Assigned**) and added `warehouse_test`.
- Checked the user overview: group memberships = 1, assigned roles = **0**, assigned licenses = 0.
- Opened the user's Licenses page: assignment is only possible in the Microsoft 365 admin center.
- Signed in as `warehouse_test` in a private browser window:
  - first sign-in forced a **password update**;
  - then Microsoft asked the user to **register MFA** (Install Microsoft Authenticator).

I stopped at the MFA registration prompt.

---

## 11. What I did not do / still unclear

**Not done**
- Assigning a Microsoft 365 license (no Microsoft 365 subscription in the lab tenant).
- Completing MFA registration for the test user.
- Dynamic groups, Conditional Access and bulk creation with PowerShell/CSV (concepts only).

**Not verified yet**
- Whether Security defaults is turned on in my tenant, and the exact grace period for MFA registration.
- Whether a deleted user can be restored, and for how long (check **Deleted users** in the admin center).
- The practical difference between Global Administrator and User Administrator (compare in **Roles & administrators**).

**Still confusing**
- Azure roles vs Entra roles.
- Security defaults vs Conditional Access.

---

## 12. Interview practice (draft answers, to be rewritten in my own words)

**Q: What is the difference between a user, a group and a role in Entra ID?**
A user is one person's account. A group is a set of users who do similar work, and we give access to the group, not to each person. A role is a set of admin permissions, such as creating accounts. A new employee should not get an admin role unless the job requires it.

**Q: A new warehouse employee starts on Monday. How would you set up their account?**
First, I would confirm the request with the manager and HR and check the job duties. Then I would create the account following the naming convention and add it to a role-based group. Through that group I would assign a Microsoft 365 license, and I would require MFA. I would not assign any admin roles, and I would document everything in a ticket.

**Q: How would you create 100 accounts at once?**
I would prepare a CSV file and use PowerShell or Azure CLI to create the users in bulk, with random temporary passwords and a forced password change at first sign-in.

**Q: Why not just give everyone Global Administrator?**
Too many permissions increase the risk of accidental changes and make a compromised account much more dangerous.

**Q: A consultant needs Teams for three months. What do you do?**
I would invite them as a guest user with limited access, and remove the account when the contract ends.

---

## 13. Next steps

1. Check whether Security defaults is enabled (Entra admin center → Overview → Properties).
2. Compare **Global Administrator** and **User Administrator** in Roles & administrators.
3. Test deleting and restoring a lab user (Deleted users).
4. Finish the Learn module "Secure Microsoft Entra users with multifactor authentication".
5. Re-answer the interview questions aloud without notes.

---

## References

- [What is Microsoft Entra ID? (Microsoft Learn)](https://learn.microsoft.com/entra/fundamentals/whatis)
- [Manage users and groups in Microsoft Entra ID (Microsoft Learn module)](https://learn.microsoft.com/en-us/training/modules/manage-users-and-groups-in-aad/)
- [Secure your identities by using Microsoft Entra ID (Microsoft Learn module)](https://learn.microsoft.com/en-gb/training/modules/intro-to-azure-ad/)
