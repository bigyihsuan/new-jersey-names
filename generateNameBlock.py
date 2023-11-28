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
        [f'        text("{core.strip()}", 1)' for core in core.readlines()]))
    print("    }")
    print("}")


with open("names/municipalities.txt") as municipalities:
    print("town_names(municipalities) {")
    print("    {")
    print(",\n".join(
        [f'        text("{municipality.strip()}", 1)' for municipality in municipalities.readlines()]))
    print("    }")
    print("}")
