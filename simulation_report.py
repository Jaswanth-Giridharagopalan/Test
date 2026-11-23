def classify_run(duration_ms):
    if duration_ms <= 100:
        return "PASS"
    return "FAIL"


if __name__ == "__main__":
    for duration_ms in [85, 100, 120]:
        print(f"{duration_ms} ms: {classify_run(duration_ms)}")
