# PDisk
Console application in Python for disk management using WMI

=== INTRODUCTION ===

What is PDisk?

It is a console application written in Python, based on disk management. Its different applications are displayed in an options menu, which has the following features:

(1) In the information section, it is capable of:
a. Listing information about Physical Disks.  
b. Listing information about Partitions.  
c. Listing information about Volumes.  
d. Listing information about Logical Drives.  


=== CONCEPTUAL EXAMPLES ===

(1#) INFORMATION QUERIES TO WMI:

Queries and WMI implementation in Python  
Conceptual Example:  
a. import wmi: Python library that acts as a translator to WMI.  
b. c = wmi.WMI(n"root\\cimv2"): Proxy connector that opens a session with the NAMESPACE ("root\cimv2") where the classes we want to query and their respective properties are stored.  
c. Win32_DiskDrive: WMI class that represents physical disks. Some of its properties are:  
Availability, Name, Status, etc.  


=== REFERENCES ===

(A). WMI INFORMATION  
1. WMI for Python: https://pypi.org/project/WMI/  
2. WMI: https://learn.microsoft.com/en-us/windows/win32/wmisdk/wmi-start-page#:~:text=Windows%20Management%20Instrumentation%20(WMI)  
3. WMI CLASS: https://learn.microsoft.com/en-us/windows/win32/wmisdk/retrieving-a-class  
4. WIN32PROCESS Class: https://learn.microsoft.com/en-us/windows/desktop/CIMWin32Prov/win32-process  
5. COM: https://learn.microsoft.com/es-es/windows/win32/wmisdk/creating-wmi-clients  
   (Information about COM clients, Python is not natively supported).  
6. SPECIFIC CLASS DOCUMENTATION:  
a. Win32_DiskDrive class: https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-diskdrive  
b. Win32_DiskPartition class: https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-diskpartition  
c. Win32_Volume class: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/legacy/aa394515(v=vs.85)  
d. Win32_LogicalDisk class: https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-logicaldisk  


=== LICENSING ===

a. GPLv3: Public use and modification without restrictions:
https://mit-license.org/

=== DISCLAIMER ===

This application is provided "as is," without express or implied warranties.  
The author is not responsible for damages, data loss, or misuse of the software.  
Use of the application is at your own risk and responsibility.
