#Lab 6: Handling Datasets using Dictionaries, Sets and Serializing Objects

#1a
print("Simple Dictionary:")
dictionary = {"user": "addie", "month": "may", "day": "monday"}
print(dictionary)
#1b
line = "Jun 14 15:16:01 combo sshd(pam_unix)[19939]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=218.188.2.4"
log = {
    "time": "15:16:01",
    "uhhh": "combo sshd(pam_unix)",
    "section": "[19939]",
    "authentication": "authentication failure;",
    "logname": " ",
    "uid": "0",
    "euid": "0",
    "tty": "NODEVssh",
    "ruser": " ",
    "rhost": "218.188.2.4",
    }
print("Time:", log["time"])
#2a
dictionary["email"] = "addie.price@oit.edu"
del dictionary["day"]
dictionary["user"] = "price"
print(dictionary)
#2b
log["date"] = "Jun 14"
del log["uhhh"]
log["time"] = "14:15:02"
print(log)
#3
nested = {
    "Students": {"Name": "John", "ID": "918314567", "Major": "Writing"},
    "Faculty": {"Name": "Jessie", "ID": "918242424", "Class": "Math"}
}
print(nested)
#4
line = "Jun 14 15:16:01 combo sshd(pam_unix)[19939]: authentication failure; logname= uid=0 euid=0 tty=NODEVssh ruser= rhost=218.188.2.4"
line_2 = "Jun 14 15:16:02 combo sshd(pam_unix)[19937]: check pass; user unknown"
log_2 = {
    "Set One": {"Date": "Jun 14", "Time": "15:16:01", "authentication": "failure"},
    "Set Two": {"Date": "Jun 14", "Time": "15:16:02", "authentication": "pass"},
}
print(log_2)
#5
print(list(dictionary.keys()))
print(list(dictionary.values()))
print(list(dictionary.items()))
print(dictionary.get("user"))
print(len(dictionary))
#6
sodas = ["ginger ale", "dr. pepper", "rootbeer", "fanta"]
count = {sodas: sodas.count(sodas) for sodas in set(sodas)}
print(count)
#7
unique = []
seen = set()
with open("Linux_2k.log.txt") as f:
    for line in f:
        for line in line.split():
            if line.startswith("rhost="):
                raw = line.split("=", 1)[1]
                s = ''.join(ch for ch in raw if ch.isdigit() or ch == '.')
                s = s.strip('.')
                parts = [p for p in s.split('.') if p != '']
                parts = parts[:4]
                ip = '.'.join(parts)
                if ip and ip not in seen:
                    seen.add(ip)
                    unique.append(ip)
                break
print(unique)
#8
unique_ips = list(set(unique))
print(unique_ips)
#student activity
unique_times = []
seen = set()
with open("Linux_2k.log.txt") as f:
    for line in f:
        if not line.strip():
            continue
        words = line.split()
        if len(words) >= 3:
            timestamp = words[0] + " " + words[1] + " " + words[2]
            if timestamp not in seen:
                seen.add(timestamp)
                unique_times.append(timestamp)

print(unique_times)