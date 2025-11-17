import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgbnVtU3F1YXJlZnVsUGVybXMoc2VsZiwgQTogTGlzdFtpbnRdKSAtPiBpbnQ6CiAgICAgICAgYyA9IGNvbGxlY3Rpb25zLkNvdW50ZXIoQSkKICAgICAgICBjYW5kID0ge2k6IHtqIGZvciBqIGluIGMgaWYgaW50KChpICsgaikqKjAuNSkgKiogMiA9PSBpICsgan0gZm9yIGkgaW4gY30KCiAgICAgICAgZGVmIGRmcyh4LCBsZWZ0PWxlbihBKSAtIDEpOgogICAgICAgICAgICBjW3hdIC09IDEKICAgICAgICAgICAgY291bnQgPSBzdW0oZGZzKHksIGxlZnQgLSAxKSBmb3IgeSBpbiBjYW5kW3hdIGlmIGNbeV0pIGlmIGxlZnQgZWxzZSAxCiAgICAgICAgICAgIGNbeF0gKz0gMQogICAgICAgICAgICByZXR1cm4gY291bnQKICAgICAgICByZXR1cm4gc3VtKG1hcChkZnMsIGMpKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
