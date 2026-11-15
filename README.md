# Google Pixel 10 family device tree (Ranzel)

A unified LineageOS 24.0 repository for Pixel 10 Pro (`blazer`), Pixel 10 Pro XL (`mustang`), Pixel 10 (`frankel`), and Pixel 10 Pro Fold (`rango`). Check it out at `device/google/ranzel` and build the individual upstream product names, such as `lineage_rango` or `lineage_blazer`. Ranzel is the repository name, not a new device or product.

## Fusion design

The LineageOS Muzel tree is the base at the repository root for the three slab devices. The LineageOS Rango tree is retained under `fold/`, with its own Soong namespace, board configuration, recovery, overlays, SELinux policy, VINTF, and extraction files. The top-level `AndroidProducts.mk` registers all eight AOSP and Lineage products. Paths in both trees point to their new locations; upstream vendor paths and device-specific product identities remain unchanged. Kernel dependencies remain separate. This layout keeps the foldable configuration isolated rather than applying it to the slab devices.

Upstream source commits used:

- [Muzel](https://github.com/LineageOS/android_device_google_muzel/tree/60f3d1ade4062cec3609023357eba8fcccc9e74a): `60f3d1ade4062cec3609023357eba8fcccc9e74a`
- [Rango](https://github.com/LineageOS/android_device_google_rango/tree/55805a1451f37dc8589a2eeb041bcac40fbe8b8b): `55805a1451f37dc8589a2eeb041bcac40fbe8b8b`

Both snapshots came from `lineage-24.0`. Future upstream changes must be ported to the corresponding area of this tree.

## Dependencies and proprietary files

The Lineage dependency list includes `device/google/laguna`, `device/google/muzel-kernels`, and `device/google/rango-kernels`. The appropriate device-specific proprietary vendor tree and other dependencies of Laguna are also required. Follow LineageOS extraction requirements for the matching factory image and firmware.

From this directory, dispatch to the upstream extractor or regenerate makefiles for a device:

```sh
./extract-files.py blazer [upstream options]
./extract-files.py mustang [upstream options]
./extract-files.py frankel [upstream options]
./extract-files.py rango [upstream options]
./setup-makefiles.py rango [upstream options]
```

The extracted vendor files remain under `vendor/google/<device>`. A source build and device testing are needed to establish that each product works; repository-level checks alone cannot establish boot or hardware support.
