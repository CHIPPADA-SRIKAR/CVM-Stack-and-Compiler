import os
import subprocess

TEST_DIRS = ["tests/valid", "tests/expressions", "tests/controlflow", "tests/invalid"]
EXECUTABLE = "./main" # Use "main.exe" if you are on Windows CMD

def run_tests():
    if not os.path.exists(EXECUTABLE):
        print(f"Error: {EXECUTABLE} not found. Run 'make' first.")
        return

    total, passed = 0, 0

    for test_dir in TEST_DIRS:
        if not os.path.exists(test_dir):
            continue
            
        print(f"\n--- Running tests in {test_dir} ---")
        for filename in os.listdir(test_dir):
            if not filename.endswith(".cvm"): continue
            
            total += 1
            filepath = os.path.join(test_dir, filename)
            result = subprocess.run([EXECUTABLE, filepath], capture_output=True, text=True)

            # Invalid tests SHOULD fail or throw errors
            if "invalid" in test_dir:
                if result.returncode != 0 or "Error" in result.stdout or "Error" in result.stderr:
                    print(f"  [PASS] {filename} (Caught syntax/runtime error as expected)")
                    passed += 1
                else:
                    print(f"  [FAIL] {filename} (Expected an error, but it compiled!)")
            # Valid tests SHOULD pass
            else:
                if result.returncode == 0 and "Error" not in result.stdout:
                    print(f"  [PASS] {filename}")
                    passed += 1
                else:
                    print(f"  [FAIL] {filename}\n         Output: {result.stdout.strip()}")

    print(f"\n=== Test Summary: {passed}/{total} Passed ===")

if __name__ == "__main__":
    run_tests()