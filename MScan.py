#-*- MouseXsec -Sam -*-
import requests

logo = """
    Tools Scan shell and uploader - MouseXsec

status [200] = Found
status [404] = Not found
status [403] = Forbiden
status [500] = Error
"""
print logo
target = raw_input("list: ")
target = open(target,"r")

for a in target.readlines():
    pw = a.strip()
    c = requests.get(pw+"/admin/modules/bibliography/pop_attach.php")
    print "url: ",c.url,"status",c.status_code
