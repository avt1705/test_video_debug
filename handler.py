import runpod

def handler(event):
    print(">>> Handler received event:", event)
    return {"output": "Hello world"}

runpod.serverless.start({"handler": handler})
