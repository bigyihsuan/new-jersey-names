from collections import Counter
import json
import re
from bs4 import BeautifulSoup
import bs4
import requests
import wikipediaapi

# wikipediaapi.log.setLevel(level=wikipediaapi.logging.DEBUG)
# out_hdlr = wikipediaapi.logging.StreamHandler(sys.stderr)
# out_hdlr.setFormatter(
#     wikipediaapi.logging.Formatter('%(asctime)s %(message)s'))
# out_hdlr.setLevel(wikipediaapi.logging.DEBUG)
# wikipediaapi.log.addHandler(out_hdlr)

pages = [
    "Category:Unincorporated_communities_in_New_Jersey",
    "Category:Census-designated_places_in_New_Jersey"
]

user_agent = ""
with open("./secret.txt", "r") as secrets:
    user_agent = secrets.readline().strip()

if user_agent == "":
    exit(1)

wiki = wikipediaapi.Wikipedia(
    user_agent, "en", extract_format=wikipediaapi.ExtractFormat.WIKI)

names: list[str] = []
cdp: list[str] = []
for name in pages:
    page = wiki.page(name, ns=wikipediaapi.Namespace.CATEGORY)
    n = [wiki.page(entry).title.partition(",")[0] for entry in page.categorymembers if entry.endswith(", New Jersey")]
    names.extend(n)
    cdp.extend(n)

url = "https://en.wikipedia.org/w/api.php?action=parse&page=List_of_municipalities_in_New_Jersey"
headers = {"User-Agent": user_agent}
page_text = requests.get(url=url, headers=headers).text
nodes = BeautifulSoup(page_text, features="html.parser")
pre = nodes.find("pre", recursive=True)
if not pre:
    exit(1)

data = json.loads(pre.text)
text = data["parse"]["text"]["*"]
text_nodes = BeautifulSoup(text, features="html.parser")
table = text_nodes.table
if not table:
    exit(1)
tbody = table.tbody
if not tbody:
    exit(1)
trs: list[bs4.Tag] = tbody.findChildren("tr")[2:]
municpalities = [td.get_text().strip()
                 for tr in trs for i, td in enumerate(tr.children) if i == 1]
with open("names/municipalities.txt", "w") as municpality_file:
    municpality_file.write("\n".join(municpalities))
names.extend(municpalities)

cdp = [name for name in cdp if cdp not in municpalities]
with open("names/cdp.txt", "w") as cdp_file:
    cdp = [name.removesuffix(" (CDP)").removesuffix(
        " (unincorporated community)") for name in cdp]
    cdp = list(set(cdp))
    cdp.sort()
    cdp_file.write("\n".join(cdp))

names = [name.removesuffix(" (CDP)").removesuffix(
    " (unincorporated community)") for name in names]
names = list(set(names))
names.sort()

with open("names.txt", "w") as name_file:
    name_file.write("\n".join(names))

double_names = [name for name in names if " " in name or "-" in name]

flattened_double_names = [
    part for name in names for part in re.split(r" |-", name)]
counter: Counter[str] = Counter(flattened_double_names)

common_parts = sorted(counter)

with open("parts.txt", "w") as parts:
    for part in common_parts:
        parts.write(part + "\n")

# short_municpalities: list[str] = municpalities[:]
# for part, count in sorted(counter.items(), key=lambda item: item[1], reverse=True):
#     short_municpalities = [name.removesuffix(
#         part) for name in short_municpalities]

# for name in short_municpalities:
#     print(name)
