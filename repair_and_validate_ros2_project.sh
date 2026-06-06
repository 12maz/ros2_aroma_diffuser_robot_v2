#!/usr/bin/env bash
set -e

echo "================================================="
echo "ROS 2 Project Repair and Validation Tool"
echo "================================================="

if [ ! -d "src" ]; then
  echo "ERROR: src folder not found. Run this script from the repository root."
  exit 1
fi

echo ""
echo "Step 1: Creating safety backup..."
BACKUP_DIR="backup_before_repair_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
cp -r src "$BACKUP_DIR/src_backup"
echo "Backup created at: $BACKUP_DIR"

echo ""
echo "Step 2: Repairing ROS 2 Python packages..."

python3 - <<'PY'
from pathlib import Path
import xml.etree.ElementTree as ET
import re

SRC = Path("src")

def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i

def get_package_name(package_xml):
    try:
        root = ET.parse(package_xml).getroot()
        name_el = root.find("name")
        if name_el is not None and name_el.text:
            return name_el.text.strip()
    except Exception:
        pass
    return package_xml.parent.name

def repair_package_xml(pkg_dir, pkg_name):
    package_xml = pkg_dir / "package.xml"

    if not package_xml.exists():
        root = ET.Element("package", {"format": "3"})
        ET.SubElement(root, "name").text = pkg_name
        ET.SubElement(root, "version").text = "0.0.1"
        ET.SubElement(root, "description").text = f"{pkg_name} ROS 2 Python package"
        ET.SubElement(root, "maintainer", {"email": "student@example.com"}).text = "ROS2 Student"
        ET.SubElement(root, "license").text = "MIT"
        ET.SubElement(root, "depend").text = "rclpy"
        export = ET.SubElement(root, "export")
        ET.SubElement(export, "build_type").text = "ament_python"
        indent(root)
        ET.ElementTree(root).write(package_xml, encoding="utf-8", xml_declaration=True)
        return

    tree = ET.parse(package_xml)
    root = tree.getroot()

    if root.find("name") is None:
        ET.SubElement(root, "name").text = pkg_name

    if root.find("version") is None:
        ET.SubElement(root, "version").text = "0.0.1"

    if root.find("description") is None:
        ET.SubElement(root, "description").text = f"{pkg_name} ROS 2 Python package"

    if root.find("maintainer") is None:
        ET.SubElement(root, "maintainer", {"email": "student@example.com"}).text = "ROS2 Student"

    if root.find("license") is None:
        ET.SubElement(root, "license").text = "MIT"

    # Remove duplicate exec_depend/build_depend/test_depend if already present as depend
    generic_depends = {el.text.strip() for el in root.findall("depend") if el.text and el.text.strip()}
    for tag in ["exec_depend", "build_depend", "build_export_depend"]:
        for el in list(root.findall(tag)):
            if el.text and el.text.strip() in generic_depends:
                root.remove(el)

    # Ensure rclpy exists
    if "rclpy" not in generic_depends:
        ET.SubElement(root, "depend").text = "rclpy"

    # Ensure export/build_type
    export = root.find("export")
    if export is None:
        export = ET.SubElement(root, "export")

    build_type = export.find("build_type")
    if build_type is None:
        build_type = ET.SubElement(export, "build_type")
    build_type.text = "ament_python"

    indent(root)
    tree.write(package_xml, encoding="utf-8", xml_declaration=True)

def detect_console_scripts(pkg_dir, pkg_name):
    module_dir = pkg_dir / pkg_name
    scripts = []

    if module_dir.exists():
        for py_file in sorted(module_dir.glob("*.py")):
            if py_file.name == "__init__.py":
                continue
            text = py_file.read_text(errors="ignore")
            if "def main" in text:
                exe_name = py_file.stem
                scripts.append(f"            '{exe_name} = {pkg_name}.{py_file.stem}:main',")

    return scripts

def write_setup_py(pkg_dir, pkg_name):
    scripts = detect_console_scripts(pkg_dir, pkg_name)

    setup_py = pkg_dir / "setup.py"
    content = f'''from setuptools import setup
from glob import glob
import os

package_name = '{pkg_name}'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
        (os.path.join('share', package_name, 'maps'), glob('maps/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ROS2 Student',
    maintainer_email='student@example.com',
    description='{pkg_name} package for ROS 2 Jazzy project.',
    license='MIT',
    entry_points={{
        'console_scripts': [
{chr(10).join(scripts)}
        ],
    }},
)
'''
    setup_py.write_text(content)

def write_setup_cfg(pkg_dir, pkg_name):
    setup_cfg = pkg_dir / "setup.cfg"
    setup_cfg.write_text(f'''[develop]
script_dir=$base/lib/{pkg_name}

[install]
install_scripts=$base/lib/{pkg_name}
''')

def repair_package(pkg_dir):
    package_xml = pkg_dir / "package.xml"
    pkg_name = get_package_name(package_xml) if package_xml.exists() else pkg_dir.name

    print(f"Repairing package: {pkg_name}")

    # Required folders/files
    (pkg_dir / "resource").mkdir(exist_ok=True)
    (pkg_dir / "resource" / pkg_name).touch()

    module_dir = pkg_dir / pkg_name
    module_dir.mkdir(exist_ok=True)
    (module_dir / "__init__.py").touch()

    repair_package_xml(pkg_dir, pkg_name)
    write_setup_cfg(pkg_dir, pkg_name)
    write_setup_py(pkg_dir, pkg_name)

for pkg_dir in sorted(SRC.iterdir()):
    if not pkg_dir.is_dir():
        continue

    if (pkg_dir / "package.xml").exists() or (pkg_dir / "setup.py").exists():
        repair_package(pkg_dir)

print("Repair completed.")
PY

echo ""
echo "Step 3: Showing repaired package structure..."
find src -maxdepth 3 -type f | sort

echo ""
echo "Step 4: Cleaning old build/install/log..."
rm -rf build install log

echo ""
echo "Step 5: Sourcing ROS 2 Jazzy..."
source /opt/ros/jazzy/setup.bash

echo ""
echo "Step 6: Building project..."
PYTHONNOUSERSITE=1 colcon build --symlink-install --merge-install --event-handlers console_direct+

echo ""
echo "Step 7: Sourcing workspace..."
source install/setup.bash

echo ""
echo "Step 8: Checking ROS 2 packages..."
ros2 pkg list | grep -E "lab01_ros2_basics|lab02_nav2_slam_mission_control|lab03_aroma_diffuser_robot_mission" || true

echo ""
echo "Step 9: Checking executables..."
ros2 pkg executables lab01_ros2_basics || true
ros2 pkg executables lab02_nav2_slam_mission_control || true
ros2 pkg executables lab03_aroma_diffuser_robot_mission || true

echo ""
echo "================================================="
echo "Repair and validation completed."
echo "If packages and executables appear above, the project is ready for runtime testing."
echo "================================================="
