import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZmluZEdvb2RTdHJpbmdzKHNlbGYsIE4sICphcmdzKSA6CiAgICAgICAgZnJvbSBmdW5jdG9vbHMgaW1wb3J0IGxydV9jYWNoZQogICAgICAgIHMxLHMyLCBldmlsID0gW2xpc3QobWFwKG9yZCwgaSkpIGZvciBpIGluIGFyZ3NdCiAgICAgICAgbW9kID0gMTAgKiogOSArIDcKICAgICAgICAKICAgICAgICBkZWYga21wKGwsIGMpOgogICAgICAgICAgICB3aGlsZSBsIGFuZCBldmlsW2xdICE9IGM6IGwgPSBmW2wtMV0KICAgICAgICAgICAgaWYgZXZpbFtsXSA9PSBjIDogbCArPSAxCiAgICAgICAgICAgIHJldHVybiBsCiAgICAgICAgCiAgICAgICAgZiA9IFswXSAqIGxlbihldmlsKSAKICAgICAgICBmb3IgaSBpbiByYW5nZSgxLCBsZW4oZXZpbCkpOgogICAgICAgICAgICBmW2ldID0ga21wKGZbaS0xXSwgZXZpbFtpXSkKICAgICAgICAKICAgICAgICBAbHJ1X2NhY2hlKE5vbmUpCiAgICAgICAgZGVmIGRwKGkgPSAwLCBsY3AgPSAwICwgZjEgPSBGYWxzZSwgZjIgPSBGYWxzZSk6CiAgICAgICAgICAgIGlmIGxjcCA9PSBsZW4oZXZpbCk6IHJldHVybiAwIAogICAgICAgICAgICBpZiBpID09IE4gOiByZXR1cm4gMQogICAgICAgICAgICBhbnMgPSAwCiAgICAgICAgICAgIGZvciBjaGFyIGluIHJhbmdlKGYxIGFuZCA5NyBvciBzMVtpXSwgZjIgYW5kIDEyMyBvciBzMltpXSsxKToKICAgICAgICAgICAgICAgIGFucyArPSBkcChpKzEsIGttcChsY3AsIGNoYXIgKSwgZjEgb3IgY2hhciA+IHMxW2ldLCBmMiBvciBjaGFyIDwgczJbaV0pCiAgICAgICAgICAgICAgICBhbnMgJT0gbW9kIAogICAgICAgICAgICByZXR1cm4gYW5zIAoKICAgICAgICByZXR1cm4gZHAoKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
