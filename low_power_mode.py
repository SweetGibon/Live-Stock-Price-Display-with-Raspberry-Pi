import os
print("Turning off display backlight")
os.system("sudo sh -c 'echo 1 > /sys/class/backlight/10-0045/bl_power'")
print("Disabling Bluetooth")
os.system("sudo rfkill block bluetooth")
print("Setting CPU to powersave mode")
os.system("sudo sh -c 'echo powersave > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'")

