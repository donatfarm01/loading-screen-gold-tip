"""Loading Screen Gold entry: one loading-screen tip, written to /output/entry.txt.

The tip is a single line for stressed developers and AI coding agents: while
the build loads, the agent waits on the one dependency it cannot install.
The turn is the last word: everything the agent can do is done, and the one
thing left is the human approving it.
"""

import os

ENTRY = "Tip: while this loads, your agent is waiting on the one dependency it cannot install: your approval."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
