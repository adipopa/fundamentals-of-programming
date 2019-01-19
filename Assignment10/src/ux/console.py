from controllers.controller_exception import ControllerException


class Console:

    def __init__(self, game_controller):
        self.__game_controller = game_controller

    def start_game(self):
        print("New game of PLANES started!")
        print("Welcome Player ONE. We will start by drawing two planes on the board below.")

        self.ui_draw_planes()
        self.__game_controller.ai_draw_planes()

        game_over = False
        while not game_over:
            player_board = self.__game_controller.retrieve_player_board(show_target=True)
            print(player_board)

            player_planes_count = self.__game_controller.get_player_planes_count()
            opponent_planes_count = self.__game_controller.get_opponent_planes_count()

            print("You're standing with " + str(player_planes_count) +
                  (" plane" if player_planes_count == 1 else " planes") + " alive. " +
                  "Your opponent has " + str(opponent_planes_count) +
                  (" plane" if opponent_planes_count == 1 else " planes") + " remaining.")

            if player_planes_count == 0 and opponent_planes_count == 0:
                print("It's a tie, you downed each other!")
                game_over = True

            if opponent_planes_count == 0:
                print("You've won!")
                game_over = True

            if player_planes_count == 0:
                print("Opponent won!")
                game_over = True

            if not game_over:
                self.ui_strike_board()
                self.__game_controller.ai_strike_board()

        keep_alive = True
        while keep_alive:
            user_input = input("Play again? (Y/N): ").strip().upper()
            if user_input == 'Y':
                self.__game_controller.reset_player_board()
                keep_alive = False
                self.start_game()
            elif user_input == 'N':
                keep_alive = False

    def ui_draw_planes(self):
        player_board = self.__game_controller.retrieve_player_board(show_target=False)
        print(player_board)

        for plane_index in range(1, 3):
            if plane_index == 1:
                print("Please enter the start position and direction of the tail for the first plane "
                      "(format: <start_position> <direction>).")
            else:
                print("Same for the second plane. You can also go back one step by typing 'retry'.")
            keep_alive = True
            while keep_alive:
                try:
                    draw_details = input("PLANE " + str(plane_index) + ": ").strip().split()
                    if plane_index == 2 and draw_details[0].lower() == 'retry':
                        self.__game_controller.reset_player_board()
                        self.ui_draw_planes()
                        return
                    if len(draw_details) != 2:
                        raise IOError("Invalid details, insert: <start_position> <direction>")
                    start_position = draw_details[0].upper()
                    direction = draw_details[1].lower()
                    self.__game_controller.draw_plane(start_position, direction)
                    keep_alive = False
                except IOError as io_error:
                    print(str(io_error))
                except ControllerException as controller_exception:
                    print(str(controller_exception))
                except Exception as exception:
                    print(str(exception))

            player_board = self.__game_controller.retrieve_player_board(show_target=False)
            print(player_board)

        print("Your planes have been placed. If you want to draw the planes again, type 'retry', otherwise, type "
              "'start' to start the game.")

        keep_alive = True
        while keep_alive:
            should_start = input(">> ").strip().lower()
            if should_start == 'retry':
                keep_alive = False
                self.__game_controller.reset_player_board()
                self.ui_draw_planes()
            elif should_start == 'start':
                self.__game_controller.next_turn()
                keep_alive = False
            else:
                print("Invalid command.")

    def ui_strike_board(self):
        keep_alive = True
        while keep_alive:
            try:
                strike_position = input("Strike a position: ").strip().upper()
                self.__game_controller.strike_board(strike_position)
                self.__game_controller.next_turn()
                keep_alive = False
            except IOError as io_error:
                print(str(io_error))
            except ControllerException as controller_exception:
                print(str(controller_exception))
            except Exception as exception:
                print(str(exception))
