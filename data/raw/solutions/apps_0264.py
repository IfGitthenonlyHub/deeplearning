import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4TGVuZ3RoKHNlbGYsIGFycjogTGlzdFtzdHJdKSAtPiBpbnQ6CiAgICAgICAgCiAgICAgICAgZHAgPSBbc2V0KCldCiAgICAgICAgZm9yIGEgaW4gYXJyOgogICAgICAgICAgICBpZiBsZW4oc2V0KGEpKSA8IGxlbihhKTogY29udGludWUKICAgICAgICAgICAgYSA9IHNldChhKQogICAgICAgICAgICBmb3IgYyBpbiBkcFs6XToKICAgICAgICAgICAgICAgIGlmIGEgJiBjOiBjb250aW51ZQogICAgICAgICAgICAgICAgZHAuYXBwZW5kKGEgfCBjKQogICAgICAgIHJldHVybiBtYXgobGVuKGEpIGZvciBhIGluIGRwKQoKICAgICAgICAKICAgICAgICByZXR1cm4gc2VsZi5t").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
