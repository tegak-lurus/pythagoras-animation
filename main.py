from manim import *
class Main(Scene):
    def construct(self):
        tr1 = Main.create_right_triangle(3, 4)
        tr2 = Main.create_right_triangle(15 / 2, 8 / 2)
        tr3 = Main.create_right_triangle(40 / 4, 9 / 4)
        tr4 = Main.create_right_triangle(24 / 2, 7 / 2)

        self.play(*Main.triangle_make(tr1))
        self.play(*Main.triangle_transform(tr1, tr2))
        self.play(*Main.triangle_transform(tr1, tr3))
        self.play(*Main.triangle_transform(tr1, tr4))

    def create_right_triangle(x, y, color=BLUE, color_opacity=0.3):
        # x is width
        # y is height
        tr_w = Polygon([0, 0, 0], [x, 0, 0], [0, y, 0])
        tr_w.set_fill(color, color_opacity)
        # tr_w.move_to(tr_w.get_center() - tr_w.get_center_of_mass())
        tr_w.move_to([0, 0, 0])
        tr_w_x = Tex(Main.format_number(x))
        tr_w_x.next_to(tr_w, DOWN)
        tr_w_y = Tex(Main.format_number(y))
        tr_w_y.next_to(tr_w, LEFT)
        hyp = (x ** 2 + y ** 2) ** 0.5
        tr_w_z = Tex(Main.format_number((x ** 2 + y ** 2) ** 0.5))
        tr_w_z.move_to(tr_w.get_center() + np.array((0.3, 0.3, 0.0)))

        return (tr_w, tr_w_x, tr_w_y, tr_w_z)
    def triangle_make(tr):
        return [Create(tr[0])] + [Write(tr[i]) for i in range(1, 4)]

    def triangle_transform(triangle1, triangle2):
        return [Transform(triangle1[i], triangle2[i]) for i in range(4)]
        
    def format_number(x) :
        if isinstance(x, int):
            return f"{x}"
        elif isinstance(x, float):
            if x.is_integer():
                return f"{int(x)}"
            else:
                return f"{x:.4}"
        else:
            return "NaN"
