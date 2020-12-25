# Client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dn** | **str** |  | [optional] 
**inum** | **str** | XRI i-number. Client Identifier to uniquely identify the client. | [optional] 
**client_secret** | **str** | The client secret.  The client MAY omit the parameter if the client secret is an empty string. | [optional] 
**front_channel_logout_uri** | **str** |  | [optional] 
**front_channel_logout_session_required** | **bool** |  | [optional] 
**registration_access_token** | **str** |  | [optional] 
**client_id_issued_at** | **date** |  | [optional] 
**client_secret_expires_at** | **date** |  | [optional] 
**redirect_uris** | **list[str]** | Redirection URI values used by the Client. One of these registered Redirection URI values must exactly match the redirect_uri parameter value used in each Authorization Request | [optional] 
**claim_redirect_uris** | **list[str]** | Array of The Claims Redirect URIs to which the client wishes the authorization server to direct the requesting party&#x27;s user agent after completing its interaction. | [optional] 
**response_types** | **list[str]** | A list of the OAuth 2.0 response_type values that the Client is declaring that it will restrict itself to using. If omitted, the default is that the Client will use only the code Response Type. Allowed values are code, token, id_token. | 
**grant_types** | **list[str]** | A list of the OAuth 2.0 Grant Types that the Client is declaring that it will restrict itself to using. | 
**application_type** | **str** | Kind of the application. The default, if omitted, is web. The defined values are native or web. Web Clients using the OAuth Implicit Grant Type must only register URLs using the HTTPS scheme as redirect_uris, they must not use localhost as the hostname. Native Clients must only register redirect_uris using custom URI schemes or URLs using the http scheme with localhost as the hostname. | 
**contacts** | **list[str]** | e-mail addresses of people responsible for this Client. | [optional] 
**client_name** | **str** | A human-readable name of the client. | 
**id_token_token_binding_cnf** | **str** | Specifies the JWT Confirmation Method member name (e.g. tbh) that the Relying Party expects when receiving Token Bound ID Tokens. The presence of this parameter indicates that the Relying Party supports Token Binding of ID Tokens. If omitted, the default is that the Relying Party does not support Token Binding of ID Tokens. | [optional] 
**logo_uri** | **str** | URL that references a logo for the Client application. | [optional] 
**client_uri** | **str** | URL of the home page of the Client. The value of this field must point to a valid Web page. | [optional] 
**policy_uri** | **str** | URL that the Relying Party Client provides to the End-User to read about the how the profile data will be used. | [optional] 
**tos_uri** | **str** | URL that the Relying Party Client provides to the End-User to read about the Relying Party&#x27;s terms of service. | [optional] 
**jwks_uri** | **str** | URL for the Client&#x27;s JSON Web Key Set (JWK) document containing key(s) that are used for signing requests to the OP. The JWK Set may also contain the Client&#x27;s encryption keys(s) that are used by the OP to encrypt the responses to the Client. When both signing and encryption keys are made available, a use (Key Use) parameter value is required for all keys in the document to indicate each key&#x27;s intended usage. | [optional] 
**jwks** | **str** | List of JSON Web Key (JWK) - A JSON object that represents a cryptographic key. The members of the object represent properties of the key, including its value. | [optional] 
**sector_identifier_uri** | **str** | URL using the https scheme to be used in calculating Pseudonymous Identifiers by the OP. | [optional] 
**subject_type** | **str** | Subject type requested for the Client ID. Valid types include pairwise and public. | 
**id_token_signed_response_alg** | **str** | JWS alg algorithm (JWA) required for signing the ID Token issued to this Client. | 
**id_token_encrypted_response_alg** | **str** | JWE alg algorithm (JWA) required for encrypting the ID Token issued to this Client. | [optional] 
**id_token_encrypted_response_enc** | **str** | JWE enc algorithm (JWA) required for encrypting the ID Token issued to this Client. | [optional] 
**user_info_signed_response_alg** | **str** | JWS alg algorithm (JWA) required for signing UserInfo Responses. | [optional] 
**user_info_encrypted_response_alg** | **str** | JWE alg algorithm (JWA) required for encrypting UserInfo Responses. | [optional] 
**user_info_encrypted_response_enc** | **str** | JWE enc algorithm (JWA) required for encrypting UserInfo Responses. | [optional] 
**request_object_signing_alg** | **str** | JWS alg algorithm (JWA) that must be used for signing Request Objects sent to the OP. | [optional] 
**request_object_encryption_alg** | **str** | JWE alg algorithm (JWA) the RP is declaring that it may use for encrypting Request Objects sent to the OP. | [optional] 
**request_object_encryption_enc** | **str** | JWE enc algorithm (JWA) the RP is declaring that it may use for encrypting Request Objects sent to the OP. | [optional] 
**token_endpoint_auth_method** | **str** | Requested Client Authentication method for the Token Endpoint. | 
**token_endpoint_auth_signing_alg** | **str** | JWS alg algorithm (JWA) that must be used for signing the JWT used to authenticate the Client at the Token Endpoint for the private_key_jwt and client_secret_jwt authentication methods. | [optional] 
**default_max_age** | **int** | Specifies the Default Maximum Authentication Age. | [optional] 
**require_auth_time** | **bool** | Boolean value specifying whether the auth_time Claim in the ID Token is required. It is required when the value is true. | [optional] 
**default_acr_values** | **list[str]** | Array of default requested Authentication Context Class Reference values that the Authorization Server must use for processing requests from the Client. | [optional] 
**initiate_login_uri** | **str** | Specifies the URI using the https scheme that the authorization server can call to initiate a login at the client. | [optional] 
**post_logout_redirect_uris** | **list[str]** | Provide the URLs supplied by the RP to request that the user be redirected to this location after a logout has been performed. | [optional] 
**request_uris** | **list[str]** | Provide a list of requests_uri values that are pre-registered by the Client for use at the Authorization Server. | [optional] 
**scopes** | **list[str]** | Provide list of scopes granted to the client. | 
**claims** | **list[str]** | Provide list of claims granted to the client. | [optional] 
**trusted_client** | **bool** | Attribute which corresponds to the \&quot;Pre-Authorization\&quot; property. Default value is false. | [optional] 
**last_access_time** | **date** | Integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating last access time. | [optional] 
**last_logon_time** | **date** | Integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating last login time. | [optional] 
**persist_client_authorizations** | **bool** | Specifies if the client authorization details are to be persisted. Default value is true. | [optional] 
**include_claims_in_id_token** | **bool** | If true then claims are included in token id, default value is false. | [optional] 
**refresh_token_lifetime** | **int** | Specifies the Client-specific refresh token expiration. | [optional] 
**access_token_lifetime** | **int** | Specifies the Client-specific access token expiration. | [optional] 
**custom_attributes** | [**list[CustomAttribute]**](CustomAttribute.md) |  | [optional] 
**custom_object_classes** | **list[str]** |  | [optional] 
**rpt_as_jwt** | **bool** | Specifies whether RPT should be return as signed JWT. | [optional] 
**access_token_as_jwt** | **bool** | Specifies whether access token as signed JWT. | [optional] 
**access_token_signing_alg** | **str** | Specifies signing algorithm that has to be used during JWT signing. If it&#x27;s not specified, then the default OP signing algorithm will be used. | 
**disabled** | **bool** | Specifies whether client is disabled. | [optional] 
**authorized_origins** | **list[str]** | Specifies authorized JavaScript origins. | [optional] 
**software_id** | **str** | Specifies a unique identifier string (UUID) assigned by the client developer or software publisher used by registration endpoints to identify the client software to be dynamically registered. | [optional] 
**software_version** | **str** | Specifies a version identifier string for the client software identified by &#x27;software_id&#x27;. The value of the &#x27;software_version&#x27; should change on any update to the client software identified by the same &#x27;software_id&#x27;. | [optional] 
**software_statement** | **str** | Specifies a software statement containing client metadata values about the client software as claims. This is a string value containing the entire signed JWT. | [optional] 
**attributes** | [**ClientAttributes**](ClientAttributes.md) |  | [optional] 
**backchannel_token_delivery_mode** | **str** | specifies how backchannel token will be delivered. | [optional] 
**backchannel_client_notification_endpoint** | **str** | Client Initiated Backchannel Authentication (CIBA) enables a Client to initiate the authentication of an end-user by means of out-of-band mechanisms. Upon receipt of the notification, the Client makes a request to the token endpoint to obtain the tokens. | [optional] 
**backchannel_authentication_request_signing_alg** | **str** | The JWS algorithm alg value that the Client will use for signing authentication request, as described in Section 7.1.1. of OAuth 2.0 [RFC6749]. When omitted, the Client will not send signed authentication requests. | [optional] 
**backchannel_user_code_parameter** | **bool** | Boolean value specifying whether the Client supports the user_code parameter. If omitted, the default value is false. | [optional] 
**exp** | **date** | Integer timestamp, measured in the number of seconds since January 1 1970 UTC, indicating when this permission will expire. | [optional] 
**deletable** | **bool** | Specifies whether client is deletable. | [optional] 
**jans_id** | **str** | Attribute Scope Id. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

