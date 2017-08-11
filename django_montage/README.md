# How to Configure Settings
`settings.py` contains defaults to many settings.  To use the defaults, there
is no configuration needed.  Add any changes to settings to a file called
`local_settings.py` and place it along side `settings.py`.  Included is a
`local_settings.py.example`.

Currently, production database information as well as an example for loading an
RSA key pair used for the JWT implementation are placed in the `.example` file. 
Anything that would be a vital or strongly suggested in production, but not in
development should be placed in this file.  For example, the JWT key pair does
not need to be loaded in the way exemplified in this file, but it does need to
be loaded in production, as it is a security risk to use the pair included in
`local_settings.py`.
