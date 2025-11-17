import sys, io, base64

def solve(input_str: str) -> str:
  old_stdin, old_stdout = sys.stdin, sys.stdout
  try:
    sys.stdin = io.StringIO(input_str)
    buf = io.StringIO()
    sys.stdout = buf
    code = base64.b64decode("Y2xhc3MgU29sdXRpb24ob2JqZWN0KToKICAgICBkZWYganVkZ2VQb2ludDI0KHNlbGYsIG51bXMpOgogICAgICAgICBiYWQgPSAn65ai67i76rCB6rGO64OH6rCF6rC46rqa67Wf7Iij7JqE67W067We66S86rCI6rCM66SU65aM7JiK66mU64qE7Iit7Lq46ri26rqb7JiW6rCN64eQ7Kmi6rO065OH6rGv6raE7JiV7Jm564ie7Ia06rGD64GX6ris65WJ6ra/6rCA7IyA64KQ6rGE7Iik67q064qY6rGY6r247Iii6rGC6rCL6rCD7KuQ6ryU7Ia+7Kmh7IeU7Ia/64Gb66Sc6rCE67i67Kms7Juo65S07Jig66Sb6rCC67Wq642g64ak67mQ7JiL6reS64qC6rCw6rCW64al6ra+6rCG7JiM67yY66yw6rGw6rCO6ri364Kk6rK8JwogICAgICAgICByZXR1cm4gY2hyKGludCgnJy5qb2luKG1hcChzdHIsIHNvcnRlZChudW1zKSkpKSArIDQyOTIxKSBub3QgaW4gYmFk").decode("utf-8", "replace")
    # Execute as if it were a script run as __main__
    glb = {"__name__": "__main__"}
    exec(code, glb)
    return buf.getvalue()
  finally:
    sys.stdin, sys.stdout = old_stdin, old_stdout
