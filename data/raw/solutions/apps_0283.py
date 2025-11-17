import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIHNtYWxsZXN0RGlzdGFuY2VQYWlyKHNlbGYsIG51bXMsIGspOgogICAgICAgICAiIiIKICAgICAgICAgOnR5cGUgbnVtczogTGlzdFtpbnRdCiAgICAgICAgIDp0eXBlIGs6IGludAogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgbnVtcy5zb3J0KCkKICAgICAgICAgbCwgciA9IDAsIG51bXNbLTFdIC0gbnVtc1swXQogICAgICAgICAKICAgICAgICAgd2hpbGUgbCA8IHI6CiAgICAgICAgICAgICBtID0gbCArIChyIC0gbCkgLy8gMgogICAgICAgICAgICAgY291bnQgPSAwCiAgICAgICAgICAgICBsZWZ0ID0gMAogICAgICAgICAgICAgZm9yIHJpZ2h0IGluIHJhbmdlKGxlbihudW1zKSk6CiAgICAgICAgICAgICAgICAgd2hpbGUgbnVtc1tyaWdodF0gLSBudW1zW2xlZnRdID4gbTogbGVmdCArPSAxCiAgICAgICAgICAgICAgICAgY291bnQgKz0gKHJpZ2h0IC0gbGVmdCkgICAgICAgIAogICAgICAgICAgICAgaWYgY291bnQgPCBrIDoKICAgICAgICAgICAgICAgICBsID0gbSsxCiAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgIHIgPSBtCiAgICAgICAgIHJldHVybiBs").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
