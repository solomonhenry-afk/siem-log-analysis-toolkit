# Sample Splunk Queries

## Detect SSH brute-force
index=auth sourcetype=sshd "Failed password"
| stats count by src_ip, user
| where count > 5

## Detect Kerberos AS-REQ anomalies
index=kerberos "AS-REQ without pre-authentication"
| stats count by src_ip, user
