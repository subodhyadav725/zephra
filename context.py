import os
from typing import List, Dict, Any

class ContextManager:
    """Manages multi-file context gathering and token estimation for Zephra agent loops."""

    def __init__(self, root_dir: str = "."):
        self.root_dir = root_dir

    def scan_codebase(self, extensions: List[str] = [".py", ".ts", ".js", ".md"]) -> List[Dict[str, str]]:
        files_data = []
        for root, _, files in os.walk(self.root_dir):
            if ".git" in root or "__pycache__" in root or "node_modules" in root:
                continue
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            content = f.read()
                            files_data.append({"path": full_path, "content": content})
                    except Exception as e:
                        print(f"[Zephra Warning] Failed to read {full_path}: {e}")
        return files_data

    def build_prompt_context(self, files: List[Dict[str, str]]) -> str:
        formatted_context = []
        for f in files:
            formatted_context.append(f"--- File: {f['path']} ---\n{f['content']}\n")
        return "\n".join(formatted_context)