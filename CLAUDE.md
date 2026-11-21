# Platform build guidance

Use platforms/apple-silicon/README.md for native Mac builds and platforms/windows-snapdragon/README.md for Windows x86 builds on ARM. Initialize the pinned ports/GeneralsX submodule and apply platforms/native-lan.patch once to a clean checkout. Check git status before applying it to an existing tree. For LAN peers use the same source revision, patch and game data. Verify retail inputs with platforms/stage_assets.py. Keep original game archives, local credentials, user profiles and machine-specific build caches outside Git and release uploads.

For validation, record executable architecture, SHA-256, and both hosts. Verify lobby discovery on UDP 8086, then sustained bidirectional match traffic on UDP 8088 and advancing replay files. Preserve an active match when cleaning old installations. Resolve symlinks and verify their replacements before retiring their targets.
