import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGZpbmRMb25nZXN0V29yZChzZWxmLCBzLCBkKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHM6IHN0cgogICAgICAgICA6dHlwZSBkOiBMaXN0W3N0cl0KICAgICAgICAgOnJ0eXBlOiBzdHIKICAgICAgICAgIiIiCiAgICAgICAgIHJlc3VsdCA9ICcnCiAgICAgICAgIGZvciB3b3JkIGluIGQ6CiAgICAgICAgICAgICBsbyA9IDAKICAgICAgICAgICAgIGZvciBsIGluIHdvcmQ6CiAgICAgICAgICAgICAgICAgbG8gPSBzLmZpbmQobCwgbG8pKzEKICAgICAgICAgICAgICAgICBpZiBsbyA9PSAwOgogICAgICAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICAgaWYgbG8gPiAwIGFuZCBsZW4od29yZCkgPj0gbGVuKHJlc3VsdCk6CiAgICAgICAgICAgICAgICAgaWYgbGVuKHdvcmQpID09IGxlbihyZXN1bHQpOgogICAgICAgICAgICAgICAgICAgICByZXN1bHQgPSB3b3JkIGlmIHdvcmQgPCByZXN1bHQgZWxzZSByZXN1bHQKICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICByZXN1bHQgPSB3b3JkCiAgICAgICAgIHJldHVybiByZXN1bHQ=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
