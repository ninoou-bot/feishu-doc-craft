# 飞书云文档与白板全流程制作技能 (Feishu Doc & Canvas Craft)

<p align="center">
  <b>面向 AI Agent 的工业级飞书云文档 (DocX) 与白板 (Whiteboard/Canvas) 全流程策划、排版与生成技能</b>
</p>

---

## 🌟 技能亮点 (Highlights)

- 🎨 **35 套精选调色板设计系统**：完整集成  的 35 套高质感风格库（含 Papier Bleu、Grove、Macchiato、Avocado Press 等），支持指定 Vibe 一键切换配色。
- 📐 **三大战略 Canvas 架构**：内置「本品全周期排期总图 (Roadmap)」、「竞品攻防雷达图 (Competitor Radar)」、「课题诊断与对策推导矩阵 (Strategy Matrix)」三大高质感白板模板。
- 📊 **五大高阶数据表格**：涵盖场景痛点对决表、预算与媒介拆解表、VOC口碑对比表、进度推移表、客群归因表。
- 🍰 **7 大槽位战役级施策卡片**：从战略逻辑、传播动作、话题矩阵、客群切角到量化资源与 KPI 的完整落地表达。
- 🛡️ **四大 SVG 物理渲染铁律与 5 步自检 SOP**：解决飞书白板解析器（`svg-parser`）引起的文字穿框、重叠、出线问题，实现 100% 像素级对齐。
- ⚡ **基于 OpenCLI 的安全增量更新**：遵循“改前必 fetch，绝不整篇 overwrite”的外科手术式更新工作流。

---

## 📂 仓库目录结构

```
feishu-doc-craft/
├── SKILL.md                          # 核心技能规范与完整 SOP（Agent 识别入口）
├── README.md                         # 项目使用与安装说明
├── LICENSE                           # MIT 开源协议
├── examples/                         # 标准 XML 范式与模板库
│   ├── master_roadmap_template.xml   # 本品全周期营销排期总图 (带 SVG Canvas)
│   ├── competitor_radar_template.xml # 竞品攻防与动作雷达全景看板 (带 SVG Canvas)
│   ├── strategy_matrix_template.xml  # 课题诊断与对策推导矩阵画布
│   ├── universal_tables.xml          # 五大高阶数据表格 XML 范式
│   └── tactical_action_card.xml      # 7 大槽位战役施策卡片模板
└── scripts/
    └── validate_canvas_svg.py        # 飞书 Whiteboard SVG 物理铁律自动校验脚本
```

---

## 🚀 安装与使用指南 (Installation)

### 1. 在 Google Antigravity / Gemini CLI 中安装
将本仓库克隆至你的全局技能目录或项目专用技能目录：

```bash
# 全局安装 (所有项目均可调用)
git clone https://github.com/ninoou-bot/feishu-doc-craft.git ~/.gemini/config/skills/feishu-doc-craft

# 或单项目安装 (仅当前 Agent 项目调用)
git clone https://github.com/ninoou-bot/feishu-doc-craft.git .agents/skills/feishu-doc-craft
```

### 2. 在 Claude Code / GitHub Copilot CLI / Amp 中安装
将本仓库克隆并放置在对应工具的技能目录中（如 `.claude/skills/` 或 `.agents/skills/`），Agent 会自动读取 `SKILL.md` 的 YAML frontmatter 并按需触发。

---

## 🛠️ 核心画布模式与适用场景 (Canvas Patterns)

### 1. 本品全周期整合营销排期总图 (Master Roadmap Canvas)
- **适用场景**：新车上市全案、年度品牌/车系 IMC 传播规划、多部门跨周期大排期对齐。
- **视觉特征**：顶部战略定调 + 5-12月产品节奏标尺 + 中部三大推进阶段大框 + 底部多轨纵向执行泳道（大事件线 / 圈层背书线 / 用户共创线 / 日常基盘线）。

### 2. 竞品攻防与动作雷达全景看板 (Competitor Campaign Radar Canvas)
- **适用场景**：单一竞品战役解构、竞品阶段性攻防监测、公关攻防战役复盘。
- **视觉特征**：左侧竖向导引胶囊 + 顶部车系定位与主时间轴 + 中部跨周期话题大框群 + 底部三阶段分色时序动作卡片。

### 3. 课题诊断与对策推导矩阵画布 (Diagnosis-to-Strategy Matrix Canvas)
- **适用场景**：策略提案前期逻辑推导、向上汇报策略定锚。
- **视觉特征**：4 栏水平递进推导卡片流（`[课题诊断] ➔ [突破策略] ➔ [落地施策] ➔ [预期成效]`）。

---

## 📋 飞书 Whiteboard SVG 四大物理铁律速查

1. **竖排文字单字绝对定锚律**：飞书白板解析器会忽略 CSS `writing-mode: vertical-rl`。所有竖排文字必须拆解为独立的 `<text x="..." y="...">` 标签逐字定位。
2. **分栏绝对物理隔离律**：左右多栏布局必须留足 `≥ 40px` 的绝对隔离空隙，文本总宽按 `字符数 × 14px` 验算。
3. **垂直吸附紧凑与底部安全留白律**：时间轴基线吸附在卡片下方 `20-25px`；外层大框高度必须保证 `Outer_Height - Max_Y ≥ 30px`，杜绝穿框出线。
4. **SVG 特性白名单**：严禁 `<radialGradient>`, `<filter>`, `<clipPath>`, `skew`，推荐使用 `<rect>`, `<circle>`, `<line>`, `<polygon>`, `<text>`。

---

## 📄 开源协议 (License)

本项目采用 [MIT License](LICENSE) 开源协议。欢迎提交 PR 与 Issue 共同完善！
