import netsquid as ns

print("This example module is located at: {}".format(
      ns.examples.teleportation.__file__))
from netsquid.examples.teleportation import (
    example_network_setup, example_sim_setup)
network = example_network_setup(node_distance=4e-3, depolar_rate=0, dephase_rate=0)
node_a = network.get_node("Alice")
node_b = network.get_node("Bob")
protocol_alice, protocol_bob, dc = example_sim_setup(node_a, node_b)
protocol_alice.start()
protocol_bob.start()
q_conn = network.get_connection(node_a, node_b, label="quantum")
cycle_runtime = (q_conn.subcomponents["qsource"].subcomponents["internal_clock"]
                 .models["timing_model"].delay)
ns.sim_run(cycle_runtime * 100)
print(f"Mean fidelity of teleported state: {dc.dataframe['fidelity'].mean():.3f}")
