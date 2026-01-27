import tcod;


from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main():
    screen_width = 80
    screen_height = 50
    
    # hold our player position and center it
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)
    
    tileset = tcod.tileset.load_tilesheet(
        "../resources/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    
    event_handler = EventHandler()
    
    # create our screen
    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial!",
        vsync=True, 
    ) as context:
        # create our console
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        
        while True:
            #print the player to the screen
            root_console.print(player_x, player_y, text="@")
            
            # update screen
            context.present(root_console)
            
            # clear the screen
            root_console.clear()
            
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                
                if action is None:
                    continue
                
                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy 
                    
                elif isinstance(action, EscapeAction):
                    raise SystemExit()
    
    
    

if __name__ == "__main__":
    main()