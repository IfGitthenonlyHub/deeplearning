import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGludGVnZXJSZXBsYWNlbWVudChzZWxmLCBuKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIG46IGludAogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgZGVmIGRmcyhuKToKICAgICAgICAgICAgIGlmIG49PTE6IHJldHVybiAwCiAgICAgICAgICAgICBpZiBuPT0zOiByZXR1cm4gMgogICAgICAgICAgICAgaWYgKG4gJiAweDEpPT0wOiByZXR1cm4gZGZzKG4+PjEpKzEKICAgICAgICAgICAgIGVsaWYgKChuPj4xKSAmIDB4MSk9PTA6IHJldHVybiBkZnMobi0xKSsxCiAgICAgICAgICAgICBlbHNlOiByZXR1cm4gZGZzKG4rMSkrMQogICAgICAgICAgICAgCiAgICAgICAgIHJldHVybiBkZnMobik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
