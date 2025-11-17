import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4VW5pcXVlU3BsaXQoc2VsZiwgczogc3RyLCBzZWVuPSAoKSkgLT4gaW50OgogICAgICAgIHJldHVybiBtYXgoKDEgKyBzZWxmLm1heFVuaXF1ZVNwbGl0KHNbaTpdLCB7Y2FuZGlkYXRlLCAqc2Vlbn0pIGZvciBpIGluIHJhbmdlKDEsIGxlbihzKSArIDEpIGlmIChjYW5kaWRhdGUgOj0gc1s6aV0pIG5vdCBpbiBzZWVuKSwgZGVmYXVsdD0wKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
