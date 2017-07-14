# How to Configure Settings
`settings.py` contains very little. In fact, it only sets the `DEBUG` flag and
imports settings based on whether or not `DEBUG` is `True` or `False`.

## Relevant settings.py code

```python
DEBUG = True

if DEBUG:
    try:
        from .dev_settings import *
    except ImportError:
        pass
else:
    try:
        from .prod_settings import *
    except ImportError:
        pass
```

## `base_settings.py`

Therefore, settings are set in `base_settings.py`, `dev_settings.py`, and
`prod_settings.py`.  `base_settings.py` contains settings that are used both in
development and also in production that are required for basic operation of the
project.  In general `base_settings.py` should not be changed.  If these
settings do need to be changed, just edit these settings in `dev_settings.py`
or `prod_settings.py`.  Since this is just a python file, a user can just
overwrite any settings and it will be changed.  Furthermore, `dev_settings.py`
and `prod_settings` need to include `base_settings.py` if they do not
themselves define all settings.
