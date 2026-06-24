BLOCKED_PATTERNS = [
    "<",
    ">",
    "script",
    "javascript:",
    "onerror",
    "onload"
]

test_inputs = [
    "Hello World",
    "Welcome User",
    "<example>",
    "javascript:test",
    "Sample Text",
    "onload event",
    "Good Morning"
]

print("=" * 50)
print("WAF FILTER ANALYSIS REPORT")
print("=" * 50)

for text in test_inputs:
    blocked = False
    reason = ""

    for pattern in BLOCKED_PATTERNS:
        if pattern.lower() in text.lower():
            blocked = True
            reason = pattern
            break

    if blocked:
        print(f"\nInput : {text}")
        print("Status: BLOCKED")
        print(f"Reason: Matched '{reason}'")
    else:
        print(f"\nInput : {text}")
        print("Status: ALLOWED")
