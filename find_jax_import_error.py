import sys
import importlib

targets = ["flax", "chex", "optax", "orbax", "orbax.checkpoint"]

for pkg in targets:
    try:
        print(f"Testing import: {pkg}")
        importlib.import_module(pkg)
        print(f"✅ {pkg} imported successfully\n")
    except Exception as e:
        print(f"❌ {pkg} caused error:\n{e}\n")


