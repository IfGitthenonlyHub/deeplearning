import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluRmxpcHMoc2VsZiwgYTogaW50LCBiOiBpbnQsIGM6IGludCkgLT4gaW50OgogICAgICAgIGZsaXBzID0gMAogICAgICAgIHdoaWxlIGEgb3IgYiBvciBjOgogICAgICAgICAgICBpZiBjICYgMSA9PSAwOgogICAgICAgICAgICAgICAgaWYgYSAmIDE6CiAgICAgICAgICAgICAgICAgICAgZmxpcHMgKz0gMQogICAgICAgICAgICAgICAgaWYgYiAmIDE6CiAgICAgICAgICAgICAgICAgICAgZmxpcHMgKz0gMQogICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgaWYgKGEgJiAxKSA9PSAwIGFuZCAoYiAmIDEpID09IDA6CiAgICAgICAgICAgICAgICAgICAgZmxpcHMgKz0gMQogICAgICAgICAgICBhID4+PSAxCiAgICAgICAgICAgIGIgPj49IDEKICAgICAgICAgICAgYyA+Pj0gMQogICAgICAgIHJldHVybiBmbGlwcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
