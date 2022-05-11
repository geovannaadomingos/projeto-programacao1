class NodeState():
	Normal = (255,255,255)
	Obstacle = (0,0,0)
	FarmerSpawn = (161, 23, 252)
	Plantable = (0,255,0)
	WaterWell = (0,0,255)
	SeedSpawn = (200, 0, 255)

	AllStates = {
		Normal:Obstacle,
		Obstacle:FarmerSpawn,
		FarmerSpawn:Plantable,
		Plantable:WaterWell,
		WaterWell:SeedSpawn,
		SeedSpawn:Normal,
	}