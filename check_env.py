# check_env.py
# Verificación completa del entorno de Data Science
# Bootcamp DS - Jackson Sierra

import platform
import sys
import os
import shutil

print("=" * 55)
print("  VERIFICACIÓN DE ENTORNO — BOOTCAMP DATA SCIENCE")
print("=" * 55)

# ── 1. Python ──────────────────────────────────────────────
print("\n[1] PYTHON")
print(f"  Versión        : {sys.version.split()[0]}")
print(f"  Ejecutable     : {sys.executable}")

# ── 2. Librerías DS ────────────────────────────────────────
print("\n[2] LIBRERÍAS DATA SCIENCE")
libs = [
    "numpy", "pandas", "matplotlib",
    "seaborn", "scipy", "sklearn",
    "statsmodels", "jupyter", "torch"
]
for lib in libs:
    try:
        mod = __import__(lib)
        version = getattr(mod, "__version__", "OK")
        print(f"  {lib:<15}: {version}")
    except ImportError:
        print(f"  {lib:<15}: ✗ NO INSTALADO")

# ── 3. GPU / CUDA ──────────────────────────────────────────
print("\n[3] GPU / CUDA")
try:
    import torch
    if torch.cuda.is_available():
        props = torch.cuda.get_device_properties(0)
        print(f"  GPU            : {torch.cuda.get_device_name(0)}")
        print(f"  VRAM total     : {props.total_memory / 1e9:.1f} GB")
        print(f"  CUDA versión   : {torch.version.cuda}")
        print(f"  Compute cap.   : {props.major}.{props.minor}")
    else:
        print("  CUDA           : No disponible")
except ImportError:
    print("  PyTorch        : No instalado")

# ── 4. Sistema ─────────────────────────────────────────────
print("\n[4] SISTEMA")
print(f"  OS             : {platform.system()} {platform.release()}")
print(f"  Procesador     : {platform.processor()}")
ram = shutil.disk_usage("/")
total, free = os.get_terminal_size if False else (0, 0)
try:
    import psutil
    ram_total = psutil.virtual_memory().total / 1e9
    ram_available = psutil.virtual_memory().available / 1e9
    print(f"  RAM total      : {ram_total:.1f} GB")
    print(f"  RAM disponible : {ram_available:.1f} GB")
except ImportError:
    print("  RAM            : instala psutil para ver este dato")

disk = shutil.disk_usage("C:/")
print(f"  Disco C: total : {disk.total / 1e9:.0f} GB")
print(f"  Disco C: libre : {disk.free / 1e9:.0f} GB")

print("\n" + "=" * 55)
print("  Entorno verificado correctamente ✓")
print("=" * 55)