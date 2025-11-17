import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGRpdmlkZShzZWxmLCBkaXZpZGVuZCwgZGl2aXNvcik6CiAgICAgICAgIHBvc2l0aXZlID0gKGRpdmlkZW5kIDwgMCkgaXMgKGRpdmlzb3IgPCAwKQogICAgICAgICBkaXZpZGVuZCwgZGl2aXNvciA9IGFicyhkaXZpZGVuZCksIGFicyhkaXZpc29yKQogICAgICAgICByZXMgPSAwCiAgICAgICAgIHdoaWxlIGRpdmlkZW5kID49IGRpdmlzb3I6CiAgICAgICAgICAgICB0ZW1wLCBpID0gZGl2aXNvciwgMQogICAgICAgICAgICAgd2hpbGUgZGl2aWRlbmQgPj0gdGVtcDoKICAgICAgICAgICAgICAgICBkaXZpZGVuZCAtPSB0ZW1wCiAgICAgICAgICAgICAgICAgcmVzICs9IGkKICAgICAgICAgICAgICAgICBpIDw8PSAxCiAgICAgICAgICAgICAgICAgdGVtcCA8PD0gMQogICAgICAgICBpZiBub3QgcG9zaXRpdmU6CiAgICAgICAgICAgICByZXMgPSAtcmVzCiAgICAgICAgIHJldHVybiBtaW4obWF4KC0yMTQ3NDgzNjQ4LCByZXMpLCAyMTQ3NDgzNjQ3KQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
