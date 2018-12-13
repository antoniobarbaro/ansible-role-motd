import psutil
import platform
import datetime

cpu_perc = psutil.cpu_percent(interval=1, percpu=True)
boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
total_memory = round(psutil.virtual_memory().total / (1024.0 ** 3),2)    #  memory in Gb
used_memory = round(psutil.virtual_memory().used / (1024.0 ** 3),2)    #  memory in Gb
percent_memory = psutil.virtual_memory().percent
total_swap_memory = round(psutil.swap_memory().total / (1024.0 ** 3),2)    #  memory in Gb
used_swap_memory = round(psutil.swap_memory().used / (1024.0 ** 3),2)    #  memory in Gb
percent_swap_memory = psutil.swap_memory().percent

def print_disk_usage():
    partitions=psutil.disk_partitions()
    for item in partitions:    
        disk_usage = psutil.disk_usage(item.mountpoint)
        total_disk_usage = round(disk_usage.total / (1024.0 ** 3),2)    #  disk usage in Gb
        used_disk_usage = round(disk_usage.used / (1024.0 ** 3),2)    #  disk usage in Gb
        percent_disk_usage = disk_usage.percent
        print '- Disk Usage....: {:5.2f} / {:5.2f} Gb {:3.1f}% - mountpoint: {:s}'.format(used_disk_usage,total_disk_usage,percent_disk_usage,item.mountpoint)

def print_net_address():
    net_address=psutil.net_if_addrs()
    for key, value in net_address.iteritems():        
        print '- Network.......: card {:14s} ip {:18s} mask {:s}'.format(key,value[0].address,value[0].netmask)


print("==============================================================================")
print("- Hostname......: "+platform.node())
print("- System Info...: "+platform.system()+" - "+platform.release()+" - "+platform.machine())
print("- CPU type......: "+platform.processor())
print("- Boot time.....: "+str(boot_time))
cpu_usage = "- CPU Usage.....: "
for count, item in enumerate(cpu_perc, start=1):
    cpu_usage = cpu_usage + "CPU" + str(count) + ":" + str(item)+ "%  "
print(cpu_usage)
print '- Memory........: {:5.2f} / {:5.2f} Gb {:3.1f}%'.format(used_memory,total_memory,percent_memory)
print '- Swap Memory...: {:5.2f} / {:5.2f} Gb {:3.1f}%'.format(used_swap_memory,total_swap_memory,percent_swap_memory)
print_disk_usage()
print_net_address()
print("==============================================================================")





