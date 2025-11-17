import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtQnVzZXNUb0Rlc3RpbmF0aW9uKHNlbGYsIHJvdXRlcywgUywgVCk6CiAgICAgICAgaWYgUyA9PSBUOiByZXR1cm4gMAogICAgICAgIHRvX3JvdXRlcyA9IGNvbGxlY3Rpb25zLmRlZmF1bHRkaWN0KHNldCkKICAgICAgICBmb3IgaSwgcm91dGUgaW4gZW51bWVyYXRlKHJvdXRlcyk6CiAgICAgICAgICAgIGZvciBqIGluIHJvdXRlOgogICAgICAgICAgICAgICAgdG9fcm91dGVzW2pdLmFkZChpKQogICAgICAgIGJmcyA9IFsoUywgMCldCiAgICAgICAgc2VlbiA9IHNldChbU10pCiAgICAgICAgZm9yIHN0b3AsYnVzIGluIGJmczoKICAgICAgICAgICAgaWYgc3RvcCA9PSBUOgogICAgICAgICAgICAgICAgcmV0dXJuIGJ1cwogICAgICAgICAgICBmb3IgaSBpbiB0b19yb3V0ZXNbc3RvcF06CiAgICAgICAgICAgICAgICBmb3IgaiBpbiByb3V0ZXNbaV06CiAgICAgICAgICAgICAgICAgICAgaWYgaiBub3QgaW4gc2VlbjoKICAgICAgICAgICAgICAgICAgICAgICAgc2Vlbi5hZGQoaikKICAgICAgICAgICAgICAgICAgICAgICAgYmZzLmFwcGVuZCgoaixidXMrMSkpCiAgICAgICAgcmV0dXJuIC0x").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
