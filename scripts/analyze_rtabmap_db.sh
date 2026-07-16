#!/bin/bash
set -e

DB="$1"

if [ -z "$DB" ]; then
  echo "Usage: bash scripts/analyze_rtabmap_db.sh /path/to/rtabmap.db"
  exit 1
fi

echo "DB: $DB"
ls -lh "$DB"

echo ""
echo "Integrity:"
sqlite3 "$DB" "PRAGMA integrity_check;"

echo ""
echo "Node count:"
sqlite3 "$DB" "SELECT COUNT(*) FROM Node;"

echo ""
echo "Link types:"
sqlite3 "$DB" "SELECT type, COUNT(*) FROM Link GROUP BY type ORDER BY type;"

echo ""
echo "Data count:"
sqlite3 "$DB" "SELECT COUNT(*) FROM Data;"

echo ""
echo "First and last node IDs:"
sqlite3 "$DB" "SELECT MIN(id), MAX(id) FROM Node;"
