import math

with open("names/municipalities.txt") as municipalities:
    munc_names = [m.strip() for m in municipalities.readlines()]
    print("town_names(municipalities) {")
    print("    {")
    print(",\n".join(
        # [f'        text("{municipality.strip()}", {math.ceil((m:=len(munc_names))/(i+m/127)) or 1})' for i, municipality in enumerate(munc_names)]))
        [f'        text("{municipality.strip()}", {math.ceil(math.exp(-(i-1)/127+4.84))-1 or 1})' for i, municipality in enumerate(munc_names)]))
    print("    }")
    print("}")

with open("names/cdp.txt") as cdp:
    cdp_names = [m.strip() for m in cdp.readlines()]
    print("town_names(cdp) {")
    print("    {")
    print(",\n".join(
        [f'        text("{cdp.strip()}", {1})' for i, cdp in enumerate(cdp_names)]))
    print("    }")
    print("}")

with open("names/prefix.txt") as prefixes:
    print("town_names(prefixes) {")
    print("    {")
    print(",\n".join(
        [f'        text("{prefix.strip()} ", 1)' for prefix in prefixes.readlines()]))
    print("    }")
    print("}")

with open("names/new-suffix.txt") as suffixes:
    print("town_names(suffixes) {")
    print("    {")
    print(",\n".join(
        [f'        text("{suffix.rstrip()}", 1)' for suffix in suffixes.readlines()]))
    print("    }")
    print("}")

with open("names/core-stub.txt") as corestubs:
    print("town_names(corestubs) {")
    print("    {")
    print(",\n".join(
        [f'        text("{stub.strip()}", 1)' for stub in corestubs.readlines()]))
    print("    }")
    print("}")

with open("names/core.txt") as core:
    print("town_names(core) {")
    print("    {")
    print(",\n".join(
        [f'        text("{core.strip()}", 1)' for core in core.readlines() if all(core.strip() not in name for name in munc_names)]))
    print("    }")
    print("}")
