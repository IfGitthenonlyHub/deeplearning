import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("IyBjb29rIHlvdXIgZGlzaCBoZXJlCmZvciB0IGluIHJhbmdlKGludChpbnB1dCgpKSk6CiAgICBuLGs9bWFwKGludCxpbnB1dCgpLnNwbGl0KCkpCiAgICBhPVtdCiAgICBzcj1bXQogICAgZm9yIGkgaW4gcmFuZ2Uoayk6CiAgICAgICAgeCx5PWlucHV0KCkuc3BsaXQoKQogICAgICAgIHk9aW50KHkpCiAgICAgICAgYS5hcHBlbmQoWzEwKioxMC15LHhdKQogICAgICAgIHNyLmFwcGVuZChzb3J0ZWQoeCkpCiAgICBmb3IgaSBpbiByYW5nZShuLWspOgogICAgICAgIHgseT1pbnB1dCgpLnNwbGl0KCkKICAgICAgICB5PWludCh5KQogICAgICAgIHg9c29ydGVkKHgpCiAgICAgICAgZm9yIGogaW4gcmFuZ2Uoayk6CiAgICAgICAgICAgIGlmIHg9PXNyW2pdOgogICAgICAgICAgICAgICAgYVtqXVswXS09eQogICAgICAgICAgICAgICAgYnJlYWsKICAgIGEuc29ydCgpCiAgICBmb3IgaSBpbiBhOgogICAgICAgIHByaW50KGlbMV0sYWJzKGlbMF0tMTAqKjEwKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
