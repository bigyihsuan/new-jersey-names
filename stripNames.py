cores: list[str] = []
suffixes: list[str] = []

with open("names/core.txt", "r") as core_file, open("names/suffix.txt", "r") as suffix_file:
    cores = [line.strip() for line in core_file.readlines()]
    suffixes = [line.strip() for line in suffix_file.readlines()]

stub_suffixes = ["ton", "town", "ville", "wood", "burg",
                 "field", "dale", "lawn", "ford", "boro", "land", "side"]

cores_names = {
    suffix: [name.removesuffix(suffix) for name in cores if name.endswith(suffix)] for suffix in stub_suffixes
}

with open("names/core-stub.txt", "w") as core_stub, open("names/new-suffix.txt", "w") as suffix_file:
    c = sorted(set(e for l in cores_names.values() for e in l))
    s = sorted(set(l for l in cores_names.keys()))
    for core in c:
        core_stub.write(core + "\n")
    for suffix in s:
        suffix_file.write(suffix + "\n")
    for suffix in suffixes:
        if suffix[0].isupper():
            suffix_file.write(" " + suffix + "\n")
        else:
            suffix_file.write(suffix + "\n")
