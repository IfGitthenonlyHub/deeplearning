import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGluY3JlYXNpbmdUcmlwbGV0KHNlbGYsIG51bXMpOgogICAgICAgICBmaXJzdCA9IHNlY29uZCA9IGZsb2F0KCdpbmYnKQogICAgICAgICAKICAgICAgICAgZm9yIG4gaW4gbnVtczoKICAgICAgICAgICAgIGlmIG4gPD0gZmlyc3Q6CiAgICAgICAgICAgICAgICAgZmlyc3QgPSBuCiAgICAgICAgICAgICBlbGlmIG4gPD0gc2Vjb25kOgogICAgICAgICAgICAgICAgIHNlY29uZCA9IG4KICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgcmV0dXJuIFRydWUKICAgICAgICAgcmV0dXJuIEZhbHNl").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
