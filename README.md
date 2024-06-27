Semi-manual openssl, create CSR from scratch
=========

Simple PoC script in Python to create certificate signing requests fast in an automated manner where automations like ACME are not present and CSRs have still to be manually reviewed by someone responsible for the CA

How to use?
------------

Set your unit's default metadata in defaults.yaml.
Then set the FQDN (cn) and altnames for your requested certificates in csrs.yaml, take a look at the example.
Make sure modules yaml and os are present in your python env and as well that openssl is installed on your host. Execute the script.
The usual applies: Send the CSR to the PKI folks responsible for your CA, keep the key for yourself and make sure you don't lose it, wait for your certificate to arrive...
