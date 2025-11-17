import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb246CiAgICAgZGVmIGdldE1heChzZWxmLCBhcnIsIG0sIG4pOgogICAgICAgICByZXMgPSAwCiAKICAgICAgICAgZm9yIGUgaW4gYXJyOgogICAgICAgICAgICAgaWYgbSA+PSBlWzBdIGFuZCBuID49IGVbMV06CiAgICAgICAgICAgICAgICAgcmVzICs9IDEKICAgICAgICAgICAgICAgICBtIC09IGVbMF0KICAgICAgICAgICAgICAgICBuIC09IGVbMV0KIAogICAgICAgICByZXR1cm4gcmVzCiAKICAgICBkZWYgZmluZE1heEZvcm0oc2VsZiwgc3RycywgbSwgbik6CiAgICAgICAgICIiIgogICAgICAgICA6dHlwZSBzdHJzOiBMaXN0W3N0cl0KICAgICAgICAgOnR5cGUgbTogaW50CiAgICAgICAgIDp0eXBlIG46IGludAogICAgICAgICA6cnR5cGU6IGludAogICAgICAgICAiIiIKICAgICAgICAgYXJyID0gWyhzLmNvdW50KCcwJyksIHMuY291bnQoJzEnKSkgZm9yIHMgaW4gc3Ryc10KICAgICAgICAgYXJyMSA9IHNvcnRlZChhcnIsIGtleT1sYW1iZGEgczogLW1pbihtIC0gc1swXSwgbiAtIHNbMV0pKQogICAgICAgICBhcnIyID0gc29ydGVkKGFyciwga2V5PWxhbWJkYSBzOiBtaW4oc1swXSwgc1sxXSkpCiAgICAgICAgIHJlcyA9IG1heChzZWxmLmdldE1heChhcnIxLCBtLCBuKSwgc2VsZi5nZXRNYXgoYXJyMiwgbSwgbikpCiAKICAgICAgICAgcmV0dXJuIHJlcw==").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
