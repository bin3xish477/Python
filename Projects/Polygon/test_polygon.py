from polygon.polygon import Polygon
import math

def test_polygon():
    n, R = 3, 1
    p = Polygon(n, R)
    assert str(p) == "Polygon(n=3,R=1)", f"actual: {str(p)}"
    assert p.count_vertices == n, f"actual: {p.count_vertices} expected {n}"
    assert p.count_edges == n
    assert p.circumradius == R
    assert p.interior_angle == 60

    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.area == 2.0, f"actual: {p.area}, expected 2.0"
    assert p.side_length, math.sqrt(2)
    assert p.interior_angle == 90


    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    assert p2 < p3
    assert p3 != p4
    assert p1 != p4
    assert p4 == p5

if __name__ == "__main__":
    print("[+] Testing the Polygon class")
    test_polygon()
    print("[+] Testing complete!")
