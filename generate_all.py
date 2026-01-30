import sys
import subprocess
from pathlib import Path

SPECS_DIR = Path("openapi_specs")
PACKAGE_DIR = Path("src/osdu_python_client")

def generate_all():
    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    (PACKAGE_DIR / "__init__.py").touch(exist_ok=True)
    
    specs = list(SPECS_DIR.glob("*.json"))
    print(f"Found {len(specs)} OpenAPI specs.")
    
    for spec_path in specs:
        service_name = spec_path.stem.lower().replace(" ", "_").replace("-", "_")
        output_path = PACKAGE_DIR / service_name
        
        print(f"Generating client for {service_name}...")
        
        # OSDU Specs sometimes miss the 'version' field which is required by the generator
        import json
        with open(spec_path, "r") as f:
            spec_data = json.load(f)
        
        needs_version_patch = False
        if "info" in spec_data and "version" not in spec_data["info"]:
            spec_data["info"]["version"] = "1.0.0"
            needs_version_patch = True
            print(f" - Patching missing version for {service_name}")

        temp_spec_path = spec_path
        if needs_version_patch:
            temp_spec_path = spec_path.with_suffix(".temp.json")
            with open(temp_spec_path, "w") as f:
                json.dump(spec_data, f)

        # Ensure output directory is clean for the generator
        if output_path.exists():
            import shutil
            shutil.rmtree(output_path)
        output_path.mkdir(parents=True)

        cmd = [
            sys.executable, "-m", "openapi_python_client", "generate",
            "--path", str(temp_spec_path),
            "--meta", "none",
            "--output-path", str(output_path),
            "--overwrite"
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
            if needs_version_patch and temp_spec_path.exists():
                temp_spec_path.unlink()

if __name__ == "__main__":
    generate_all()
