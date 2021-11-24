from door_controller import DoorController


class TestDoorController:

    def setup_method(self) -> None:
        self.initially_door = DoorController()
        self.opened_door = DoorController(is_opened=True)
        self.closed_door = DoorController(is_opened=False)

    def test_initially_door_is_closed(self):
        # given
        actual = self.initially_door.is_door_opened()
        # when
        expected = False
        # then
        assert actual == expected

    def test_open_door(self):
        actual = self.opened_door.is_door_opened()
        expected = True
        assert actual == expected

    def test_close_door(self):
        actual = self.closed_door.is_door_opened()
        expected = False
        assert actual == expected
