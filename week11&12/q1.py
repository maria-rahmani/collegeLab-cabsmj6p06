# Initialize the server configuration
server_config = {"timeout": 300, "status": "active"}

print("=== Debug Console: Server Configuration ===\n")

# • Read & Inspect
print("Read & Inspect")
print(f"1. Status: {server_config['status']}")

admin_email = server_config.get("admin_email", "Not Set")
print(f"2. Admin Email: {admin_email}")

print(f"3. Total number of settings: {len(server_config)}")

print(f"4. Keys: {list(server_config.keys())}")
print(f"   Values: {list(server_config.values())}\n")

# • Modify
print("Modify")
server_config["timeout"] = -server_config["timeout"]
print(f"1. Updated 'timeout' to: {server_config['timeout']}")

server_config["max_connections"] = 100
print(f"2. Added 'max_connections': {server_config['max_connections']}\n")

# • Clean Up
print("Clean Up")
if "timeout" in server_config:
    removed_timeout = server_config.pop("timeout")
    print(f"Removed 'timeout' key with value: {removed_timeout}")
else:
    print("No 'timeout' key to remove.\n")

# • Sort
print("Sort")
remaining_keys = sorted(server_config.keys())
print(f"Remaining keys in alphabetical order: {remaining_keys}")  
