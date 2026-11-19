import sys, types, pathlib
sys.path.extend([str(pathlib.Path(__file__).parent.parent / "Graphics"), str(pathlib.Path(__file__).parent.parent / "Physics")])
sys.modules['pygame'] = types.ModuleType('pygame')
sys.modules['pygame'].init = lambda: None
sys.modules['pygame'].display = types.SimpleNamespace(set_mode=lambda x: None, set_caption=lambda x: None, flip=lambda: None)
sys.modules['pygame'].time = types.SimpleNamespace(Clock=lambda: types.SimpleNamespace(tick=lambda x: None))
sys.modules['pygame'].event = types.SimpleNamespace(get=lambda: [])
sys.modules['pygame'].QUIT = 0
from game_loop import GameLoop
loop = GameLoop()
loop.update()
print("Mock playthrough OK - GameLoop updates without pygame")
