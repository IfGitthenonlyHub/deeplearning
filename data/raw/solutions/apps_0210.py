import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgIyBAcGFyYW0ge2ludGVnZXJbXX0gbnVtcwogICAgICMgQHBhcmFtIHtpbnRlZ2VyfSBrCiAgICAgIyBAcGFyYW0ge2ludGVnZXJ9IHQKICAgICAjIEByZXR1cm4ge2Jvb2xlYW59CiAgICAgZGVmIGNvbnRhaW5zTmVhcmJ5QWxtb3N0RHVwbGljYXRlKHNlbGYsIG51bXMsIGssIHQpOgogICAgICAgICBpZiBsZW4obnVtcykgPT0gMCBvciBsZW4obnVtcykgPT0gMSBvciBrIDwgMSBvciB0IDwgMDoKICAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgICBkID0gY29sbGVjdGlvbnMuT3JkZXJlZERpY3QoKQogICAgICAgICBmb3IgaSBpbiBudW1zOgogICAgICAgICAgICAga2V5ID0gaSBpZiBub3QgdCBlbHNlIGkgLy8gdAogICAgICAgICAgICAgZm9yIGogaW4gKGQuZ2V0KGtleSAtIDEpLCBkLmdldChrZXkpLCBkLmdldChrZXkgKyAxKSk6CiAgICAgICAgICAgICAgICAgaWYgaiAhPSBOb25lIGFuZCBhYnMoaiAtIGkpIDw9IHQ6CiAgICAgICAgICAgICAgICAgICAgIHJldHVybiBUcnVlCiAgICAgICAgICAgICBpZiBsZW4oZCkgPT0gazoKICAgICAgICAgICAgICAgICBkLnBvcGl0ZW0oRmFsc2UpCiAgICAgICAgICAgICBkW2tleV0gPSBpCiAgICAgICAgICAgICAKICAgICAgICAgcmV0dXJuIEZhbHNl").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
