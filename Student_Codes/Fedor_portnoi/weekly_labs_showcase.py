import json
from datetime import datetime

def lab_10_7(age_value):
    if age_value < 18 or age_value > 75:
        raise ValueError("Invalid age.")
    return (220 - age_value) * 0.7

def lab_10_8(lines):
    outputs = []
    for line in lines:
        parts = line.split()
        if parts[0] == "-1":
            break
        name = parts[0]
        try:
            age = int(parts[1]) + 1
        except ValueError:
            age = 0
        outputs.append(f"{name} {age}")
    return outputs

def lab_10_9(index_value):
    names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
    try:
        return {"out": f"Name: {names[index_value]}", "exc": None}
    except IndexError as e:
        closest = names[0] if index_value < 0 else names[-1]
        return {"out": f"Exception! {e}\nThe closest name is: {closest}", "exc": str(e)}

from datetime import datetime, UTC
from pathlib import Path
import json

def lab_10_7(age_value):
    if age_value < 18 or age_value > 75:
        raise ValueError("Invalid age.")
    return (220 - age_value) * 0.7

def lab_10_8(lines):
    outputs = []
    for line in lines:
        parts = line.split()
        if parts[0] == "-1":
            break
        name = parts[0]
        try:
            age = int(parts[1]) + 1
        except ValueError:
            age = 0
        outputs.append(f"{name} {age}")
    return outputs

def lab_10_9(index_value):
    names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
    try:
        return {"out": f"Name: {names[index_value]}", "exc": None}
    except IndexError as e:
        closest = names[0] if index_value < 0 else names[-1]
        return {"out": f"Exception! {e}\nThe closest name is: {closest}", "exc": str(e)}

def lab_10_10(user_num_str, div_num_str):
    try:
        user_num = int(user_num_str)
        div_num = int(div_num_str)
        return {"out": str(user_num // div_num), "exc": None}
    except ZeroDivisionError as e:
        return {"out": f"Zero Division Exception: {e}", "exc": str(e)}
    except ValueError as e:
        return {"out": f"Input Exception: {e}", "exc": str(e)}

def lab_10_11(steps_count):
    if steps_count < 0:
        raise ValueError("Exception: Negative step count entered.")
    return f"{steps_count / 2000:.2f}"

class StudentInfoError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def find_ID(name, info):
    if name in info:
        return info[name]
    raise StudentInfoError(f"Student ID not found for {name}")

def find_name(student_id, info):
    inverted = {v: k for k, v in info.items()}
    if student_id in inverted:
        return inverted[student_id]
    raise StudentInfoError(f"Student name not found for {student_id}")

def lab_10_12(choice, query):
    student_info = {
        'Reagan': 'rebradshaw835',
        'Ryley': 'rbarber894',
        'Peyton': 'pstott885',
        'Tyrese': 'tmayo945',
        'Caius': 'ccharlton329'
    }
    try:
        if choice == "0":
            return {"out": find_ID(query, student_info), "exc": None}
        return {"out": find_name(query, student_info), "exc": None}
    except StudentInfoError as e:
        return {"out": e.message, "exc": e.message}

def lab_27_1(preentered):
    count = 0
    current_max = None
    try:
        for _ in range(3):
            value = int(preentered[count])
            count += 1
            current_max = value if current_max is None else max(current_max, value)
        return {"out": str(current_max), "exc": None, "count": count}
    except Exception:
        if count == 0:
            return {"out": "0 input(s) read:\nNo max", "exc": "EOFError", "count": count}
        return {"out": f"{count} input(s) read:\nMax is {current_max}", "exc": "EOFError", "count": count}

def run_showcase():
    results = {}
    results["timestamp_utc"] = datetime.now(UTC).isoformat()
    results["lab_10_7"] = {"input": 35, "output": f"Fat burning heart rate for a 35 year-old: {lab_10_7(35):.1f} bpm"}
    results["lab_10_7_invalid"] = {"input": 17, "output": None}
    try:
        lab_10_7(17)
    except Exception as e:
        results["lab_10_7_invalid"]["output"] = f"{e}\nCould not calculate heart rate info."
    lines = ["Lee 18", "Lua 21", "Mary Beth 19", "Stu 33", "-1"]
    results["lab_10_8"] = {"input": lines, "output": lab_10_8(lines)}
    results["lab_10_9_ok"] = {"input": 5, "output": lab_10_9(5)["out"]}
    results["lab_10_9_high"] = {"input": 12, "output": lab_10_9(12)["out"]}
    results["lab_10_9_negative"] = {"input": -2, "output": lab_10_9(-2)["out"]}
    results["lab_10_9_very_negative"] = {"input": -15, "output": lab_10_9(-15)["out"]}
    results["lab_10_10_ok"] = {"input": ["15", "3"], "output": lab_10_10("15", "3")["out"]}
    results["lab_10_10_zero"] = {"input": ["10", "0"], "output": lab_10_10("10", "0")["out"]}
    results["lab_10_10_value"] = {"input": ["15.5", "5"], "output": lab_10_10("15.5", "5")["out"]}
    results["lab_10_11_ok"] = {"input": 5345, "output": lab_10_11(5345)}
    results["lab_10_11_neg"] = {"input": -3850, "output": None}
    try:
        lab_10_11(-3850)
    except Exception as e:
        results["lab_10_11_neg"]["output"] = str(e)
    results["lab_10_12_find_id_ok"] = {"input": ["0", "Reagan"], "output": lab_10_12("0", "Reagan")["out"]}
    results["lab_10_12_find_id_miss"] = {"input": ["0", "Mcauley"], "output": lab_10_12("0", "Mcauley")["out"]}
    results["lab_10_12_find_name_ok"] = {"input": ["1", "rebradshaw835"], "output": lab_10_12("1", "rebradshaw835")["out"]}
    results["lab_10_12_find_name_miss"] = {"input": ["1", "mpreston272"], "output": lab_10_12("1", "mpreston272")["out"]}
    results["lab_27_1_full"] = {"input": ["3", "7", "5"], "output": lab_27_1(["3", "7", "5"])["out"]}
    results["lab_27_1_partial"] = {"input": ["3"], "output": lab_27_1(["3"])["out"]}
    results["lab_27_1_empty"] = {"input": [], "output": lab_27_1([])["out"]}
    return results

results = run_showcase()

output_dir = Path("/content")
output_dir.mkdir(parents=True, exist_ok=True)
md_path = output_dir / "weekly_labs_showcase.md"
json_path = output_dir / "weekly_labs_showcase.json"

report_lines = []
report_lines.append("# Weekly Labs Showcase\n")
report_lines.append(f"Generated: {results['timestamp_utc']}\n")
report_lines.append("## 10.7 Fat-burning Heart Rate\n")
report_lines.append(results["lab_10_7"]["output"] + "\n")
report_lines.append(results["lab_10_7_invalid"]["output"] + "\n")
report_lines.append("## 10.8 Detect String vs Integer\n")
report_lines.append("\n".join(results["lab_10_8"]["output"]) + "\n")
report_lines.append("## 10.9 Exceptions With Lists\n")
report_lines.append(results["lab_10_9_ok"]["output"] + "\n")
report_lines.append(results["lab_10_9_high"]["output"] + "\n")
report_lines.append(results["lab_10_9_negative"]["output"] + "\n")
report_lines.append(results["lab_10_9_very_negative"]["output"] + "\n")
report_lines.append("## 10.10 Simple Integer Division\n")
report_lines.append(results["lab_10_10_ok"]["output"] + "\n")
report_lines.append(results["lab_10_10_zero"]["output"] + "\n")
report_lines.append(results["lab_10_10_value"]["output"] + "\n")
report_lines.append("## 10.11 Step Counter\n")
report_lines.append(results["lab_10_11_ok"]["output"] + "\n")
report_lines.append(results["lab_10_11_neg"]["output"] + "\n")
report_lines.append("## 10.12 Student Info Not Found\n")
report_lines.append(results["lab_10_12_find_id_ok"]["output"] + "\n")
report_lines.append(results["lab_10_12_find_id_miss"]["output"] + "\n")
report_lines.append(results["lab_10_12_find_name_ok"]["output"] + "\n")
report_lines.append(results["lab_10_12_find_name_miss"]["output"] + "\n")
report_lines.append("## 27.1 Input Errors With zyLabs\n")
report_lines.append(results["lab_27_1_full"]["output"] + "\n")
report_lines.append(results["lab_27_1_partial"]["output"] + "\n")
report_lines.append(results["lab_27_1_empty"]["output"] + "\n")

with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines))
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

from google.colab import files
print("Report paths:", md_path, json_path)
files.download(str(md_path))
files.download(str(json_path))