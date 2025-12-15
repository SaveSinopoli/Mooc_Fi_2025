"""Parameters:
- directories: list of root directories to scan
- entrypoint: optional function name to call on each module (e.g., "register")
- require_entry: if True, modules without the entrypoint are treated as failures
- verbose: if True, debug logging is enabled

Returns a mapping:
  root_dir -> list of dicts with keys:
    - 'path': filepath
    - 'module': loaded module object or None
    - 'error': error message or None
    - 'entry_result': result of calling entrypoint (if called), or None

if verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

results: Dict[str, List[Dict[str, object]]] = {} """
import os
directories = "C:/Users/saves/AppData/Local/tmc/vscode/mooc-programming-25"
for root in directories:
    root = os.path.abspath(root)
    results[root] = []
    src_dir = os.path.join(root, "src")
    logger.info("Scanning %s", src_dir)
    if not os.path.isdir(src_dir):
        msg = f"No src/ directory at {src_dir}"
        logger.warning(msg)
        results[root].append({"path": src_dir, "module": None, "error": msg, "entry_result": None})
        continue

    try:
        files = sorted(os.listdir(src_dir))
    except Exception as e:
        tb = traceback.format_exc()
        logger.error("Failed to list %s: %s", src_dir, tb)
        results[root].append({"path": src_dir, "module": None, "error": tb, "entry_result": None})
        continue

    py_files = [f for f in files if f.endswith(".py")]
    if not py_files:
        logger.info("No .py files found in %s", src_dir)
        continue

    for fname in py_files:
        fpath = os.path.join(src_dir, fname)
        module, error = _load_module_from_path(fpath)
        entry_result = None
        if module and entrypoint:
            if hasattr(module, entrypoint):
                try:
                    func = getattr(module, entrypoint)
                    if callable(func):
                        logger.debug("Calling %s on module %s", entrypoint, fpath)
                        entry_result = func()
                    else:
                        entry_result = f"<{entrypoint} exists but is not callable>"
                except Exception:
                    tb = traceback.format_exc()
                    logger.error("Error when calling %s in %s: %s", entrypoint, fpath, tb)
                    error = (error or "") + "\n" + tb
            else:
                msg = f"Entrypoint '{entrypoint}' not found in {fpath}"
                logger.debug(msg)
                if require_entry:
                    error = (error or "") + "\n" + msg
        results[root].append({"path": fpath, "module": module, "error": error, "entry_result": entry_result})
return results