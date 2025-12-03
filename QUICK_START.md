# IDM Manager v3.0 - Quick Start Guide

## Running the Application

### Option 1: Run as Administrator (Recommended)
1. Right-click on `IDM Manager v3.0.py`
2. Select **"Run as administrator"**
3. Click **Yes** on the UAC prompt
4. The app will show: ✓ Running with administrator privileges

### Option 2: Run Normally (Will prompt when needed)
1. Open Command Prompt or PowerShell
2. Navigate to the folder:
   ```bash
   cd "c:\Users\zinzi\Desktop\IDM-Freezer-Activation-Tool"
   ```
3. Run the application:
   ```bash
   python "IDM Manager v3.0.py"
   ```
4. The app will show: ⚠️ Running without administrator privileges
5. You'll be prompted for admin when selecting operations that need it

---

## How the New Admin System Works

### When You Select an Operation (like Activate):

**If NOT running as admin:**
```
⚠️  This operation works best with administrator privileges.
Continue anyway? (yes/no):
```

**Your options:**
- Type **`yes`** - Continue without admin (may fail, but you can try)
- Type **`no`** - Go back to menu (recommended: restart as admin first)

**Then if you continue, network check happens:**
```
🌐 Checking network connectivity...
✓ Network connection OK
```

---

## What Changed in the Fix

### Before (v3.0 initial):
- App would immediately try to restart with admin
- Nothing happened if user cancelled UAC
- App would just close

### After (v3.0 fixed):
- App asks if you want to continue without admin
- You can choose to try anyway
- Better feedback about what's happening
- Doesn't force restart unless you agree

---

## Troubleshooting

### "Nothing happens when I choose activate"
**Solution:** Try these steps:

1. **Close the current app**

2. **Run as administrator from the start:**
   - Right-click `IDM Manager v3.0.py`
   - Select "Run as administrator"
   - Accept the UAC prompt

3. **Now try activate again:**
   - Choose option `[1]` Activate IDM
   - It should proceed directly to the network check

### "Operation may fail" warning
This means you're running without admin. Some operations might not work correctly. It's recommended to:
- Exit the app (option 0)
- Restart as administrator
- Try again

### UAC keeps appearing
If you see multiple UAC prompts:
- The app is trying to elevate privileges
- Click "Yes" to allow
- Or exit and run as admin from the start

---

## Recommended Workflow

### First Time Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run as admin (right-click → Run as administrator)
python "IDM Manager v3.0.py"
```

### For Activation/Freeze (Needs Internet + Admin)
1. Start app as administrator
2. Choose `[2]` Freeze Trial (Recommended)
3. Wait for completion
4. Done!

### For Status Check (No Admin Needed)
1. Run app normally
2. Choose `[4]` Check IDM Status
3. View installation info
4. No admin required!

### For Backup (No Admin Needed)
1. Run app normally
2. Choose `[5]` Backup/Restore
3. Choose `[1]` Backup
4. Settings saved!

---

## Admin Requirements by Operation

| Operation | Needs Admin? | Notes |
|-----------|--------------|-------|
| **[1] Activate IDM** | ✅ Yes | Modifies registry |
| **[2] Freeze Trial** | ✅ Yes | Modifies registry |
| **[3] Reset** | ✅ Yes | Modifies registry |
| **[4] Check Status** | ❌ No | Read-only |
| **[5] Backup/Restore** | ⚠️ Sometimes | Backup=No, Restore=Yes |
| **[6] Download IDM** | ❌ No | Opens browser |
| **[7] GitHub** | ❌ No | Opens browser |
| **[8] Check Updates** | ❌ No | Network only |
| **[9] Settings** | ❌ No | Manages config |

---

## Tips

💡 **Best Practice:** Always run as administrator for activation/freeze/reset operations

💡 **Network Required:** Options 1, 2, and 8 need internet connection

💡 **Check Logs:** If something fails, go to Settings → View Logs to see what happened

💡 **Backup First:** Before major operations, use option 5 to backup your settings

---

## Example Session

```
PS C:\> python "IDM Manager v3.0.py"

======================================================================
=                   IDM FREEZER & ACTIVATION TOOL                    =
=                            Version 3.0                             =
======================================================================

⚠️  Running without administrator privileges.
Some operations may require admin rights. You'll be prompted when needed.

MAIN MENU:
======================================================================
 [1] Activate IDM
 [2] Freeze Trial (Recommended)
 ...
======================================================================

Enter your choice: 2

⚠️  This operation works best with administrator privileges.
Continue anyway? (yes/no): yes

⚠️  Continuing without admin (operation may fail)...

🌐 Checking network connectivity...
✓ Network connection OK

Running command with parameter: /frz
Progress: ██████████████████████████████████████████████████ Done!

[Batch script runs...]

✓ Operation completed successfully!

Press Enter to return to the main menu...
```

---

For more help, check the logs in the `logs/` folder or open the full [walkthrough.md](file:///C:/Users/zinzi/.gemini/antigravity/brain/d213ea97-8681-4108-8ef7-f75f2354d45b/walkthrough.md).
