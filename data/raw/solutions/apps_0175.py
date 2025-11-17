import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRJbnRlZ2VycyhzZWxmLCBudW0pOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgbnVtOiBpbnQKICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGRlZiBmdW5jKG51bSk6CiAgICAgICAgICAgICBpZiBudW08MzoKICAgICAgICAgICAgICAgICByZXR1cm4gbnVtKzEKICAgICAgICAgICAgIHQsaz1udW0sLTEKICAgICAgICAgICAgIHdoaWxlIHQ6CiAgICAgICAgICAgICAgICAgdD4+PTEKICAgICAgICAgICAgICAgICBrKz0xCiAgICAgICAgICAgICBpZiAobnVtPj4oay0xKSleMz09MDoKICAgICAgICAgICAgICAgICByZXR1cm4gYVtrLTFdK2Fba10KICAgICAgICAgICAgIHJldHVybiBhW2tdK2Z1bmMobnVtLSgxPDxrKSkKICAgICAgICAgCiAgICAgICAgIHQsayxhPW51bSwtMSxbMSwyXQogICAgICAgICB3aGlsZSB0OgogICAgICAgICAgICAgdD4+PTEKICAgICAgICAgICAgIGsrPTEKICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMSxrKToKICAgICAgICAgICAgIGEuYXBwZW5kKGFbLTFdK2FbLTJdKQogICAgICAgICByZXR1cm4gZnVuYyhudW0p").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
