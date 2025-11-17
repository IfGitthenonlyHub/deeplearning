import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZGVjb2RlQXRJbmRleChzZWxmLCBTLCBLKToKICAgICAgICBOID0gMAogICAgICAgIGZvciBpLCBjIGluIGVudW1lcmF0ZShTKToKICAgICAgICAgICAgTiA9IE4gKiBpbnQoYykgaWYgYy5pc2RpZ2l0KCkgZWxzZSBOICsgMQogICAgICAgICAgICBpZiBLIDw9IE46IGJyZWFrCiAgICAgICAgZm9yIGogaW4gcmFuZ2UoaSwgLTEsIC0xKToKICAgICAgICAgICAgYyA9IFNbal0KICAgICAgICAgICAgaWYgYy5pc2RpZ2l0KCk6CiAgICAgICAgICAgICAgICBOIC89IGludChjKQogICAgICAgICAgICAgICAgSyAlPSBOCiAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICBpZiBLID09IE4gb3IgSyA9PSAwOiByZXR1cm4gYwogICAgICAgICAgICAgICAgTiAtPSAx").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
