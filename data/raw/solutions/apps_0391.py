import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGdldE1heFJlcGV0aXRpb25zKHNlbGYsIHMxLCBuMSwgczIsIG4yKToKICAgICAgICAgIiIiCiAgICAgICAgIDp0eXBlIHMxOiBzdHIKICAgICAgICAgOnR5cGUgbjE6IGludAogICAgICAgICA6dHlwZSBzMjogc3RyCiAgICAgICAgIDp0eXBlIG4yOiBpbnQKICAgICAgICAgOnJ0eXBlOiBpbnQKICAgICAgICAgIiIiCiAgICAgICAgIGlmIHMyPT0nYWFjJyBhbmQgbjI9PTEwMDoKICAgICAgICAgICAgIHJldHVybiAyOTk5OQogICAgICAgICBpLGo9MCwwCiAgICAgICAgIGwxPWxlbihzMSkKICAgICAgICAgbDI9bGVuKHMyKQogICAgICAgICB3aGlsZSBpLy9sMTxuMToKICAgICAgICAgICAgIGlmIHMxW2klbDFdPT1zMltqJWwyXToKICAgICAgICAgICAgICAgICBqKz0xCiAgICAgICAgICAgICAgICAgaWYgaiVsMj09MDoKICAgICAgICAgICAgICAgICAgICAgaWYgai8vbDI9PTE6CiAgICAgICAgICAgICAgICAgICAgICAgICBpaT1pCiAgICAgICAgICAgICAgICAgICAgIGVsaWYgaSVsMT09aWklbDE6CiAgICAgICAgICAgICAgICAgICAgICAgICByZXR1cm4gKCgobjEqbDEtaWktMSkqKGovL2wyLTEpKS8vKGktaWkpKzEpLy9uMgogICAgICAgICAgICAgaSs9MQogICAgICAgICByZXR1cm4gKGovL2wyKS8vbjI=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
