'///////////////////////////////////////////////////////////////////////////////////////////////////////////////'
'*************************************        Q U E R Y  M O D U L E S         *********************************'
'///////////////////////////////////////////////////////////////////////////////////////////////////////////////'





'WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMI WMIW MI WMI WMI'
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////'
#***************************************     QUERY  MODULE  TO  WMI      ***************************************'
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////'

'| 1 # |  D I S K S ********** Physical Disks Win32_DiskDrive**********' 
# import the WMI library
import wmi 
# Connect to WMI service in the namespace "root\cimv2"
c = wmi.WMI(namespace="root\\cimv2") 
# Loop through each physical disk returned by the WMI query
def list_disk():
    for disk in c.Win32_DiskDrive():
        print("-" * 40)
        print("")
        print("=== DETECTED LISTED DISK DRIVES ===")

        
        print("")
        print("***IMPORTANT INFORMATION***\n")
        print("1.Availability:", disk.Availability)
        print("2.Description:", disk.Description)
        print("3.DeviceID:", disk.DeviceID)
        print("4.FirmwareRevision:", disk.FirmwareRevision)
        print("5.Index:", disk.Index)
        print("6.InterfaceType:", disk.InterfaceType)
        print("7.Manufacturer:", disk.Manufacturer)
        print("8.Model:", disk.Model)
        print("9.Name:", disk.Name)
        print("10.Partitions:", disk.Partitions)
        print("11.PNPDeviceID:", disk.PNPDeviceID)
        print("12.SerialNumber:", disk.SerialNumber)
        print("13.Size:", disk.Size)
        print("14.Status:", disk.Status)
        print("15.StatusInfo:", disk.StatusInfo)
        print("16.SystemName:", disk.SystemName)
        print("")

        
        print("***ADDITIONAL INFORMATION***\n")
        print("17.BytesPerSector:", disk.BytesPerSector)
        print("18.Capabilities:", disk.Capabilities)
        print("19.CapabilityDescriptions:", disk.CapabilityDescriptions)
        print("20.ConfigManagerUserConfig:", disk.ConfigManagerUserConfig)
        print("21.DefaultBlockSize:", disk.DefaultBlockSize)
        print("22.MaxBlockSize:", disk.MaxBlockSize)
        print("23.MaxMediaSize:", disk.MaxMediaSize)
        print("24.MediaLoaded:", disk.MediaLoaded)
        print("25.MediaType:", disk.MediaType)
        print("26.MinBlockSize:", disk.MinBlockSize)
        print("27.PowerManagementCapabilities:", getattr(disk, "PowerManagementCapabilities", []))
        print("28.PowerManagementSupported:", disk.PowerManagementSupported)
        print("29.SCSIBus:", disk.SCSIBus)
        print("30.SCSILogicalUnit:", disk.SCSILogicalUnit)
        print("31.SCSIPort:", disk.SCSIPort)
        print("32.SCSITargetId:", disk.SCSITargetId)
        print("33.Signature:", disk.Signature)
        print("34.TotalCylinders:", disk.TotalCylinders)
        print("35.TotalHeads:", disk.TotalHeads)
        print("36.TotalSectors:", disk.TotalSectors)
        print("37.TotalTracks:", disk.TotalTracks)
        print("38.TracksPerCylinder:", disk.TracksPerCylinder)
        print("")

        print("-" * 40)


'| 2 # |  P A R T I T I O N S **********Disk Partitions Win32_DiskPartition**********'

import wmi 

c = wmi.WMI(namespace="root\\cimv2")

def list_partition():
    for partition in c.Win32_DiskPartition():
        print("-" * 40)
        print("")
        print("=== DETECTED LISTED PARTITIONS ===")

       
        print("")
        print("***IMPORTANT INFORMATION***\n")
        print("1.Access:", partition.Access)
        print("2.Availability:", partition.Availability)
        print("3.BlockSize:", partition.BlockSize)
        print("4.Bootable:", partition.Bootable)
        print("5.BootPartition:", partition.BootPartition)
        print("6.Description:", partition.Description)
        print("7.DeviceID:", partition.DeviceID)
        print("8.Name:", partition.Name)
        print("9.NumberOfBlocks:", partition.NumberOfBlocks)
        print("10.Size:", partition.Size)
        print("11.Status:", partition.Status)
        print("12.Type:", partition.Type)
        print("")

       
        print("***ADDITIONAL INFORMATION***\n")
        print("13.AdditionalAvailability:", getattr(partition, "AdditionalAvailability",[]))
        print("14.IdentifyingDescriptions:", getattr(partition, "IdentifyingDescription",[]))
        print("15.OtherIdentifyingInfo:", getattr(partition,"OtherIdentifyingInfo",[]))
        print("16.PNPDeviceID:", partition.PNPDeviceID)
        print("17.PowerManagementCapabilities:", getattr(partition, "PowerManagementCapabilities",[]))
        print("18.PrimaryPartition:", partition.PrimaryPartition)
        print("19.Purpose:", partition.Purpose)
        print("20.StatusInfo:", partition.StatusInfo)
        print("21.SystemName:", partition.SystemName)
        print("")

        print("-" * 40)


'| 3 # |  V O L U M E S **********Disk Volumes Win32_DiskVolume**********'

import wmi 

c = wmi.WMI(namespace="root\\cimv2")

def list_volume():
    for volume in c.Win32_Volume():
        print("-" * 40)
        print("")
        print("=== DETECTED LISTED VOLUMES ===")
        print("")
        print("***IMPORTANT INFORMATION***\n")
        print("1. Availability:", volume.Availability)
        print("2. BlockSize:", volume.BlockSize)
        print("3. Capacity:", volume.Capacity)
        print("4. ConfigManagerUserConfig:", volume.ConfigManagerUserConfig)
        print("5. Description:", volume.Description)
        print("6. DeviceID:", volume.DeviceID)
        print("7. DriveLetter:", volume.DriveLetter)
        print("8. DriveType:", volume.DriveType)
        print("9. FileSystem:", volume.FileSystem)
        print("10. FreeSpace:", volume.FreeSpace)
        print("11. Label:", volume.Label)
        print("12. Name:", volume.Name)
        print("13. SerialNumber:", volume.SerialNumber)
        print("14. Status:", volume.Status)
        print("15. StatusInfo:", volume.StatusInfo)
        print("16. SystemName:", volume.SystemName)

        
        print("\n***ADDITIONAL INFORMATION***\n")
        print("17. Access:", volume.Access)
        print("18. Automount:", volume.Automount)
        print("19. Compressed:", volume.Compressed)
        print("20. DirtyBitSet:", volume.DirtyBitSet)
        print("21. IndexingEnabled:", volume.IndexingEnabled)
        print("22. MaximumFileNameLength:", volume.MaximumFileNameLength)
        print("23. NumberOfBlocks:", volume.NumberOfBlocks)
        print("24. PNPDeviceID:", volume.PNPDeviceID)
        print("25. PowerManagementCapabilities:", getattr(volume, "PowerManagementCapabilities", []))
        print("26. PowerManagementSupported:", volume.PowerManagementSupported)
        print("27. Purpose:", volume.Purpose)
        print("28. QuotasEnabled:", volume.QuotasEnabled)
        print("29. QuotasIncomplete:", volume.QuotasIncomplete)
        print("30. QuotasRebuilding:", volume.QuotasRebuilding)
        print("31. SupportsDiskQuotas:", volume.SupportsDiskQuotas)
        print("32. SupportsFileBasedCompression:", volume.SupportsFileBasedCompression)

        print("-" * 40)


'| 4 # |  L O G I C   UNIT   C: ********** LOGICAL UNIT Win32_LogicalDisk**********'

import wmi 

c = wmi.WMI(namespace="root\\cimv2")

def list_logicaldisk():
    for logical_unit in c.Win32_LogicalDisk():
        print("-" * 40)
        print("")
        print("=== LOGICAL DISK DETECTED ===")
        print("")
        print("***IMPORTANT INFORMATION***\n")
        print("1. DeviceID:", logical_unit.DeviceID)
        print("2. Name:", logical_unit.Name)
        print("3. DriveType:", logical_unit.DriveType)
        print("4. FileSystem:", logical_unit.FileSystem)
        print("5. Size:", logical_unit.Size)
        print("6. FreeSpace:", logical_unit.FreeSpace)
        print("7. VolumeName:", logical_unit.VolumeName)
        print("8. VolumeSerialNumber:", logical_unit.VolumeSerialNumber)
        print("9. Status:", logical_unit.Status)
        print("10. StatusInfo:", logical_unit.StatusInfo)
        print("11. Availability:", logical_unit.Availability)
        print("12. SystemName:", logical_unit.SystemName)
        print("")
        print("\n***ADDITIONAL INFORMATION***\n")
        print("13. ProviderName:", logical_unit.ProviderName)
        print("14. MediaType:", logical_unit.MediaType)
        print("15. Description:", logical_unit.Description)
        print("16. Compressed:", logical_unit.Compressed)
        print("17. BlockSize:", logical_unit.BlockSize)
        print("18. Access:", logical_unit.Access)
        print("19. ConfigManagerUserConfig:", logical_unit.ConfigManagerUserConfig)
        print("20. ConfigManagerErrorCode:", logical_unit.ConfigManagerErrorCode)
        print("21. ErrorCleared:", logical_unit.ErrorCleared)
        print("22. ErrorDescription:", logical_unit.ErrorDescription)
        print("23. ErrorMethodology:", logical_unit.ErrorMethodology)
        print("24. LastErrorCode:", logical_unit.LastErrorCode)
        print("25. InstallDate:", logical_unit.InstallDate)
        print("26. MaximumComponentLength:", logical_unit.MaximumComponentLength)
        print("27. NumberOfBlocks:", logical_unit.NumberOfBlocks)
        print("28. PNPDeviceID:", logical_unit.PNPDeviceID)
        print("29. PowerManagementCapabilities:", getattr(logical_unit, "PowerManagementCapabilities", []))
        print("30. PowerManagementSupported:", logical_unit.PowerManagementSupported)
        print("31. QuotasDisabled:", logical_unit.QuotasDisabled)
        print("32. QuotasIncomplete:", logical_unit.QuotasIncomplete)
        print("33. QuotasRebuilding:", logical_unit.QuotasRebuilding)
        print("34. SupportsDiskQuotas:", logical_unit.SupportsDiskQuotas)
        print("35. SupportsFileBasedCompression:", logical_unit.SupportsFileBasedCompression)
        print("36. SystemCreationClassName:", logical_unit.SystemCreationClassName)
        print("37. VolumeDirty:", logical_unit.VolumeDirty)

        print("-" * 40)





















'///////////////////////////////////////////////////////////////////////////////////////////////////////////////'
'******************************************    M  E  N  U    MODULE    *****************************************'
'///////////////////////////////////////////////////////////////////////////////////////////////////////////////'

'| 1 # |************************************** MENU O P T I O N S **************************************' 
#1 MENU OPTIONS
while True:
    print("")
    print("PLEASE SELECT AN OPTION EXAMPLE: 1,2,3,4,e,ETC\n")
    print("        ==== M E N U ====  ")
    print("                           ")
    print("          O P T I O N S    ")
    print("                           ")
    print("      ____- D I S K S -____")
    print("(1) - [    DISKS  INFO    ]")
    print("(2) - [  PARTITIONS  INFO ]")
    print("(3) - [   VOLUMES INFO    ]")
    print("(4) - [LOGICAL DISKS  INFO]")
    print("                           ")
    print("                           ")
    print("(e) - [   EXIT  PROGRAM   ]")
    print("")
 
 # MENU
    '| 2 # | ****************************************** M E N U ************************************'

    option = input ("SELECT AN OPTION: ")

    if option == "1":
        list_disk()
    elif option == "2":
        list_partition()
    elif option == "3":
        list_volume()
    elif option == "4":
        list_logicaldisk()
    elif option == "e":
        print("EXIT PROGRAM SUCCESFULL...")
        break 
    else:
        print("\n_I N V A L I D  -  O P T I O N_\n")



