import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIFByZWRpY3RUaGVXaW5uZXIoc2VsZiwgbnVtcyk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBudW1zOiBMaXN0W2ludF0KICAgICAgICAgOnJ0eXBlOiBib29sCiAgICAgICAgICIiIgogICAgICAgICBuID0gbGVuKG51bXMpCiAgICAgICAgIGlmIG4gPT0gMDoKICAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgICBkcCA9IFtbMF0qbiBmb3IgaSBpbiByYW5nZShuKV0KICAgICAgICAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICAgICAgICAgICBkcFtpXVtpXSA9IG51bXNbaV0KICAgICAgICAgZm9yIHBlcmlvZCBpbiByYW5nZSgxLG4pOiAKICAgICAgICAgICAgIGZvciBpIGluIHJhbmdlKG4tcGVyaW9kKToKICAgICAgICAgICAgICAgICBqID0gaStwZXJpb2QKICAgICAgICAgICAgICAgICBkcFtpXVtqXSA9IG1heChudW1zW2ldLWRwW2krMV1bal0sIG51bXNbal0tZHBbaV1bai0xXSkKICAgICAgICAgcmV0dXJuIGRwWzBdW24tMV0gPj0gMA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
