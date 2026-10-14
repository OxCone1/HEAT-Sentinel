#!/usr/bin/env python3
"""Rewrite the RELEASE-EN / RELEASE-RU marker blocks in README.md.

Input JSON (produced by .github/workflows/release-readme.yml):
{
  "tag": "v2.0.0",
  "release_url": "https://github.com/OxCone1/HEAT-Sentinel/releases/tag/v2.0.0",
  "date": "2026-07-15",
  "assets": [
    {"kind": "installer", "name": "HEAT.Sentinel_2.0.0_x64-setup.exe",
     "sha256": "...", "size": 12345678, "download_url": "https://..."},
    {"kind": "heat-capture", "name": "heat-capture.exe",
     "sha256": "...", "size": 12345678, "download_url": null},
    {"kind": "labelme", "name": "labelme.exe",
     "sha256": "...", "size": 12345678, "download_url": "https://..."}
  ]
}

"kind" is optional; when missing it is inferred from the file name.
Assets without a download_url are listed as bundled (no link).
"""

import argparse
import json
import re
import sys

VT_FILE_URL = "https://www.virustotal.com/gui/file/{sha256}"

MARKERS = {
    "en": ("<!-- RELEASE-EN:START -->", "<!-- RELEASE-EN:END -->"),
    "ru": ("<!-- RELEASE-RU:START -->", "<!-- RELEASE-RU:END -->"),
}

NOTES_MARKERS = ("<!-- DOWNLOAD:START -->", "<!-- DOWNLOAD:END -->")

TEXT = {
    "en": {
        "badge_label": "Download",
        "latest": "**Latest release:**",
        "published": "published",
        "file": "File",
        "size": "Size",
        "vt": "VirusTotal report",
        "view": "View scan",
        "installer": "app installer",
        "capture": "capture/watcher engine, bundled inside the installer",
        "labelme": "calibration annotation tool",
        "asset": "release asset",
    },
    "ru": {
        "badge_label": "Скачать",
        "latest": "**Последний релиз:**",
        "published": "опубликован",
        "file": "Файл",
        "size": "Размер",
        "vt": "Отчёт VirusTotal",
        "view": "Открыть отчёт",
        "installer": "установщик приложения",
        "capture": "движок захвата, встроен в установщик",
        "labelme": "инструмент разметки калибровок",
        "asset": "файл релиза",
    },
}


def shields_escape(text: str) -> str:
    """Escape a shields.io path segment: - -> --, _ -> __, space -> %20."""
    out = text.replace("-", "--").replace("_", "__").replace(" ", "%20")
    return "".join(c if ord(c) < 128 else "".join(f"%{b:02X}" for b in c.encode("utf-8")) for c in out)


def human_size(size: int) -> str:
    return f"{size / (1024 * 1024):.1f} MB"


KIND_KEYS = {"installer": "installer", "heat-capture": "capture", "labelme": "labelme"}


def asset_kind(asset: dict, lang: str) -> str:
    kind = asset.get("kind")
    if kind in KIND_KEYS:
        return TEXT[lang][KIND_KEYS[kind]]
    lower = asset["name"].lower()
    if lower.endswith("-setup.exe"):
        return TEXT[lang]["installer"]
    if lower.startswith("heat-capture"):
        return TEXT[lang]["capture"]
    if lower.startswith("labelme"):
        return TEXT[lang]["labelme"]
    return TEXT[lang]["asset"]


def build_badge(data: dict, lang: str) -> str:
    t = TEXT[lang]
    version = data["tag"].lstrip("vV")

    installer = next(
        (
            a
            for a in data["assets"]
            if a.get("kind") == "installer"
            or a["name"].lower().endswith("-setup.exe")
        ),
        None,
    )
    if installer is None or not installer.get("download_url"):
        sys.exit("No installer asset with a download URL found in release data.")

    return (
        f"[![{t['badge_label']} HEAT Sentinel]"
        f"(https://img.shields.io/badge/"
        f"{shields_escape(t['badge_label'])}-"
        f"{shields_escape(f'HEAT Sentinel v{version}')}-0a0a0a"
        f"?style=for-the-badge&logo=github)]({installer['download_url']})"
    )


def build_block(data: dict, lang: str) -> str:
    t = TEXT[lang]
    tag = data["tag"]
    badge = build_badge(data, lang)

    lines = [
        badge,
        "",
        f"{t['latest']} [{tag}]({data['release_url']}) -- {t['published']} {data['date']}",
        "",
        f"| {t['file']} | {t['size']} | {t['vt']} |",
        "|------|------|------|",
    ]
    for asset in data["assets"]:
        kind = asset_kind(asset, lang)
        if asset.get("download_url"):
            name_cell = f"[`{asset['name']}`]({asset['download_url']})"
        else:
            name_cell = f"`{asset['name']}`"
        vt_link = f"[{t['view']}]({VT_FILE_URL.format(sha256=asset['sha256'])})"
        lines.append(
            f"| {name_cell} ({kind}) | {human_size(asset['size'])} | {vt_link} |"
        )
    return "\n".join(lines)


def replace_block(readme: str, lang: str, block: str) -> str:
    start, end = MARKERS[lang]
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(readme):
        sys.exit(f"Markers {start} / {end} not found in README.")
    return pattern.sub(f"{start}\n{block}\n{end}", readme)


def update_notes(notes: str, badge: str) -> str:
    """Put the download badge at the top of the release notes (idempotent)."""
    start, end = NOTES_MARKERS
    notes = re.sub(
        re.escape(start) + r".*?" + re.escape(end) + r"\s*", "", notes, flags=re.DOTALL
    )
    return f"{start}\n{badge}\n{end}\n\n{notes.lstrip()}".rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readme", required=True)
    parser.add_argument("--data", required=True)
    parser.add_argument(
        "--notes",
        help="Release notes markdown file to update in place with the download badge.",
    )
    args = parser.parse_args()

    with open(args.data, encoding="utf-8") as f:
        data = json.load(f)
    with open(args.readme, encoding="utf-8") as f:
        readme = f.read()

    for lang in ("en", "ru"):
        readme = replace_block(readme, lang, build_block(data, lang))

    with open(args.readme, "w", encoding="utf-8", newline="\n") as f:
        f.write(readme)
    print("README updated.")

    if args.notes:
        with open(args.notes, encoding="utf-8") as f:
            notes = f.read()
        notes = update_notes(notes, build_badge(data, "en"))
        with open(args.notes, "w", encoding="utf-8", newline="\n") as f:
            f.write(notes)
        print("Release notes updated.")


if __name__ == "__main__":
    main()
