# Workflowy Automation

Python scripts to automate tasks in Workflowy

## flag_due_workflowy_items.py

Script that finds all Workflowy items tagged with today's date and gives then the tag `#Focus`

Allows for scheduling of items in Workflowy without fear of losing them

To schedule items you need to give them a tag in the format `#yyy-MM-dd`, for example `#2016-02-18`

**Pre-requisites**

* Firefox Web Browser
* Selenium package (`pip install -U selenium` or run `py .\setup.py install`)
* A Workflowy account

**Setup**

Create a file in the root directory called `local_settings.py`

Then paste this into the fill with your Workflowy credentials:

```
workflowy_username = "your username"
workflowy_password = "your password"
```

**Running**

Run `py .\flag_due_workflowy_items.py` to launch the script.

**Troubleshooting**

> Firefox opens but doesn't navigate to any page

Usually means the Selenium version is out of date, run `pip install -U selenium` to ensure you have the latest version installed.
