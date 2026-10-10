# 维护与贡献

规则见 [仓库规则](docs/LIBRARY-RULES.md)，文件交付约定见 [作品合同](skills/uigod/docs/WORK-CONTRACT.md)。

## 新增与整理

1. 查来源地址和稳定 ID 是否已有记录；相同来源更新原记录，不按提示词内容去重。
2. 外部清单使用 import_opus_videos.py 导入，保留作者、原帖、版本、许可与原始提示词。没有真实效果证据时不声称已验证。
3. 新风格包放 skills/style-manager/styles/<id>/，按作品合同准备真实封面与可用预览，再运行 register_new。人工标题、中文简介、分类和可用性改 editorial.json，修改时更新 updated_at。新增视觉标签先改 taxonomy.json。
4. 原始提示词不改写；可复用制作提示词放正式风格包 DESIGN.md 的 Prompt Guide。不同用途保留明确标记。
5. 将条目加入公开精选必须由维护者明确挑选，只改 curation.json 的 featured_ids，并按数组顺序排列。网页收藏不算公开精选请求。

```sh
python -c "import sys; sys.path.insert(0,'skills/uigod/tools'); from library_data import register_new; register_new()"
python skills/uigod/tools/build_catalog.py
python skills/uigod/tools/build_gallery.py
python skills/uigod/tools/validate_library.py
python -m unittest discover -s skills/uigod/tests
git diff --check
```

## 同步上游

```sh
python skills/uigod/tools/import_opus_videos.py
```

也可传本地上游 Git checkout 路径。导入保留人工字段与首次时间；仅来源实际变化的记录更新 updated_at。发现上游少了记录时停止，维护者确认归档办法后再处理，不静默删记录。

外部参考升级为风格包时填写 related_style_id。隐藏重复或无效卡片需 hidden_reason，并更新 docs/MAINTENANCE-LOG.md；保留原始来源记录。链接暂时不可访问时不自动删除，也不自动认定失效。

## 本地安装与制作偏好

复制 sync.example.json 为 sync.local.json，填写绝对同步目标路径，再运行 python skills/uigod/tools/sync_library.py。个人制作偏好复制 preferences.example.json 为 preferences.local.json 后调整；工具会把个人偏好同步到本机安装副本，但不提交到公开 Git。

提交说明包括问题、最终行为、验证结果；不提交缓存、依赖目录、账号配置、中间成片或本机 local 配置。CI 会重建目录和页面，检查生成结果是否过期。
