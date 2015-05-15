#!/usr/bin/python2
from __future__ import unicode_literals, print_function

try:
    import hooking
except ImportError:
    from xml.dom.minidom import parseString
    from unittest.mock import Mock
    hooking = Mock()
    hooking.read_domxml.return_value = parseString('''
<domain type='kvm' id='38'>
  <name>testvm</name>
  <uuid>74c072b6-ad66-4643-9211-da80a2a9b996</uuid>
  <memory unit='KiB'>1048576</memory>
  <currentMemory unit='KiB'>1048576</currentMemory>
  <vcpu placement='static' current='2'>16</vcpu>
  <cputune>
    <shares>1020</shares>
    <period>3125</period>
    <quota>50000</quota>
  </cputune>
  <resource>
    <partition>/machine</partition>
  </resource>
    <sysinfo type='smbios'>
      <system>
        <entry name='manufacturer'>oVirt</entry>
        <entry name='product'>Ovirt Managed Engine</entry>
        <entry name='version'>7-1.1503.el7.centos.2.8</entry>
        <entry name='serial'>4C4C4544-0037-5210-8037-B2C04F483332</entry>
        <entry name='uuid'>74c072b6-ad66-4643-9211-da80a2a9b996</entry>
      </system>
    </sysinfo>
  <os>
    <type arch='x86_64' machine='rhel6.5.0'>hvm</type>
    <smbios mode='sysinfo'/>
  </os>
  <features>
    <acpi/>
  </features>
  <cpu mode='custom' match='exact'>
    <model fallback='allow'>SandyBridge</model>
    <topology sockets='16' cores='1' threads='1'/>
  </cpu>
  <clock offset='variable' adjustment='0' basis='utc'>
    <timer name='rtc' tickpolicy='catchup'/>
    <timer name='pit' tickpolicy='delay'/>
    <timer name='hpet' present='no'/>
  </clock>
  <on_poweroff>destroy</on_poweroff>
  <on_reboot>restart</on_reboot>
  <on_crash>destroy</on_crash>
  <devices>
    <emulator>/usr/libexec/qemu-kvm</emulator>
    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <source startupPolicy='optional'/>
      <backingStore/>
      <target dev='hdc' bus='ide'/>
      <readonly/>
      <serial></serial>
      <alias name='ide0-1-0'/>
      <address type='drive' controller='0' bus='1' target='0' unit='0'/>
    </disk>
    <disk type='file' device='disk' snapshot='no'>
      <driver name='qemu' type='raw' cache='none' error_policy='stop' io='threads'/>
      <source file='/rhev/data-center/00000002-0002-0002-0002-000000000064/048bfe72-a2e8-42cc-b1d2-3d46fb631b27/images/bdebb9d1-2bdd-4bb0-9857-32952c7a283d/8038986e-d3ec-4829-9288-8726cf7d7ad1'/>
      <backingStore/>
      <target dev='vda' bus='virtio'/>
      <serial>bdebb9d1-2bdd-4bb0-9857-32952c7a283d</serial>
      <boot order='1'/>
      <alias name='virtio-disk0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x0'/>
    </disk>
    <controller type='scsi' index='0' model='virtio-scsi'>
      <alias name='scsi0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x03' function='0x0'/>
    </controller>
    <controller type='virtio-serial' index='0' ports='16'>
      <alias name='virtio-serial0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x04' function='0x0'/>
    </controller>
    <controller type='usb' index='0'>
      <alias name='usb0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x2'/>
    </controller>
    <controller type='pci' index='0' model='pci-root'>
      <alias name='pci.0'/>
    </controller>
    <controller type='ide' index='0'>
      <alias name='ide0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x01' function='0x1'/>
    </controller>
    <interface type='bridge'>
      <mac address='00:1a:4a:97:cd:0b'/>
      <source bridge='Net_902'/>
      <bandwidth>
      </bandwidth>
      <target dev='vnet14'/>
      <model type='virtio'/>
      <filterref filter='vdsm-no-mac-spoofing'/>
      <link state='up'/>
      <alias name='net0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x07' function='0x0'/>
    </interface>
    <interface type='bridge'>
      <mac address='00:1a:4a:97:cd:0e'/>
      <source bridge='Secure'/>
      <bandwidth>
      </bandwidth>
      <target dev='vnet15'/>
      <model type='virtio'/>
      <filterref filter='vdsm-no-mac-spoofing'/>
      <link state='up'/>
      <alias name='net1'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x08' function='0x0'/>
    </interface>
    <channel type='unix'>
      <source mode='bind' path='/var/lib/libvirt/qemu/channels/74c072b6-ad66-4643-9211-da80a2a9b996.com.redhat.rhevm.vdsm'/>
      <target type='virtio' name='com.redhat.rhevm.vdsm' state='disconnected'/>
      <alias name='channel0'/>
      <address type='virtio-serial' controller='0' bus='0' port='1'/>
    </channel>
    <channel type='unix'>
      <source mode='bind' path='/var/lib/libvirt/qemu/channels/74c072b6-ad66-4643-9211-da80a2a9b996.org.qemu.guest_agent.0'/>
      <target type='virtio' name='org.qemu.guest_agent.0' state='disconnected'/>
      <alias name='channel1'/>
      <address type='virtio-serial' controller='0' bus='0' port='2'/>
    </channel>
    <channel type='spicevmc'>
      <target type='virtio' name='com.redhat.spice.0' state='disconnected'/>
      <alias name='channel2'/>
      <address type='virtio-serial' controller='0' bus='0' port='3'/>
    </channel>
    <input type='mouse' bus='ps2'/>
    <input type='keyboard' bus='ps2'/>
    <graphics type='spice' tlsPort='5907' autoport='yes' keymap='en-us' passwdValidTo='2015-05-14T09:06:46' connected='disconnect'>
      <listen type='network' address='10.100.0.12' network='vdsm-ovirtmgmt'/>
      <channel name='main' mode='secure'/>
      <channel name='display' mode='secure'/>
      <channel name='inputs' mode='secure'/>
      <channel name='cursor' mode='secure'/>
      <channel name='playback' mode='secure'/>
      <channel name='record' mode='secure'/>
      <channel name='smartcard' mode='secure'/>
      <channel name='usbredir' mode='secure'/>
    </graphics>
    <video>
      <model type='qxl' ram='65536' vram='32768' vgamem='16384' heads='1'/>
      <alias name='video0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
    </video>
    <memballoon model='virtio'>
      <alias name='balloon0'/>
      <address type='pci' domain='0x0000' bus='0x00' slot='0x06' function='0x0'/>
    </memballoon>
  </devices>
</domain>''')

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
