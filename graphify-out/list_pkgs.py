"""Check all installed packages in the graphifyy environment"""
import pkg_resources
pkgs = sorted([p.project_name for p in pkg_resources.working_set])
for p in pkgs:
    print(p)
