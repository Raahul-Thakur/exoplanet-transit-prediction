"""
3D Orbit Animation using Manim + Poliastro

Render with:
    manim -pql orbit_animation.py OrbitScene
    manim -pqh orbit_animation.py OrbitScene
"""

from manim import *
import numpy as np
import astropy.units as u
from astropy.constants import G, M_sun
from poliastro.bodies import Sun as PoliSun
from poliastro.twobody import Orbit


class OrbitScene(ThreeDScene):
    def construct(self):
        # Camera setup
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # Star
        star = Sphere(radius=0.3, color=YELLOW)
        star_label = Text("Star", font_size=24).next_to(star, UP)
        self.add(star, star_label)

        # Orbital parameters
        period_days = 3.5
        star_mass_solar = 1.0
        ecc = 0.3
        inc_deg = 20

        # Kepler's 3rd law
        P = period_days * u.day
        M = star_mass_solar * M_sun
        a = ((G * M * P**2) / (4 * np.pi**2)) ** (1 / 3)
        a_au = a.to(u.AU).value

        # Poliastro orbit (for consistency, not animation directly)
        Orbit.from_classical(
            PoliSun,
            a_au * u.AU,
            ecc * u.one,
            inc_deg * u.deg,
            0 * u.deg,
            90 * u.deg,
            0 * u.deg,
        )

        # Orbit path
        theta = np.linspace(0, 2 * np.pi, 300)
        points = []
        for t in theta:
            r = a_au * (1 - ecc**2) / (1 + ecc * np.cos(t))
            x = r * np.cos(t) * 2
            y = r * np.sin(t) * 2 * np.cos(np.deg2rad(inc_deg))
            z = r * np.sin(t) * 2 * np.sin(np.deg2rad(inc_deg))
            points.append([x, y, z])

        orbit_path = VMobject()
        orbit_path.set_points_smoothly(points)
        orbit_path.set_color(BLUE)
        self.add(orbit_path)

        # Planet
        planet = Sphere(radius=0.15, color=BLUE)
        planet.move_to(points[0])
        planet_label = Text("Planet", font_size=20).next_to(planet, RIGHT)
        self.add(planet, planet_label)

        # Animate motion
        self.play(
            MoveAlongPath(planet, orbit_path),
            MaintainPositionRelativeTo(planet_label, planet),
            run_time=8,
            rate_func=linear,
        )

        # Camera rotation
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        # Info overlay
        info = VGroup(
            Text(f"Period: {period_days} days", font_size=20),
            Text(f"Semi-major axis: {a_au:.3f} AU", font_size=20),
            Text(f"Eccentricity: {ecc}", font_size=20),
            Text(f"Inclination: {inc_deg}°", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT).to_corner(UL)

        self.add_fixed_in_frame_mobjects(info)
        self.play(Write(info))
        self.wait(2)
