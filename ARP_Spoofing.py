# This program will be able to identify ARP spoofing behavior in Computer's using the ARP table

# importing the essential libraries for the program
import os
import re
import datetime

# Main menu, where will be receiving input from the user and creating the "choice" variable.
while True:
    print("This program will check for ARP spoofing in the ARP table, it was meant for MacOS, Windows 10, and Kali Linux!! However, Imagination is Free!!\n")
    print("====================================================================================================")
    print("====================================================================================================")
    choice = input("Would you like to proceed? If \"Yes\", please type \"Y\" or \"y\" for Yes, or any other key to exit the program: ")
    print("======================================================================================================================================================")
    print("======================================================================================================================================================")

# ARP Table function call the ARP table command to extract it each line from the output generated
    def ARP_TABLE_EXTRACTION(choice):
        if choice == "Y" or choice == "y":
         print("\nRemember to check if that file path and file extension are correct!! if not the file won't be created!! " +
              " If any of this is not created correctly the task will not be performed and an error may occurred!!\n")
         print("======================================================================================================================================================")
         Path = input("Define the path, name, and extension of the file where it will be created, accordingly with the OS: ")
         print("======================================================================================================================================================")
         print("======================================================================================================================================================")
         os.system("arp -a >> " + Path)
         with open(Path, "r") as file:
            ARP = file.readlines()
            ARP_Line = []
            for line in ARP:
                ARP_Line.append(line)
         return(ARP_Line)
        else:
            print("====================================================================================================")
            print("You have chosen to exit the program!!!")
            print("====================================================================================================")
            raise SystemExit

# Get IPv4 and Mac Address Function to filter the address from the rest of the data
    def get_ip_and_mac(line):

        Each_line = line

        List = []
        for line in Each_line:
            mac_address_pattern_linux = re.compile(r'([0-9a-f]{1,2}(?::[0-9a-f]{1,2}){5})')
            mac_address_pattern_windows = re.compile(r'(?:[0-9a-fA-F]-?){12}')
            ip_address_pattern = re.compile(r"\b\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\b")
            mac_addresses = re.findall(mac_address_pattern_linux, line) + re.findall(mac_address_pattern_windows, line)
            ip_addresses = re.findall(ip_address_pattern, line)
            if mac_addresses and ip_addresses:
                if (str(mac_addresses).lower() != "ff:ff:ff:ff:ff:ff") or (str(mac_addresses).lower() != "ff-ff-ff-ff-ff-ff"):
                    List.append(f"{ip_addresses}")
                    List.append(f"{mac_addresses}")
                else:
                    return None, None
            else:
                return None, None
        return List

# Spoofing Identification Function to separate the Mac Addresses from the IPv4 Addresses. Furthermore, it will identify if a Mac Address has been spoofed or not
    def Spoofing_Identification(Addresses):

        mac_addresses = []
        i = 1
        while i < len(Addresses):
            mac_addresses.append(Addresses[i])
            i += 2

        x = 1
        Checking_Mac = set()
        for elem in mac_addresses:
            if elem in Checking_Mac:
                print("======================================================================================================================================================")
                print("Oops!!\n")
                print(f"The address {elem} has been spoofed!! Same Mac address assigned to more than one IPv4 in the ARP table. For more info, Check your Log_Spoofing.txt file\n\n\n")
                print("======================================================================================================================================================")
                return elem
            else:
                Checking_Mac.add(elem)
                print(f" {x}- Great News!! This {elem} Mac Address was checked for the first time!\n")
                x += 1
        print("====================================================================================================")
        print("Great News! You are Spoof free!")
        print("====================================================================================================\n\n\n")


# Log Events Function will create a log file to give additional information about the spoofing
    def log_Events(Alert):

        now = datetime.datetime.now()
        Log = f"The Mac Address \"{Alert}\" at {now}\n"
        os.system("touch Log_Spoofing.txt\n")
        Log_File = open("Log_Spoofing.txt", "a")
        Log_File.write(Log)
        Log_File.close()

# Calling the Functions
    log_Events(Spoofing_Identification(get_ip_and_mac(ARP_TABLE_EXTRACTION(choice))))

# Giving the user the option to repeat the program, if not it will be terminated
    Rerun = input("Would you like to run the program again? If yes, please type \"Y\" or \"y\" for Yes, or any other key to exit the program: ")
    print("************************************************************************************************************************************")
    print("************************************************************************************************************************************")
    if Rerun == "Y" or Rerun == "y":
        continue
    else:
        raise SystemExit













