import os
print("Turning on display backlight")
os.system("sudo sh -c 'echo 0 > /sys/class/backlight/10-0045/bl_power'")
print("Enabling Bluetooth")
os.system("sudo rfkill unblock bluetooth")
print("Setting CPU to performance mode")
os.system("sudo sh -c 'echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'")

