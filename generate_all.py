import json
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

SPECS_DIR = Path("openapi_specs")
PACKAGE_DIR = Path("src/osdu_python_client/generated")
SPEC_EXTENSIONS = {".json", ".yaml", ".yml"}


class _NoTimestampLoader(yaml.SafeLoader):
    """SafeLoader that leaves ISO date/datetime values as strings.

    OpenAPI ``example`` fields like ``2021-01-26T02:24:13.843Z`` would
    otherwise become ``datetime`` objects, which then break JSON serialization
    when we hand the spec off to the generator.
    """


_NoTimestampLoader.yaml_implicit_resolvers = {
    k: [(tag, regexp) for tag, regexp in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def _load_spec(spec_path: Path) -> dict:
    text = spec_path.read_text(encoding="utf-8")
    if spec_path.suffix.lower() in {".yaml", ".yml"}:
        return yaml.load(text, Loader=_NoTimestampLoader)
    return json.loads(text)


def generate_all():
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    (PACKAGE_DIR / "__init__.py").touch(exist_ok=True)

    specs = sorted(
        p for p in SPECS_DIR.iterdir()
        if p.is_file() and p.suffix.lower() in SPEC_EXTENSIONS
    )
    print(f"Found {len(specs)} OpenAPI specs.")

    for spec_path in specs:
        service_name = spec_path.stem.lower().replace(" ", "_").replace("-", "_")
        output_path = PACKAGE_DIR / service_name

        print(f"Generating client for {service_name} (from {spec_path.name})...")

        spec_data = _load_spec(spec_path)

        needs_patch = False
        if "info" in spec_data and "version" not in spec_data["info"]:
            spec_data["info"]["version"] = "1.0.0"
            needs_patch = True
            print(f" - Patching missing version for {service_name}")

        # Normalize YAML to JSON for the generator (and write a temp file only
        # when we need to mutate the spec or convert format).
        temp_spec_path: Path | None = None
        is_yaml = spec_path.suffix.lower() in {".yaml", ".yml"}
        if needs_patch or is_yaml:
            temp_spec_path = spec_path.with_suffix(".temp.json")
            temp_spec_path.write_text(json.dumps(spec_data), encoding="utf-8")
            spec_arg = temp_spec_path
        else:
            spec_arg = spec_path

        if output_path.exists():
            shutil.rmtree(output_path)
        output_path.mkdir(parents=True)

        cmd = [
            sys.executable, "-m", "openapi_python_client", "generate",
            "--path", str(spec_arg),
            "--meta", "none",
            "--output-path", str(output_path),
            "--overwrite",
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Successfully generated {service_name}")
            else:
                print(f"Failed to generate {service_name}")
                print(result.stderr)
        except Exception as e:
            print(f"An error occurred while generating {service_name}: {e}")
        finally:
            if temp_spec_path is not None and temp_spec_path.exists():
                temp_spec_path.unlink()


if __name__ == "__main__":
    generate_all()
