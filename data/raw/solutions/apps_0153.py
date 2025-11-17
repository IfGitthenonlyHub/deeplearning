import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG1ha2VzcXVhcmUoc2VsZiwgbnVtcyk6CiAgICAgICAgIHMgPSBzdW0obnVtcykKICAgICAgICAgaWYgbm90IHMgJSA0ID09IDA6CiAgICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgICAgICAgbCA9IHMgLy8gNAogICAgICAgICBmcm9tIGNvbGxlY3Rpb25zIGltcG9ydCBDb3VudGVyCiAgICAgICAgIHNlbGYuYyA9IENvdW50ZXIobnVtcykKICAgICAgICAgZm9yIF8gaW4gcmFuZ2UoNCk6CiAgICAgICAgICAgICBuID0gc2VsZi5mKDAsIHNvcnRlZChzZWxmLmMuZWxlbWVudHMoKSxyZXZlcnNlPVRydWUpLCBsLCAoKSkKICAgICAgICAgICAgIGlmIG5vdCBuOgogICAgICAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgICAgICAgc2VsZi5jLnN1YnRyYWN0KG4pCiAgICAgICAgIHJldHVybiBUcnVlCiAKICAgICBkZWYgZihzZWxmLCBpbmRleCwga2V5cywgc3VtLCBudW1zKToKICAgICAgICAgaWYgc3VtID09IDA6CiAgICAgICAgICAgICByZXR1cm4gbnVtcwogICAgICAgICBpZiBzdW0gPCAwIG9yIGluZGV4ID49IGxlbihrZXlzKToKICAgICAgICAgICAgIHJldHVybiBOb25lCiAgICAgICAgIHJldHVybiBzZWxmLmYoaW5kZXggKyAxLCBrZXlzLCBzdW0gLSBrZXlzW2luZGV4XSwgKCpudW1zLCBrZXlzW2luZGV4XSkpIFwKICAgICAgICAgICAgICAgIG9yIHNlbGYuZihpbmRleCArIDEsIGtleXMsIHN1bSwgbnVtcyk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
