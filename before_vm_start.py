#!/usr/bin/python2
from __future__ import unicode_literals

import hooking

def inject_console_xml(domxml, name):
    dev_elem = domxml.getElementsByTagName('devices')[0]
    console_elem = domxml.createElement('console')
    console_elem.setAttribute('type', 'pty')
    source_elem = domxml.createElement('source')
    source_elem.setAttribute('path', '/dev/ovirt-vm/'+name)
    console_elem.appendChild(source_elem)
    target_elem = domxml.createElement('target')
    target_elem.setAttribute('port', '0')
    console_elem.appendChild(target_elem)
    dev_elem.appendChild(console_elem)


try:
    domxml = hooking.read_domxml()
    name = domxml.getElementsByTagName('name')[0].childNodes[0].data
    inject_console_xml(domxml, name)
    hooking.write_domxml(domxml)

except Exception as e:
    sys.error.write("Unexpected error on serial console creation\n")
    sys.exit(2)
