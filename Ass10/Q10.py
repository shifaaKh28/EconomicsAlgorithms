#324095702
from abcvoting.preferences import Profile

def custom_equal_shares_verbose(profile, k):
    """
    Implements the Equal Shares method, printing all internal steps.

    Args:
        profile (Profile): An election profile containing voters and their approvals.
        k (int): Size of the committee to select.

    Returns:
        set: The selected committee as a set of candidate indices.
    """
    num_voters = len(profile)
    budget = [1.0 / k] * num_voters  # initial budget per voter
    committee = set()
    candidates = set(range(profile.num_cand))

    print(f"\n=== Running Equal Shares for k={k} ===")
    print(f"Initial budgets per voter: {[round(b, 3) for b in budget]}")

    round_num = 1

    while len(committee) < k:
        print(f"\n--- Round {round_num} ---")
        viable = []

        # Check each candidate not yet in the committee
        for c in sorted(candidates - committee):
            supporters = [i for i, ballot in enumerate(profile) if c in ballot.approved]
            if not supporters:
                print(f"Candidate {c} has no supporters → skipped.")
                continue

            cost_per_voter = 1.0 / len(supporters)
            total_budget = sum(budget[i] for i in supporters)

            print(f"Checking candidate {c}: supported by voters {supporters}")
            print(f"  • Needs {round(cost_per_voter, 3)} per supporter")
            print(f"  • Total supporter budget available: {round(total_budget, 3)}")

            # Check if all supporters can afford their share
            if all(budget[i] >= cost_per_voter for i in supporters):
                print(f"  ✅ Candidate {c} is affordable.")
                viable.append((cost_per_voter, c, supporters))
            else:
                print(f"  ❌ Candidate {c} cannot be afforded.")

        if not viable:
            print("❌ No more viable candidates. Stopping.")
            break

        # Select candidate with minimal cost (tie-breaking by index)
        cost, chosen_cand, supporters = min(viable)
        print(f"\n✅ Selecting candidate {chosen_cand} (cost per supporter: {round(cost, 3)})")
        committee.add(chosen_cand)

        # Deduct cost from supporters' budgets
        for i in supporters:
            budget[i] -= cost

        print(f"Updated budgets after round {round_num}: {[round(b, 3) for b in budget]}")

        round_num += 1

    print(f"\nFinal committee for k={k}: {committee}")
    return committee

def check_monotonicity(committee_k, committee_k1):
    """
    Checks whether the committee for k is a subset of the committee for k+1.

    Args:
        committee_k (set): Committee selected for size k.
        committee_k1 (set): Committee selected for size k+1.

    Returns:
        bool: True if monotonic, False if non-monotonic.
    """
    removed = committee_k - committee_k1
    if removed:
        print(f"\n❗ Non-monotonicity: candidate(s) {removed} were selected for k but not for k+1")
        return False
    else:
        print("\n✅ Monotonic: all members of the smaller committee are in the larger one")
        return True

def prepare_profile(approval_sets):
    """
    Prepares a Profile object from a list of voter approval sets.

    Args:
        approval_sets (list of lists): Each inner list contains candidate indices approved by that voter.

    Returns:
        Profile: The constructed election profile.
    """
    num_cand = max([cand for voter in approval_sets for cand in voter]) + 1
    profile = Profile(num_cand)
    for voter in approval_sets:
        profile.add_voter(voter)
    return profile

# Example block (only one test case here, but you can add more if needed)
examples = [
    {
        "name": "Example for Non-Monotonicity - section A ",
        "approval_sets": [
            [0, 1],  # Voter 0 approves candidates 0,1
            [0, 1],  # Voter 1 approves candidates 0,1
            [2, 3],  # Voter 2 approves candidates 2,3
            [2, 3],  # Voter 3 approves candidates 2,3
        ],
        "num_winners_k": 2,
    },

    {
        "name": "Non-monotonic Without Tie-Breaking - section B",
        "approval_sets": [
            [0],      # Voter 0 approves candidate 0
            [1],      # Voter 1 approves candidate 1
            [1, 2],   # Voter 2 approves candidates 1, 2
            [3],      # Voter 3 approves candidate 3
        ],
        "num_winners_k": 2,
    },
]

# Main loop over examples
for example in examples:
    print(f"\n\n===== Running {example['name']} =====")
    k = example["num_winners_k"]
    approval_sets = example["approval_sets"]
    profile = prepare_profile(approval_sets)

    # Run Equal Shares method for k
    committee_k = custom_equal_shares_verbose(profile, k)

    # Run Equal Shares method for k+1
    committee_k1 = custom_equal_shares_verbose(profile, k + 1)

    # Check monotonicity between k and k+1
    if not check_monotonicity(committee_k, committee_k1):
        print(f"⚠️ Found non-monotonicity in {example['name']} ")
        print(f"------------------------------------------------------------------------------ ")
       
