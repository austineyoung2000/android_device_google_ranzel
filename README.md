# Android device tree for Google Pixel 10 family (Ranzel)

Unified LineageOS device repository for:

- `blazer`
- `mustang`
- `frankel`
- `rango` — Pixel 10 Pro Fold

Place this repository at `device/google/ranzel`.

## How the trees were fused

The official LineageOS Muzel tree was used as the multi-device base. Rango was
then added as the fourth product while keeping its foldable-specific hardware
configuration isolated from the Muzel slab devices.

The fusion:

- Registers all eight AOSP and LineageOS product makefiles.
- Rewrites both source-tree paths to `device/google/ranzel`.
- Keeps Muzel's shared configuration at the repository root for Blazer,
  Mustang, and Frankel.
- Keeps Rango's board-info, recovery touch modules, SELinux policy, sysconfig,
  and VINTF files in Rango-specific paths.
- Retains separate `muzel-kernels` and `rango-kernels` dependencies.
- Uses a shared Wi-Fi configuration only because the two upstream files are
  identical.
- Provides root extraction/setup dispatchers for all four devices.

This consolidation does not make the Muzel products inherit Rango's foldable
display, hinge sensor, secondary-display, fingerprint, recovery, or SELinux
configuration.

## Repository dependencies

- `device/google/laguna`
- `device/google/muzel-kernels`
- `device/google/rango-kernels`

## Proprietary file helpers

```bash
./extract-files.py blazer
./extract-files.py mustang
./extract-files.py frankel
./extract-files.py rango

./setup-makefiles.py blazer
./setup-makefiles.py mustang
./setup-makefiles.py frankel
./setup-makefiles.py rango
```

## Source snapshots

- Muzel: `60f3d1ade4062cec3609023357eba8fcccc9e74a`
- Rango: `55805a1451f37dc8589a2eeb041bcac40fbe8b8b`

Both snapshots were taken from the official LineageOS `lineage-24.0`
branches before the fusion.
