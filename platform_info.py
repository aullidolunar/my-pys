import platform

info = {
    "Machine": platform.machine(),
    "Platform": platform.platform(),
    "System": platform.system(),
}

for label, value in info.items():
    print(f"{label}: {value}")
