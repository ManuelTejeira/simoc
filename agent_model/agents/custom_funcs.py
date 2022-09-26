def atmosphere_equalizer(agent):
    """Balance the atmosphere between two agents

    'habitat' and 'greenhouse' are arbitrary variable names
    """
    habitat, greenhouse = agent.selected_storage['in']['atmosphere']
    if not habitat or not greenhouse:
        return
    habitat_volume = habitat.attrs['char_volume']
    greenhouse_volume = greenhouse.attrs['char_volume']
    net_volume = habitat_volume + greenhouse_volume
    habitat_gasses = habitat.view(view='atmosphere')
    greenhouse_gasses = greenhouse.view(view='atmosphere')
    combined_gasses = {**habitat_gasses, **greenhouse_gasses}.keys()
    max_flow = 10_000  # Set very high for B2
    deltas = {}
    for gas in combined_gasses:
        net_mass = getattr(habitat, gas, 0) + getattr(greenhouse, gas, 0)
        equalized = net_mass / net_volume
        deltas[gas] = habitat[gas] - (equalized * habitat_volume)
    net_flow = sum(map(abs, deltas.values()))
    flow_rate = min(1, max_flow/net_flow) if net_flow else 1
    for gas, amount in deltas.items():
        amount_adj = amount * flow_rate
        habitat[gas] -= amount_adj
        greenhouse[gas] += amount_adj
