#!/usr/bin/env python
"""
Diagnostic script to find the real import error
Run this to see what's actually wrong with admin_bp import
"""

import sys
import traceback

print("=" * 80)
print("OPENALGO DIAGNOSTIC SCRIPT")
print("=" * 80)
print()

# Test 1: Check Python version
print("[TEST 1] Python version")
print(f"  Python: {sys.version}")
print()

# Test 2: Check if Flask is installed
print("[TEST 2] Flask installation")
try:
    import flask
    print(f"  ✓ Flask {flask.__version__} installed")
except ImportError as e:
    print(f"  ✗ Flask not installed: {e}")
print()

# Test 3: Check if blueprints folder exists
print("[TEST 3] Blueprints folder")
import os
if os.path.exists("blueprints"):
    print("  ✓ blueprints folder exists")
    if os.path.exists("blueprints/admin.py"):
        print("  ✓ blueprints/admin.py exists")
    else:
        print("  ✗ blueprints/admin.py NOT FOUND")
else:
    print("  ✗ blueprints folder NOT FOUND")
print()

# Test 4: Check if database folder exists
print("[TEST 4] Database folder")
if os.path.exists("database"):
    print("  ✓ database folder exists")
    if os.path.exists("database/market_calendar_db.py"):
        print("  ✓ database/market_calendar_db.py exists")
    else:
        print("  ✗ database/market_calendar_db.py NOT FOUND")
    if os.path.exists("database/qty_freeze_db.py"):
        print("  ✓ database/qty_freeze_db.py exists")
    else:
        print("  ✗ database/qty_freeze_db.py NOT FOUND")
else:
    print("  ✗ database folder NOT FOUND")
print()

# Test 5: Check if limiter.py exists
print("[TEST 5] Limiter module")
if os.path.exists("limiter.py"):
    print("  ✓ limiter.py exists")
else:
    print("  ✗ limiter.py NOT FOUND")
print()

# Test 6: Check if utils modules exist
print("[TEST 6] Utils modules")
if os.path.exists("utils/logging.py"):
    print("  ✓ utils/logging.py exists")
else:
    print("  ✗ utils/logging.py NOT FOUND")
if os.path.exists("utils/session.py"):
    print("  ✓ utils/session.py exists")
else:
    print("  ✗ utils/session.py NOT FOUND")
print()

# Test 7: Try to import admin_bp
print("[TEST 7] Import admin_bp")
try:
    from blueprints.admin import admin_bp
    print("  ✓ admin_bp imported successfully!")
except Exception as e:
    print(f"  ✗ Failed to import admin_bp")
    print()
    print("  ERROR DETAILS:")
    print("  " + "=" * 76)
    traceback.print_exc()
    print("  " + "=" * 76)
print()

# Test 8: Try to import app
print("[TEST 8] Import app")
try:
    import app
    print("  ✓ app imported successfully!")
except Exception as e:
    print(f"  ✗ Failed to import app")
    print()
    print("  ERROR DETAILS:")
    print("  " + "=" * 76)
    traceback.print_exc()
    print("  " + "=" * 76)
print()

print("=" * 80)
print("DIAGNOSTIC COMPLETE")
print("=" * 80)
print()
print("NEXT STEPS:")
print("  1. Look at the error messages above")
print("  2. Find the matching solution in REAL_FIX_admin_bp_IMPORT_ERROR.txt")
print("  3. Apply the fix")
print("  4. Run this script again to verify")
print()
