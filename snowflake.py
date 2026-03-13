import math

def rotate_point(x, y, degrees):
    """Rotates a point around the center: (0,0)."""
    radians = math.radians(degrees)
    nx = x * math.cos(radians) - y * math.sin(radians)
    ny = x * math.sin(radians) + y * math.cos(radians)
    return nx, ny

def format_points_for_polyline(points):
    """Format points for SVG polyline: 'x1,y1 x2,y2'."""
    points_str = ''
    first = True
    for x, y in points:
        if first:
            first = False
        else:
            points_str += ' '
        points_str += f'{x},{y}'
    return points_str

def rotate_polyline(polyline, sides=8):
    svg = ''
    angle_step = 360 / sides
    for i in range(sides):
        angle = i * angle_step
        rotated_points = []
        for x, y in polyline:
            rotated_points.append(rotate_point(x, y, angle))

        points_str = format_points_for_polyline(rotated_points)
        svg += (f'  <polyline points="{points_str}"' +
               f' stroke="black" fill="none" stroke-width="1" />\n')
    return svg

def generate_circle(radius):
    return (f'  <circle cx="0" cy="0" r="{radius}" stroke="lightgrey"' +
            ' fill="none" stroke-width="1" stroke-dasharray="5, 5" />\n')

def debug_lines(sides=8):
    svg = ''

    # Circles.
    svg += generate_circle(15)
    svg += generate_circle(200)

    # Segments.
    angle_step = 360 / sides
    for i in range(sides):
        angle = i * angle_step
        x1, y1 = rotate_point(0, 0, angle)
        x2, y2 = rotate_point(0, 200, angle)

        points_str = f'{x1},{y1} {x2},{y2}'
        svg += (f'  <polyline points="{points_str}" stroke="lightgrey"' +
               f' fill="none" stroke-width="1" />\n')

    # X, Y axis.
    svg += (f'  <polyline points="0,0 0,200" stroke="lightblue" fill="none"' +
           f' stroke-width="0.5" />\n')
    svg += (f'  <polyline points="0,0 200,0" stroke="lightblue" fill="none"' +
            f' stroke-width="0.5" />\n')

    return svg

def generate_snowflake(filename):
    # SVG header.
    svg = ('<svg width="400" height="400" viewBox="-200 -200 400 400"' +
          ' xmlns="http://www.w3.org/2000/svg">\n')

    svg += debug_lines()

    # The snowflake.
    svg += rotate_polyline([(6, 15), (70, 100), (40, 150), (6, 15)])
    svg += rotate_polyline([(15, 15), (79, 100), (40, 180), (0, 20)])

    # SVG end.
    svg += '</svg>'

    with open(filename, 'w') as f:
        f.write(svg)
    print(f'Snowflake saved to {filename}')

if __name__ == '__main__':
    generate_snowflake('snowflake.svg')
