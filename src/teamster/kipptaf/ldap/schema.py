USER_PERSON_FIELDS = [
    {"name": "adminCount", "type": ["null", "long"], "default": None},
    {"name": "altRecipient", "type": ["null", "string"], "default": None},
    {"name": "altRecipientBL", "type": ["null", "string"], "default": None},
    {"name": "authOrig", "type": ["null", "bytes"], "default": None},
    {"name": "authOrigBL", "type": ["null", "string"], "default": None},
    {"name": "badPwdCount", "type": ["null", "long"], "default": None},
    {"name": "c", "type": ["null", "string"], "default": None},
    {"name": "cn", "type": ["null", "string"], "default": None},
    {"name": "co", "type": ["null", "string"], "default": None},
    {"name": "codePage", "type": ["null", "long"], "default": None},
    {"name": "company", "type": ["null", "string"], "default": None},
    {"name": "countryCode", "type": ["null", "long"], "default": None},
    {"name": "delivContLength", "type": ["null", "long"], "default": None},
    {"name": "deliverAndRedirect", "type": ["null", "boolean"], "default": None},
    {"name": "department", "type": ["null", "string"], "default": None},
    {"name": "description", "type": ["null", "string"], "default": None},
    {"name": "directReports", "type": ["null", "string"], "default": None},
    {"name": "displayName", "type": ["null", "string"], "default": None},
    {"name": "displayNamePrintable", "type": ["null", "string"], "default": None},
    {"name": "distinguishedName", "type": ["null", "string"], "default": None},
    {"name": "division", "type": ["null", "string"], "default": None},
    {"name": "dn", "type": ["null", "string"], "default": None},
    {"name": "employeeID", "type": ["null", "string"], "default": None},
    {"name": "employeeNumber", "type": ["null", "string"], "default": None},
    {"name": "employeeType", "type": ["null", "string"], "default": None},
    {"name": "extensionAttribute13", "type": ["null", "string"], "default": None},
    {"name": "extensionAttribute14", "type": ["null", "string"], "default": None},
    {"name": "extensionAttribute15", "type": ["null", "string"], "default": None},
    {"name": "facsimileTelephoneNumber", "type": ["null", "string"], "default": None},
    {"name": "garbageCollPeriod", "type": ["null", "long"], "default": None},
    {"name": "givenName", "type": ["null", "string"], "default": None},
    {"name": "homeDirectory", "type": ["null", "string"], "default": None},
    {"name": "homeDrive", "type": ["null", "string"], "default": None},
    {"name": "homeMDB", "type": ["null", "string"], "default": None},
    {"name": "homePhone", "type": ["null", "string"], "default": None},
    {"name": "idauto_pwdPrivate", "type": ["null", "bytes"], "default": None},
    {"name": "idautoChallengeSet", "type": ["null", "string"], "default": None},
    {"name": "idautoID", "type": ["null", "string"], "default": None},
    {"name": "idautoPersonAlternateID", "type": ["null", "string"], "default": None},
    {"name": "idautoPersonEmailAddresses", "type": ["null", "string"], "default": None},
    {"name": "idautoPersonFacBirthdate", "type": ["null", "string"], "default": None},
    {"name": "idautoPersonPreferredName", "type": ["null", "string"], "default": None},
    {"name": "idautoPersonRehireDate", "type": ["null", "string"], "default": None},
    {"name": "idautoPersonStatusOverride", "type": ["null", "string"], "default": None},
    {"name": "idautoPersonEnableOverride", "type": ["null", "string"], "default": None},
    {"name": "idautoPersonTermDate", "type": ["null", "string"], "default": None},
    {"name": "idautoStatus", "type": ["null", "string"], "default": None},
    {"name": "info", "type": ["null", "string"], "default": None},
    {"name": "initials", "type": ["null", "string"], "default": None},
    {"name": "instanceType", "type": ["null", "long"], "default": None},
    {"name": "internetEncoding", "type": ["null", "long"], "default": None},
    {"name": "ipPhone", "type": ["null", "string"], "default": None},
    {"name": "isCriticalSystemObject", "type": ["null", "boolean"], "default": None},
    {"name": "l", "type": ["null", "string"], "default": None},
    {"name": "lastKnownParent", "type": ["null", "string"], "default": None},
    {"name": "legacyExchangeDN", "type": ["null", "string"], "default": None},
    {"name": "logonCount", "type": ["null", "long"], "default": None},
    {"name": "logonHours", "type": ["null", "bytes"], "default": None},
    {"name": "mail", "type": ["null", "string"], "default": None},
    {"name": "mailNickname", "type": ["null", "string"], "default": None},
    {"name": "managedObjects", "type": ["null", "string"], "default": None},
    {"name": "manager", "type": ["null", "string"], "default": None},
    {"name": "mDBStorageQuota", "type": ["null", "long"], "default": None},
    {"name": "mDBUseDefaults", "type": ["null", "boolean"], "default": None},
    {"name": "middleName", "type": ["null", "string"], "default": None},
    {"name": "mobile", "type": ["null", "string"], "default": None},
    {"name": "mS_DS_ConsistencyGuid", "type": ["null", "bytes"], "default": None},
    {"name": "msDS_KeyCredentialLink", "type": ["null", "bytes"], "default": None},
    {"name": "msExchArchiveGUID", "type": ["null", "bytes"], "default": None},
    {"name": "msExchArchiveName", "type": ["null", "string"], "default": None},
    {"name": "msExchArchiveStatus", "type": ["null", "long"], "default": None},
    {"name": "msExchBlockedSendersHash", "type": ["null", "bytes"], "default": None},
    {"name": "msExchCoManagedObjectsBL", "type": ["null", "string"], "default": None},
    {"name": "msExchHomeServerName", "type": ["null", "string"], "default": None},
    {"name": "msExchMailboxGuid", "type": ["null", "bytes"], "default": None},
    {"name": "msExchMailboxTemplateLink", "type": ["null", "string"], "default": None},
    {"name": "msExchMasterAccountSid", "type": ["null", "bytes"], "default": None},
    {"name": "msExchMDBRulesQuota", "type": ["null", "long"], "default": None},
    {"name": "msExchMobileMailboxFlags", "type": ["null", "long"], "default": None},
    {"name": "msExchPoliciesExcluded", "type": ["null", "string"], "default": None},
    {"name": "msExchPoliciesIncluded", "type": ["null", "string"], "default": None},
    {"name": "msExchRBACPolicyLink", "type": ["null", "string"], "default": None},
    {"name": "msExchRecipientDisplayType", "type": ["null", "long"], "default": None},
    {"name": "msExchRecipientTypeDetails", "type": ["null", "long"], "default": None},
    {"name": "msExchRemoteRecipientType", "type": ["null", "long"], "default": None},
    {"name": "msExchSafeRecipientsHash", "type": ["null", "bytes"], "default": None},
    {"name": "msExchSafeSendersHash", "type": ["null", "bytes"], "default": None},
    {"name": "msExchUMDtmfMap", "type": ["null", "string"], "default": None},
    {"name": "msExchUserAccountControl", "type": ["null", "long"], "default": None},
    {"name": "msExchUserCulture", "type": ["null", "string"], "default": None},
    {"name": "msExchUserHoldPolicies", "type": ["null", "string"], "default": None},
    {"name": "msExchVersion", "type": ["null", "long"], "default": None},
    {"name": "mSMQDigests", "type": ["null", "bytes"], "default": None},
    {"name": "mSMQSignCertificates", "type": ["null", "bytes"], "default": None},
    {"name": "msNPAllowDialin", "type": ["null", "boolean"], "default": None},
    {"name": "msTSLicenseVersion", "type": ["null", "string"], "default": None},
    {"name": "msTSManagingLS", "type": ["null", "string"], "default": None},
    {"name": "name", "type": ["null", "string"], "default": None},
    {"name": "o", "type": ["null", "string"], "default": None},
    {"name": "objectCategory", "type": ["null", "string"], "default": None},
    {"name": "objectClass", "type": ["null", "string"], "default": None},
    {"name": "objectGUID", "type": ["null", "string"], "default": None},
    {"name": "objectSid", "type": ["null", "string"], "default": None},
    {"name": "operatorCount", "type": ["null", "long"], "default": None},
    {"name": "ownerBL", "type": ["null", "string"], "default": None},
    {"name": "pager", "type": ["null", "string"], "default": None},
    {"name": "physicalDeliveryOfficeName", "type": ["null", "string"], "default": None},
    {"name": "postalCode", "type": ["null", "string"], "default": None},
    {"name": "postOfficeBox", "type": ["null", "string"], "default": None},
    {"name": "primaryGroupID", "type": ["null", "long"], "default": None},
    {"name": "profilePath", "type": ["null", "string"], "default": None},
    {"name": "protocolSettings", "type": ["null", "string"], "default": None},
    {"name": "publicDelegatesBL", "type": ["null", "string"], "default": None},
    {"name": "sAMAccountName", "type": ["null", "string"], "default": None},
    {"name": "sAMAccountType", "type": ["null", "long"], "default": None},
    {"name": "scriptPath", "type": ["null", "string"], "default": None},
    {"name": "showInAddressBook", "type": ["null", "string"], "default": None},
    {"name": "showInAdvancedViewOnly", "type": ["null", "boolean"], "default": None},
    {"name": "sIDHistory", "type": ["null", "bytes"], "default": None},
    {"name": "sn", "type": ["null", "string"], "default": None},
    {"name": "st", "type": ["null", "string"], "default": None},
    {"name": "streetAddress", "type": ["null", "string"], "default": None},
    {"name": "targetAddress", "type": ["null", "string"], "default": None},
    {"name": "telephoneNumber", "type": ["null", "string"], "default": None},
    {"name": "textEncodedORAddress", "type": ["null", "string"], "default": None},
    {"name": "title", "type": ["null", "string"], "default": None},
    {"name": "unicodePwd", "type": ["null", "string"], "default": None},
    {"name": "url", "type": ["null", "string"], "default": None},
    {"name": "userAccountControl", "type": ["null", "long"], "default": None},
    {"name": "userCertificate", "type": ["null", "bytes"], "default": None},
    {"name": "userParameters", "type": ["null", "string"], "default": None},
    {"name": "userPrincipalName", "type": ["null", "string"], "default": None},
    {"name": "uSNChanged", "type": ["null", "long"], "default": None},
    {"name": "uSNCreated", "type": ["null", "long"], "default": None},
    {"name": "wWWHomePage", "type": ["null", "string"], "default": None},
    {
        "name": "idautoPersonPreferredLastName",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "msExchHideFromAddressLists",
        "type": ["null", "boolean"],
        "default": None,
    },
    {
        "name": "msDS_ExternalDirectoryObjectId",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "msDS_SupportedEncryptionTypes",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "msExchMailboxSecurityDescriptor",
        "type": ["null", "bytes"],
        "default": None,
    },
    {
        "name": "msExchOmaAdminWirelessEnable",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "msExchRecipientSoftDeletedStatus",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "msExchMobileMailboxPolicyLink",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "memberOf",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "otherHomePhone",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "otherIpPhone",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "otherPager",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "otherTelephoneNumber",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "proxyAddresses",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "publicDelegates",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "servicePrincipalName",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "userWorkstations",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "otherFacsimileTelephoneNumber",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "accountExpires",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "badPasswordTime",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "dSCorePropagationData",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "idautoChallengeSetTimestamp",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "idautoPersonEndDate",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "lastLogoff",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "lastLogon",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "lastLogonTimestamp",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "lockoutTime",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "msExchWhenMailboxCreated",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "msTSExpireDate",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "pwdLastSet",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "whenChanged",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "whenCreated",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
]

GROUP_FIELDS = [
    {"name": "adminCount", "type": ["null", "long"], "default": None},
    {"name": "altRecipientBL", "type": ["null", "string"], "default": None},
    {"name": "authOrig", "type": ["null", "bytes"], "default": None},
    {"name": "cn", "type": ["null", "string"], "default": None},
    {"name": "description", "type": ["null", "string"], "default": None},
    {"name": "displayName", "type": ["null", "string"], "default": None},
    {"name": "displayNamePrintable", "type": ["null", "string"], "default": None},
    {"name": "distinguishedName", "type": ["null", "string"], "default": None},
    {"name": "dLMemSubmitPerms", "type": ["null", "bytes"], "default": None},
    {"name": "dLMemSubmitPermsBL", "type": ["null", "string"], "default": None},
    {"name": "dn", "type": ["null", "string"], "default": None},
    {"name": "extensionAttribute11", "type": ["null", "string"], "default": None},
    {"name": "extensionAttribute12", "type": ["null", "string"], "default": None},
    {"name": "extensionAttribute13", "type": ["null", "string"], "default": None},
    {"name": "extensionAttribute14", "type": ["null", "string"], "default": None},
    {"name": "extensionAttribute15", "type": ["null", "string"], "default": None},
    {"name": "groupType", "type": ["null", "long"], "default": None},
    {"name": "idautoGroupExcludeBaseDN", "type": ["null", "string"], "default": None},
    {"name": "idautoGroupExcludeFilter", "type": ["null", "string"], "default": None},
    {"name": "idautoGroupIncludeBaseDN", "type": ["null", "string"], "default": None},
    {"name": "idautoGroupIncludeFilter", "type": ["null", "string"], "default": None},
    {"name": "idautoGroupOwners", "type": ["null", "string"], "default": None},
    {"name": "idautoGroupSyncInterval", "type": ["null", "long"], "default": None},
    {"name": "idautoID", "type": ["null", "string"], "default": None},
    {"name": "info", "type": ["null", "string"], "default": None},
    {"name": "instanceType", "type": ["null", "long"], "default": None},
    {"name": "internetEncoding", "type": ["null", "long"], "default": None},
    {"name": "isCriticalSystemObject", "type": ["null", "boolean"], "default": None},
    {"name": "legacyExchangeDN", "type": ["null", "string"], "default": None},
    {"name": "mail", "type": ["null", "string"], "default": None},
    {"name": "mailNickname", "type": ["null", "string"], "default": None},
    {"name": "managedBy", "type": ["null", "string"], "default": None},
    {"name": "managedObjects", "type": ["null", "string"], "default": None},
    {"name": "msExchAddressBookFlags", "type": ["null", "long"], "default": None},
    {"name": "msExchArbitrationMailbox", "type": ["null", "string"], "default": None},
    {"name": "msExchCoManagedByLink", "type": ["null", "string"], "default": None},
    {"name": "msExchCoManagedObjectsBL", "type": ["null", "string"], "default": None},
    {"name": "msExchGroupMemberCount", "type": ["null", "long"], "default": None},
    {"name": "msExchPoliciesExcluded", "type": ["null", "string"], "default": None},
    {"name": "msExchPoliciesIncluded", "type": ["null", "string"], "default": None},
    {"name": "msExchRequireAuthToSendTo", "type": ["null", "boolean"], "default": None},
    {"name": "msExchUMDtmfMap", "type": ["null", "string"], "default": None},
    {"name": "msExchVersion", "type": ["null", "long"], "default": None},
    {"name": "name", "type": ["null", "string"], "default": None},
    {"name": "objectCategory", "type": ["null", "string"], "default": None},
    {"name": "objectClass", "type": ["null", "string"], "default": None},
    {"name": "objectGUID", "type": ["null", "string"], "default": None},
    {"name": "objectSid", "type": ["null", "string"], "default": None},
    {"name": "owner", "type": ["null", "string"], "default": None},
    {"name": "ownerBL", "type": ["null", "string"], "default": None},
    {"name": "reportToOriginator", "type": ["null", "boolean"], "default": None},
    {"name": "sAMAccountName", "type": ["null", "string"], "default": None},
    {"name": "sAMAccountType", "type": ["null", "long"], "default": None},
    {"name": "showInAddressBook", "type": ["null", "string"], "default": None},
    {"name": "sIDHistory", "type": ["null", "bytes"], "default": None},
    {"name": "systemFlags", "type": ["null", "long"], "default": None},
    {"name": "uSNChanged", "type": ["null", "long"], "default": None},
    {"name": "uSNCreated", "type": ["null", "long"], "default": None},
    {
        "name": "idautoGroupCoOwnerEditable",
        "type": ["null", "boolean"],
        "default": None,
    },
    {
        "name": "idautoGroupStaticExcludes",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "idautoGroupStaticIncludes",
        "type": ["null", "string"],
        "default": None,
    },
    {
        "name": "msExchHideFromAddressLists",
        "type": ["null", "boolean"],
        "default": None,
    },
    {
        "name": "msExchGroupDepartRestriction",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "msExchGroupExternalMemberCount",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "msExchGroupJoinRestriction",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "msExchRecipientDisplayType",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "msExchRecipientTypeDetails",
        "type": ["null", "long"],
        "default": None,
    },
    {
        "name": "member",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "memberOf",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "proxyAddresses",
        "type": ["null", {"type": "array", "items": "string"}],
        "default": None,
    },
    {
        "name": "dSCorePropagationData",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "idautoGroupLastSynced",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "whenChanged",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
    {
        "name": "whenCreated",
        "type": ["null", "double"],
        "logicalType": "timestamp-micros",
        "default": None,
    },
]

ASSET_FIELDS = {
    "user_person": USER_PERSON_FIELDS,
    "group": GROUP_FIELDS,
}
