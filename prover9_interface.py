import subprocess
import logging

def run_prover9(input_data):
    with open("input.in", "w") as f:
        f.write(input_data)
    
    logging.debug(f"Running Prover9 with input:\n{input_data}")
    process = subprocess.run(["./bin/prover9", "-f", "input.in"], capture_output=True, text=True)
    output = process.stdout
    logging.debug(f"Prover9 output:\n{output}")
    return "THEOREM PROVED" in output

def is_move_safe(current_state_facts, new_position):
    facts = "\n".join(current_state_facts)
    goal = f"MoveSafe({new_position[0]},{new_position[1]})."
    move_safe_rule = """
MoveSafe(X, Y).
"""
    input_data = f"""
set(prolog_style_variables).

formulas(assumptions).
{facts}
{move_safe_rule}
end_of_list.

formulas(goals).
{goal}
end_of_list.
"""
    logging.debug(f"Checking if move to {new_position} is safe with the following assumptions and goals:\n{input_data}")
    return run_prover9(input_data)
