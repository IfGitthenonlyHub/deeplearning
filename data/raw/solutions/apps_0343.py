import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIG51bVNxdWFyZXMoc2VsZiwgbik6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBuOiBpbnQKICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGRlZiBpc19zcXVhcmUobik6CiAgICAgICAgICAgICByZXR1cm4gaW50KG4qKjAuNSkgKiBpbnQobioqMC41KSA9PSBuCiAgICAgICAgIAogICAgICAgICBpZiBpc19zcXVhcmUobik6IHJldHVybiAxCiAgICAgICAgIGZvciBpIGluIHJhbmdlKDEsIGludCgobioqMC41KSArIDEpKToKICAgICAgICAgICAgIGlmIGlzX3NxdWFyZShuIC0gaSppKToKICAgICAgICAgICAgICAgICByZXR1cm4gMgogICAgICAgICB3aGlsZSAobiAmIDMpID09IDA6IG4gPj49IDIKICAgICAgICAgaWYgbiAmIDcgPT0gNzogcmV0dXJuIDQKICAgICAgICAgcmV0dXJuIDM=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
