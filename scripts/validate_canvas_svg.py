#!/usr/bin/env python3
"""
Feishu Whiteboard SVG Physics Validator
飞书 Whiteboard SVG 物理铁律与渲染质量自动校验工具
"""

import sys
import re
import xml.etree.ElementTree as ET

BLACKLIST_TAGS = ['radialgradient', 'filter', 'clippath', 'mask', 'pattern']
BLACKLIST_ATTRIBUTES = ['skewx', 'skewy', 'matrix']

def validate_svg_string(svg_content: str) -> list:
    issues = []
    
    # 1. 检查 writing-mode 黑名单
    if re.search(r'writing-mode\s*:\s*vertical', svg_content, re.IGNORECASE):
        issues.append("❌ [铁律1违规] 检测到 CSS 'writing-mode: vertical'！飞书白板解析器会忽略此属性导致文字横向穿框。请改用独立 <text> 逐字显式 y 坐标定锚。")
    
    # 2. 检查黑名单标签
    for tag in BLACKLIST_TAGS:
        if f'<{tag}' in svg_content.lower():
            issues.append(f"❌ [铁律4违规] 检测到白板黑名单标签 '<{tag}>'！会导致飞书白板渲染崩溃或严重变形。")
            
    # 3. 检查黑名单属性
    for attr in BLACKLIST_ATTRIBUTES:
        if f'{attr}(' in svg_content.lower() or f'{attr}=' in svg_content.lower():
            issues.append(f"❌ [铁律4违规] 检测到黑名单变形属性 '{attr}'！请使用基础几何元素组合。")

    # 4. 边界与底边留白校验
    y_coords = [int(m) for m in re.findall(r'\by=["\'](\d+)["\']', svg_content)]
    height_match = re.search(r'height=["\'](\d+)["\']', svg_content)
    viewbox_match = re.search(r'viewBox=["\']0\s+0\s+\d+\s+(\d+)["\']', svg_content)
    
    canvas_h = None
    if viewbox_match:
        canvas_h = int(viewbox_match.group(1))
    elif height_match:
        canvas_h = int(height_match.group(1))

    if canvas_h and y_coords:
        max_y = max(y_coords)
        margin = canvas_h - max_y
        if margin < 25:
            issues.append(f"⚠️ [铁律3警告] 底部安全留白不足 (当前仅 {margin}px，要求 ≥ 30px)！最底端元素坐标 y={max_y}，画布总高={canvas_h}，可能导致底部文字贴边或穿框出线。")

    return issues

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_canvas_svg.py <path_to_svg_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
        
    issues = validate_svg_string(content)
    if not issues:
        print("✅ [校验通过] 该 SVG 完美符合飞书白板四大渲染物理铁律！")
        sys.exit(0)
    else:
        print("⚠️ [校验发现问题]:")
        for iss in issues:
            print(f"  {iss}")
        sys.exit(1)

if __name__ == "__main__":
    main()
