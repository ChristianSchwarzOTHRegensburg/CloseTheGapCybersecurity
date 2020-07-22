import hashlib

#use the provided files or generate some simple ones to check if you can find them
files_to_check = ["TestFile.py", "TestFile2.py"]
sha256_hash = hashlib.sha256()


def print_hash(str):
    with open(file,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        print(sha256_hash.hexdigest())

#open each file and generate a hash for it
for file in files_to_check:
    print_hash(file)


