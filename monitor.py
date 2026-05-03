#!/usr/bin/env python3
import time
import csv
from datetime import datetime
import psutil

# optional GPU lib
try:
    import GPUtil
    _GPUTIL_AVAILABLE = True
except Exception:
    _GPUTIL_AVAILABLE = False

CSV_FILE = "system_metrics.csv"
SAMPLE_INTERVAL = 10.0  # seconds between samples

FIELDNAMES = ["time", "cpu_usage_perc", "ram_usage_perc", "vram_usage_perc", "gpu_perc"]

def get_timestamp():
    # dd.mm.yyyy hour:minute:segundo
    return datetime.now().strftime("%d.%m.%Y (%H:%M:%S)->")

def get_cpu_percent(interval=None):
    # psutil.cpu_percent with interval: non-blocking if interval is None (returns last cached)
    # We call with interval=0.0 to get instant sample (may be 0 on first call), so use small interval if desired.
    return psutil.cpu_percent(interval=interval or 0.1)

def get_ram_percent():
    return psutil.virtual_memory().percent

def get_gpu_stats():
    # Returns (vram_percent, gpu_percent) aggregated across GPUs (average). Returns (None, None) if unavailable.
    if not _GPUTIL_AVAILABLE:
        return None, None
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return None, None
        # average across all GPUs
        vram_percs = [g.memoryUtil * 100 for g in gpus]        # memoryUtil is 0..1
        gpu_percs = [g.load * 100 for g in gpus]               # load is 0..1
        return sum(vram_percs) / len(vram_percs), sum(gpu_percs) / len(gpu_percs)
    except Exception:
        return None, None

def ensure_csv_header(path):
    try:
        with open(path, "r", newline="") as f:
            pass
    except FileNotFoundError:
        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def main():
    ensure_csv_header(CSV_FILE)

    # Prime CPU percent measurements
    psutil.cpu_percent(interval=None)

    try:
        while True:
            tstamp = get_timestamp()
            cpu = get_cpu_percent(interval=0.1)
            ram = get_ram_percent()
            vram, gpu = get_gpu_stats()

            row = {
                "time": tstamp,
                "cpu_usage_perc": f"{cpu:.1f}",
                "ram_usage_perc": f"{ram:.1f}",
                "vram_usage_perc": f"{vram:.1f}" if vram is not None else "",
                "gpu_perc": f"{gpu:.1f}" if gpu is not None else "",
            }

            with open(CSV_FILE, "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
                writer.writerow(row)

            # sleep until next sample
            time.sleep(SAMPLE_INTERVAL)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    main()
