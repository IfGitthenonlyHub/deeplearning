import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4UHJvZml0QXNzaWdubWVudChzZWxmLCBkaWZmaWN1bHR5LCBwcm9maXQsIHdvcmtlcik6CiAgICAgICAgam9icyA9IHNvcnRlZCh6aXAoZGlmZmljdWx0eSwgcHJvZml0KSkKICAgICAgICBhbnMgPSBpID0gYmVzdCA9IDAKICAgICAgICBmb3Igc2tpbGwgaW4gc29ydGVkKHdvcmtlcik6CiAgICAgICAgICAgIHdoaWxlIGkgPCBsZW4oam9icykgYW5kIHNraWxsID49IGpvYnNbaV1bMF06CiAgICAgICAgICAgICAgICBiZXN0ID0gbWF4KGJlc3QsIGpvYnNbaV1bMV0pCiAgICAgICAgICAgICAgICBpICs9IDEKICAgICAgICAgICAgYW5zICs9IGJlc3QKICAgICAgICByZXR1cm4gYW5z").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
