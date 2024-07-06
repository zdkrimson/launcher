import wmi

c = wmi.WMI()
system = c.Win32_ComputerSystem()[0]
print(system.Model)
hostinfo = system.Model