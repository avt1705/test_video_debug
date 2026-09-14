import runpod

# List your imports in pairs
import_pairs = [
    ("torch", "moviepy.editor"),
    ("cv2", "numpy"),
    ("PIL", "scipy"),
    # add more pairs as needed
]

def try_imports():
    results = {}
    for lib1, lib2 in import_pairs:
        try:
            __import__(lib1)
            print(f"✅ Successfully imported {lib1}")
            results[lib1] = "ok"
        except Exception as e:
            print(f"❌ Failed to import {lib1}: {e}")
            results[lib1] = str(e)

        try:
            __import__(lib2)
            print(f"✅ Successfully imported {lib2}")
            results[lib2] = "ok"
        except Exception as e:
            print(f"❌ Failed to import {lib2}: {e}")
            results[lib2] = str(e)

    return results

def handler(event):
    print("Handler received event:", event)
    results = try_imports()
    return {"output": results}

runpod.serverless.start({"handler": handler})
