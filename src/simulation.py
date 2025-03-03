import traci

def apply_modified_model(veh_id):
    leader = traci.vehicle.getLeader(veh_id)
    if leader:
        gap = leader[1]  # 获取与前车间距
        # 论文中的减速度渐变公式：decel = 4.5 * (1 - gap/50)
        decel = 4.5 * (1 - (gap / 50))
        traci.vehicle.setDecel(veh_id, decel)

traci.start(["sumo-gui", "-c", "configs/sim.sumocfg"])
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    for veh_id in traci.vehicle.getIDList():
        apply_modified_model(veh_id)  # 应用改进模型
traci.close()