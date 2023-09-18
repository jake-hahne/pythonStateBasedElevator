"""
Enumerated State Machine Example (CYBR 307)
Written by Jake Hahne, Fall 2023

This is a simple example of a state machine that controls a simulated elevator.

    -------- STATES --------
    IDLE - The elevator is waiting for a request.
    MOVING_UP - The elevator is moving up.
    MOVING_DOWN - The elevator is moving down.
    OPEN_DOORS - The elevator doors are opening.
    CLOSE_DOORS - The elevator doors are closing.

    -------- TRANSITIONS --------
    From 'IDLE':
        > If an upward request is received, and the elevator is below the requested floor, move to 'MOVING_UP'.
        > If a downward request is received, and the elevator is above the requested floor, move to 'MOVING_DOWN'.
        > If a request is received, and the elevator is on the requested floor, move to 'OPEN_DOORS'.
    From 'MOVING_UP' or 'MOVING_DOWN':
        > If the elevator reaches the requested floor, move to 'OPEN_DOORS'.
    From 'OPEN_DOORS':
        > If the doors are open for a specified amount of time, move to 'CLOSE_DOORS'.
    From 'CLOSE_DOORS':
        > Return to 'IDLE' if no requests.
        > If there are more requests, process accordingly (either 'MOVING_UP' or 'MOVING_DOWN').

"""

import time
from enum import Enum


class ElevatorState(Enum):
    """Enumerated states for the elevator."""
    IDLE = "IDLE"
    MOVING_UP = "MOVING_UP"
    MOVING_DOWN = "MOVING_DOWN"
    OPEN_DOORS = "OPEN_DOORS"
    CLOSE_DOORS = "CLOSE_DOORS"


class Elevator:
    """
    Defines an Elevator object that can be used to simulate an elevator as a state based machine.
    """

    def __init__(self, current_floor=1):
        self.current_floor = current_floor
        self.destination_floor = None
        self.state = ElevatorState.IDLE

    def request(self, req_floor):
        """Floor request is fed to the elevator."""
        self.destination_floor = req_floor
        if self.state == ElevatorState.IDLE:
            if self.current_floor == req_floor:
                self.open_doors()
            elif self.current_floor < req_floor:
                self.move_up()
            else:
                self.move_down()

    def move_up(self):
        """Moves the elevator up one floor at a time until it reaches the destination floor."""
        self.state = ElevatorState.MOVING_UP
        while self.current_floor < self.destination_floor:
            time.sleep(1)
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")
        self.open_doors()

    def move_down(self):
        """Moves the elevator down one floor at a time until it reaches the destination floor."""
        self.state = ElevatorState.MOVING_DOWN
        while self.current_floor > self.destination_floor:
            time.sleep(1)
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")
        self.open_doors()

    def open_doors(self):
        """Opens the elevator doors."""
        self.state = ElevatorState.OPEN_DOORS
        print("Doors are opening...")
        time.sleep(2)
        self.close_doors()

    def close_doors(self):
        """Closes the elevator doors."""
        self.state = ElevatorState.CLOSE_DOORS
        print("Doors are closing...")
        time.sleep(2)
        self.state = ElevatorState.IDLE
        print("Elevator is now idle.")


# MAIN
if __name__ == "__main__":
    elevator = Elevator()
    floors_to_request = [3, 1, 4, 2, 5, 7, 2, 8, 1]
    for floor in floors_to_request:
        print(f"Requesting floor {floor}")
        elevator.request(floor)
