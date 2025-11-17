import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("aW1wb3J0IHN5cwoKZm9yIF8gaW4gcmFuZ2UoaW50KHN5cy5zdGRpbi5yZWFkbGluZSgpKSk6CiAgICBuLCBtID0gbWFwKGludCwgc3lzLnN0ZGluLnJlYWRsaW5lKCkuc3BsaXQoKSkKICAgIHMgPSAobi1tKS8vKG0rMSkKICAgIG5vbmUgPSAobSsxLShuLW0pJShtKzEpKSpzKihzKzEpLy8yICsgKChuLW0pJShtKzEpKSoocysxKSoocysyKS8vMgogICAgcHJpbnQoKG4rMSkqbi8vMiAtIG5vbmUp").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
