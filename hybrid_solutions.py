import random
import time

network_nodes = 10
stake_distribution = [random.randint(1, 10) for _ in range(network_nodes)] 

def simulate_dpos():
    print("\n- Dynamic Proof of Stake (DPoS) -")
    print(f"Network Size: {network_nodes} nodes")
    print(f"Stake Distribution: {stake_distribution}")
    start_time = time.time()

    num_delegates = 3
    total_stake = sum(stake_distribution)
    print(f"Total Stake in the Network: {total_stake}")
    print(f"Number of delegates to be selected: {num_delegates}")
    
    delegates = random.choices(range(network_nodes), weights=stake_distribution, k=num_delegates)

    print(f"Selected Delegates (based on their stake):")
    for delegate in delegates:
        print(f"  - Delegate {delegate} with stake {stake_distribution[delegate]}")
    
    validation_times = []
    for delegate in delegates:
        validation_time = random.uniform(0.01, 0.05)
        time.sleep(validation_time)  
        validation_times.append(validation_time)
        print(f"Delegate {delegate} completed validation in {validation_time:.3f} seconds.")

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time for DPoS (from delegate selection to validation): {total_time:.3f} seconds")
    print("-x-x-x-")
    return total_time

print("Simulating Dynamic Proof of Stake:")
simulate_dpos()

def simulate_hybrid_pos_pbft():
    print("\n- Hybrid PoS + PBFT -")
    print(f"Network Size: {network_nodes} nodes")
    print(f"Stake Distribution: {stake_distribution}")
    start_time = time.time()

    total_stake = sum(stake_distribution)
    print(f"Total Stake in the Network: {total_stake}")
    selected_validator = random.choices(range(network_nodes), weights=stake_distribution, k=1)[0]
    print(f"Selected Validator: Node {selected_validator} with stake {stake_distribution[selected_validator]}")
    consensus_nodes = random.sample(range(network_nodes), k=2 * network_nodes // 3)  
    print(f"Number of nodes required for consensus (2/3 majority): {len(consensus_nodes)}")
    print(f"Nodes involved in reaching consensus: {consensus_nodes}")

    consensus_time = random.uniform(0.05, 0.2)
    print(f"Simulating consensus process... (This may take {consensus_time:.3f} seconds)")
    time.sleep(consensus_time) 
    
    print(f"\nConsensus reached successfully among the selected nodes.")
    print(f"Time taken for PBFT consensus: {consensus_time:.3f} seconds")

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time for Hybrid PoS + PBFT: {total_time:.3f} seconds")
    print("-x-x-x-")
    return total_time

print("Simulating Hybrid PoS + PBFT:")
simulate_hybrid_pos_pbft()
