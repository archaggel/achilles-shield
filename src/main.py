print("========================================")
print("        ACHILLES' SHIELD")
print("             ASPIS")
print("    AI Security & Safety Agent")
print("========================================")
print()
print("Version: 0.1")
print()
print("Observe. Analyze. Protect.")
print("Never act beyond authority.")
print()
print("ASPIS ready.")

event = input("Enter security event:")

print()
print("Event received:")
print(event)

if "failed login" in event.lower():
    print()
    print("Category: Authentication Event")
    print("Risk Level: LOW")
    print("Recommendation: Review authentication logs.")
    print("Human Approval Required: YES")
    
elif "nmap" in event.lower():
    print()
    print("Category: Reconnaissance")
    print("Risk Level: MEDIUM")
    print("Recommendation: Investigate source IP and correlate with firewall logs.")
    print("Human Approval Required: YES")

else:
    print()
    print("Category: Unknown")
    print("Risk Level: UNDETERMINED")
    print("Recommendation: Manual review required.")
    print("Human Approval Required: YES")
        