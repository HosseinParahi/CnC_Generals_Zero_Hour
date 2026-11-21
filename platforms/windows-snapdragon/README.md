# Windows on Snapdragon X

Use Windows 11 on ARM with x86 application emulation. The current port builds a Win32 x86 executable. Install Visual Studio 2022 C++ build tools with the x86 compiler, Windows SDK and ATL, CMake, Ninja, Git, Python 3.11+ and vcpkg. Start a Visual Studio developer shell targeting x86. Set VCPKG_ROOT to the bootstrapped checkout.

```powershell
git submodule update --init --recursive
git -C ports/GeneralsX apply ../../platforms/native-lan.patch
cd ports/GeneralsX
cmake --preset win32-vcpkg
cmake --build --preset win32-vcpkg --target GeneralsX.exe
cd ../..
```

Stage the Release executable, the DLLs from its build output and the generated generalsx.big in a dedicated runtime folder. Use the matching x86 runtime dependencies, including Direct3D 8 support. From the repository root run:

```powershell
py -3.11 platforms/stage_assets.py "C:\Games\Licensed Generals" "C:\Games\GeneralsX"
cd "C:\Games\GeneralsX"
.\GeneralsX.exe -assetPath "$PWD" -fullscreen -quickstart -novideo
```

For LAN verification, join a Mac-hosted lobby and start a map. Record whether both players can issue commands and their replays advance. The observed successful two-Mac match does not establish Windows-to-Mac compatibility.

