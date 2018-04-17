import psutil, platform, getpass, socket, os

platform = platform.system()
current_user = getpass.getuser()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(socket.gethostname())

print(os.name)

def get_os():
    if psutil.OSX:
        return 'Mac OS'
    elif psutil.WINDOWS:
        return 'Windows'
    elif psutil.LINUX:
        return 'Linux'

print(get_os())

print(platform, current_user, hostname, ip_address)

processes = []
for pid in psutil.pids():
    p = psutil.Process(pid)
    processes.append(p.name())
    #if p.name()  == 'Google Chrome':
    #    p.terminate()

print(processes)



#https://pypi.org/project/psutil/

