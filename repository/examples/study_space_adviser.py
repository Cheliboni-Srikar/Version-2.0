"""Optional section 2.6 demonstration. Run with Python 3; no packages required.

Facts describe a fictional case. An absent fact is not treated as its opposite.
Each call starts with current input facts, so conclusions are recomputed.
This is a teaching example, not a room-booking application.
"""

RULES = (
    ("R4", {"quiet", "power"}, "needs_quiet_power"),
    (
        "R5",
        {"needs_quiet_power", "open_A", "quiet_A", "power_A"},
        "recommend_A",
    ),
)
INPUT_FACTS = {"quiet", "power", "open_A", "closed_A", "quiet_A", "power_A"}


def advise(input_facts):
    """Return current facts, derivation steps, and a clear status message.

    Only current input facts are accepted: callers cannot inject an old derived
    recommendation. The inference loop uses positive rules over finitely many
    symbols and adds each conclusion at most once.
    """
    facts = set(input_facts)
    unexpected = facts - INPUT_FACTS
    if unexpected:
        raise ValueError("Unexpected input facts: " + ", ".join(sorted(unexpected)))
    if {"open_A", "closed_A"}.issubset(facts):
        raise ValueError("Conflicting status: room A cannot be open and closed in this model.")

    trace = []
    changed = True
    while changed:
        changed = False
        for rule_id, conditions, conclusion in RULES:
            if conditions.issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                trace.append((rule_id, tuple(sorted(conditions)), conclusion))
                changed = True

    if "recommend_A" in facts:
        message = "Room A is supported by the current facts and rules."
    elif "closed_A" in facts:
        message = "Room A is known closed; these rules do not support recommending it."
    elif "open_A" not in facts:
        message = "Availability is unknown. Ask: Is room A open?"
    else:
        message = "No recommendation: check the remaining learner needs and room properties."
    return facts, trace, message


def main():
    all_facts = {"quiet", "power", "open_A", "quiet_A", "power_A"}
    cases = (
        ("All five facts", all_facts),
        ("Missing availability", all_facts - {"open_A"}),
        ("Known closed", (all_facts - {"open_A"}) | {"closed_A"}),
        ("Conflicting status", all_facts | {"closed_A"}),
    )
    for title, inputs in cases:
        print("\n" + title)
        print("Inputs: " + ", ".join(sorted(inputs)))
        try:
            _, trace, message = advise(inputs)
        except ValueError as error:
            print("Validation: " + str(error))
            continue
        for rule_id, conditions, conclusion in trace:
            print(rule_id + ": " + " AND ".join(conditions) + " -> " + conclusion)
        print(message)


if __name__ == "__main__":
    main()
