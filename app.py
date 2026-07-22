import humanize
from pathlib import Path
from time import perf_counter


def main() -> None:
    start = perf_counter()

    # Simulate a tiny build-like workload by scanning local files.
    repo_root = Path(__file__).resolve().parent
    bytes_used = sum(path.stat().st_size for path in repo_root.glob("**/*") if path.is_file())

    elapsed_seconds = perf_counter() - start

    pretty_size = humanize.naturalsize(bytes_used, binary=True)
    elapsed_ms = elapsed_seconds * 1000

    print("Dependency demo with humanize")
    print(f"Measured script runtime: {elapsed_ms:.3f} ms")
    print(f"Workspace size scanned: {pretty_size}")


if __name__ == "__main__":
    main()