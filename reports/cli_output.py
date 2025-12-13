def print_report(secrets):
    print("\n=== Secret Risk Report ===")
    print(f"Total Secrets Tracked: {len(secrets)}\n")

    sorted_secrets = sorted(secrets, key=lambda x: x[4], reverse=True)

    for idx, sec in enumerate(sorted_secrets[:3], start=1):
        print(
            f"{idx}. {sec[1]} | Risk: {sec[4]} | "
            f"First Seen: {sec[2]} | Occurrences: {sec[3]}"
        )
