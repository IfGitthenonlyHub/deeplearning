import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("ZnJvbSBtYXRoIGltcG9ydCBjb21iCgoKY2xhc3MgU29sdXRpb246CiAgICBkZWYgZ2V0UHJvYmFiaWxpdHkoc2VsZiwgYmFsbHM6IExpc3RbaW50XSkgLT4gZmxvYXQ6CiAgICAgICAgbiA9IGxlbihiYWxscykKICAgICAgICBzID0gc3VtKGJhbGxzKQogICAgICAgIHMyID0gcyAvLyAyCgogICAgICAgIEBscnVfY2FjaGUoTm9uZSkKICAgICAgICBkZWYgY291bnQoaW5kZXgsIGRlbHRhLCBjYSk6CiAgICAgICAgICAgIGlmIGluZGV4ID09IG46IHJldHVybiAxIGlmIGRlbHRhID09IDAgYW5kIGNhID09IHMyIGVsc2UgMAogICAgICAgICAgICB0b3RhbCA9IHN1bShbY291bnQoaW5kZXggKyAxLCBkZWx0YSwgY2EgKyB4KSAqIGNvbWIoYmFsbHNbaW5kZXhdLCB4KSBmb3IgeCBpbiByYW5nZSgxLCBiYWxsc1tpbmRleF0pXSkKICAgICAgICAgICAgdG90YWwgKz0gY291bnQoaW5kZXggKyAxLCBkZWx0YSArIDEsIGNhKQogICAgICAgICAgICB0b3RhbCArPSBjb3VudChpbmRleCArIDEsIGRlbHRhIC0gMSwgY2EgKyBiYWxsc1tpbmRleF0pCiAgICAgICAgICAgIHJldHVybiB0b3RhbAoKICAgICAgICByZXR1cm4gY291bnQoMCwgMCwgMCkgLyBjb21iKHMsIHMgLy8gMik=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
