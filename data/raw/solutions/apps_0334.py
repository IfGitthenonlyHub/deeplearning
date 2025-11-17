import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbWluQ29zdChzZWxmLCBzOiBzdHIsIGNvc3Q6IExpc3RbaW50XSkgLT4gaW50OgogICAgICAgIHRvdGFsPTAKICAgICAgICBmb3IgaSBpbiByYW5nZSgxLGxlbihzKSk6CiAgICAgICAgICAgIGlmIHNbaS0xXT09c1tpXToKICAgICAgICAgICAgICAgIHRvdGFsKz1taW4oY29zdFtpLTFdLGNvc3RbaV0pCiAgICAgICAgICAgICAgICBjb3N0W2ldID0gbWF4KGNvc3RbaS0xXSxjb3N0W2ldKQogICAgICAgIHJldHVybiB0b3RhbA==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
