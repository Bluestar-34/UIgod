# Style Manager

Style Manager is the single visible skill for selecting and applying bundled UIgod styles.

It keeps concrete style packages inside `styles/` while preserving nested `SKILL.md` files for agent discovery. That gives users one catalog entry point without losing direct style recognition.

## Use

```bash
python skills/style-manager/tools/list_styles.py
```

For a non-interactive default choice:

```bash
python skills/style-manager/tools/list_styles.py --choose
```

For brief-aware selection:

```bash
python skills/style-manager/tools/list_styles.py --choose --prefer "dark technical writing portfolio"
```

## Files

| Path | Purpose |
|---|---|
| `SKILL.md` | Main agent instructions |
| `tools/list_styles.py` | Lists and selects managed styles |
| `preferences.example.json` | User preference schema |
| `styles/` | Managed style packages |

## Visibility Rule

Managed styles keep nested `SKILL.md` files. Use this manager to list and choose them; direct nested recognition remains available for agents.
