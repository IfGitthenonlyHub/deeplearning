import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG1heGltdW1Td2FwKHNlbGYsIG51bSk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBudW06IGludAogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgQSA9IGxpc3Qoc3RyKG51bSkpCiAgICAgICAgIGFucyA9IEFbOl0KICAgICAgICAgZm9yIGkgaW4gcmFuZ2UobGVuKEEpKToKICAgICAgICAgICAgIGZvciBqIGluIHJhbmdlKGkrMSwgbGVuKEEpKToKICAgICAgICAgICAgICAgICBBW2ldLCBBW2pdID0gQVtqXSwgQVtpXQogICAgICAgICAgICAgICAgIGlmIEEgPiBhbnM6IGFucyA9IEFbOl0KICAgICAgICAgICAgICAgICBBW2ldLCBBW2pdID0gQVtqXSwgQVtpXQogCiAgICAgICAgIHJldHVybiBpbnQoIiIuam9pbihhbnMpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
