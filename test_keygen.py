import os
import shutil

from crypto.keygen import generate_keys, stub_generate_keys

def test_keygen():
    test_dir = "temp_keygen_test"
    os.makedirs(test_dir, exist_ok=True)

    print("\n---Testing key generation---")
    private_path, public_path = generate_keys(test_dir)
    print("Private key file path:", private_path)
    print("Public key file path:", public_path)

    with open(private_path) as private_key_file:
        print("Private key first line:", private_key_file.readline())
    with open(public_path) as public_key_file:
        print("Public key first line:", public_key_file.readline())

    print("\n---Testing stub function---")
    stub_private_path, stub_public_path = stub_generate_keys(test_dir)
    print("Stub private key file path:", stub_private_path)
    print("Stub public key file path:", stub_public_path)

    with open(stub_private_path) as stub_private_key_file:
        print("Stub private key first line:", stub_private_key_file.readline())
    with open(stub_public_path) as stub_public_key_file:
        print("Stub public key first line:", stub_public_key_file.readline())

    shutil.rmtree(test_dir)
    print(f"\nTemp test directory {test_dir} deleted for cleanup")

if __name__ == "__main__":
    test_keygen()