import easyjson
import os
import nbt
import nbt.nbt
import tomllib

cfg = tomllib.load(open("cfg.toml","rb"))

n = nbt.nbt.NBTFile("output.nbt")
n["items"]

items =list(n["items"])




template = [
  {
    "duration": cfg["duration"],
    "group":cfg["group"],
    "temperature_level":cfg["temperature_level"]
  }
]

mode = cfg["mode"]
template_thirst = [
  {
    "effects": cfg["effects"],
    "hydration": cfg["hydration"],
    "properties": cfg["properties"],
    "saturation": cfg["saturation"]
  }
]

if mode == "thirst":
    template = template_thirst



for _item in items:
    item = str(_item)
    modid = item.split(":")[0]
    itemid = item.split(":")[1]
    if not os.path.isdir("output/"+modid):os.mkdir("output/"+modid)
    if not os.path.isdir(f"output/{modid}/legendarysurvivaloverhaul/"):os.mkdir(f"output/{modid}/legendarysurvivaloverhaul/")
    if not os.path.isdir(f"output/{modid}/legendarysurvivaloverhaul/{mode}"):os.mkdir(f"output/{modid}/legendarysurvivaloverhaul/{mode}")
    if not os.path.isdir(f"output/{modid}/legendarysurvivaloverhaul/{mode}/consumables"):os.mkdir(f"output/{modid}/legendarysurvivaloverhaul/{mode}/consumables")

    easyjson.dump_to_file(template,f"output/{modid}/legendarysurvivaloverhaul/{mode}/consumables/{itemid}.json")
