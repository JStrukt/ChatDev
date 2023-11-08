def test_move():
    # Create a snake
    s = Snake(100, 100, 20, 640, 480)
    # Set the snake's direction to 'UP'
    s.direction = 'UP'
    # Move the snake
    s.move()
    # Check the snake's new position
    assert s.body[0] == (100, 80)
