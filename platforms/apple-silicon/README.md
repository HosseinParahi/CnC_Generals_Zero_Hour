# Apple Silicon

Use an arm64 macOS terminal with Xcode command-line tools, Git, Homebrew, CMake, Ninja, Meson, pkg-config, Python 3.11+, a bootstrapped vcpkg checkout and the macOS Vulkan SDK installed under ~/VulkanSDK. The engine uses SDL3, SDL_image, DXVK, MoltenVK, GameNetworkingSockets, protobuf, Abseil, FFmpeg and MiniAudio. The preset, vcpkg manifest and deployment script define the full dependency graph. The reference executable also loads Homebrew libraries by ABI-specific paths listed in homebrew-libraries.txt.

From the root of a fresh checkout:

```sh
git submodule update --init --recursive
git -C ports/GeneralsX apply ../../platforms/native-lan.patch
cd ports/GeneralsX
export VCPKG_ROOT="$HOME/vcpkg"
bash scripts/build/macos/build-macos-generals.sh
bash scripts/build/macos/deploy-macos-generals.sh
cd ../..
python3 platforms/stage_assets.py "/path/to/licensed/Generals" "$HOME/GeneralsX/Generals"
cd "$HOME/GeneralsX/Generals"
./run.sh -fullscreen -quickstart -novideo
```

Deployment writes to ~/GeneralsX/Generals. Use an empty staging directory or back up an existing deployment first. The manifest describes the English base-game asset set tested on the two Macs. Supply the original files from your installation and the generated generalsx.big from the port build. For a different language, validate the game data on both peers separately.

The release engine can replace the executable in a staged matching runtime. Compare its SHA-256 against the release notes. A fresh source build is preferable when the linked Homebrew ABI versions are unavailable.

## Launch the Mac release

Extract the release tarball in an empty directory. It contains the matched arm64 executable, its local dynamic libraries, the launcher and the port-generated archive. From the cloned fork, run the asset staging command above with the extracted directory as the second argument. Run ./run.sh there. Use shasum -a 256 GeneralsX to compare the uncompressed binary with the release notes. The tested hosts had Homebrew runtime dependencies installed; inspect homebrew-libraries.txt if dyld reports a missing library.
