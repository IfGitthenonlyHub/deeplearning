import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICBkZWYgZ2V0TGVuZ3RoT2ZPcHRpbWFsQ29tcHJlc3Npb24oc2VsZiwgczogc3RyLCBrOiBpbnQpIC0+IGludDoKICAgICAgICBAbHJ1X2NhY2hlKE5vbmUpCiAgICAgICAgZGVmIGdldChpbmRleCwgbGVmdCwgYywgc3RyZWFrKToKICAgICAgICAgICAgdmFsID0gKCgxICsgbGVuKHN0cihzdHJlYWspKSkgLSAoc3RyZWFrID09IDEpKSAqIChzdHJlYWsgPiAwKQogICAgICAgICAgICBpZiBsZWZ0IDwgMCBvciBpbmRleCA9PSBsZW4ocyk6IHJldHVybiAxZTYgaWYgbGVmdCA8IDAgZWxzZSB2YWwKICAgICAgICAgICAgcmV0dXJuIG1pbih2YWwqKGMhPXNbaW5kZXhdKStnZXQoaW5kZXgrMSxsZWZ0LHNbaW5kZXhdLDErc3RyZWFrKihjPT1zW2luZGV4XSkpLGdldChpbmRleCsxLGxlZnQtMSxjLHN0cmVhaykpCiAgICAgICAgcmV0dXJuIGdldCgwLCBrLCBOb25lLCAwKQ==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
