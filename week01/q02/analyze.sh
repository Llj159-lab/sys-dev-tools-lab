#!/bin/bash
if [ -z "$1" ]; then
 echo "Error: 请提供CSV文件路径" >&2
 exit 1
fi
if [ ! -f "$1" ]; then
echo "Error: 文件 '$1' 不存在" >&2
    exit 1
fi
echo "=== HTTP 5xx 数量最多的前2个path ==="
awk -F, 'NR>1 && $4 ~ /^5/ {print $3}' "$1" | sort | uniq -c | sort -rn | head -2
echo ""
echo "=== 全部数据行的平均延迟（ms） ==="
awk -F, 'NR>1 {sum += $5; count++} END {printf "%.2f\n", sum/count}' "$1"
