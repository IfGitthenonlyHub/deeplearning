import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGxhcmdlc3ROdW1iZXIoc2VsZiwgbnVtcyk6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBudW1zOiBMaXN0W2ludF0KICAgICAgICAgOnJ0eXBlOiBzdHIKICAgICAgICAgIiIiCiAgICAgICAgIGRlZiBsZXhpY19jb21wKGEsIGIpOgogICAgICAgICAgICAgYWIgPSBzdHIoYSkgKyBzdHIoYikKICAgICAgICAgICAgIGJhID0gc3RyKGIpICsgc3RyKGEpCiAgICAgICAgICAgICBpZiBhYiA+IGJhOgogICAgICAgICAgICAgICAgIHJldHVybiAtMQogICAgICAgICAgICAgZWxpZiBiYSA+IGFiOgogICAgICAgICAgICAgICAgIHJldHVybiAxCiAgICAgICAgICAgICByZXR1cm4gMAogICAgICAgICAKICAgICAgICAgaW1wb3J0IGZ1bmN0b29scwogICAgICAgICAKICAgICAgICAgbnVtcy5zb3J0KGtleT1mdW5jdG9vbHMuY21wX3RvX2tleShsZXhpY19jb21wKSkKICAgICAgICAgCiAgICAgICAgIHJldHVybiBzdHIoaW50KCcnLmpvaW4obWFwKHN0ciwgbnVtcykpKSk=").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
