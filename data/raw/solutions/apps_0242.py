import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWF4RXF1YWxGcmVxKHNlbGYsIG51bXM6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIGNudCxmcmVxLG1heEYscmVzID0gY29sbGVjdGlvbnMuZGVmYXVsdGRpY3QoaW50KSwgY29sbGVjdGlvbnMuZGVmYXVsdGRpY3QoaW50KSwwLDAKICAgICAgICBmb3IgaSxudW0gaW4gZW51bWVyYXRlKG51bXMpOgogICAgICAgICAgICBjbnRbbnVtXSArPSAxCiAgICAgICAgICAgIGZyZXFbY250W251bV0tMV0gLT0gMQogICAgICAgICAgICBmcmVxW2NudFtudW1dXSArPSAxCiAgICAgICAgICAgIG1heEYgPSBtYXgobWF4RixjbnRbbnVtXSkKICAgICAgICAgICAgaWYgbWF4RipmcmVxW21heEZdID09IGkgb3IgKG1heEYtMSkqKGZyZXFbbWF4Ri0xXSsxKSA9PSBpIG9yIG1heEYgPT0gMToKICAgICAgICAgICAgICAgIHJlcyA9IGkgKyAxCiAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
