"""DI01000111 Engineering Graphics - Unit 2: Engineering Curves.

GTU 2.1-2.2, 5 h, 20 %, 14 marks, CO2. English only. Every curve is built as a numbered construction,
so the reader learns the machinery - divide, project, intersect, join with a French curve.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_DI01000111_u1_notes import (tr, p, h4, ul, ol, table, steps, why, check, pit,  # noqa
                                        card)

SOURCES = [
    ("GTU DI01000111 Engineering Graphics syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("N. D. Bhatt - Elementary Engineering Drawing, Charotar Publishing House, Anand (chapters 4-6: "
     "conic sections, cycloidal curves, involutes and spirals)", "https://www.charotarbookstall.com/"),
    ("P. S. Gill - A Text Book of Engineering Drawing, S. K. Kataria & Sons, Delhi (engineering "
     "curves and their applications)", "https://www.skkatariaandsons.com/"),
    ("BIS SP 46 - Engineering drawing practice: construction of curves, tangent and normal",
     "https://www.bis.gov.in/"),
]

NOTES = [
    {"title": tr("1. Conic Sections and the Ellipse"),
     "items": [
         card("2.1 One cone, three curves: eccentricity decides",
              h4("The definition that replaces a hundred methods")
              + p("A conic is the locus of a point whose distance from a fixed point (the focus) "
                  "bears a constant ratio to its distance from a fixed straight line (the directrix). "
                  "That ratio is the <b>eccentricity e</b>, and it alone decides which of the three "
                  "curves you get - which is why one construction serves all three.")
              + table(["eccentricity", "curve", "where it is used"], [
                  ("e less than 1", "ellipse", "gear blanks, manhole covers, arches, elliptical "
                   "trainings (reflector), the shadow of a lamp on a wall"),
                  ("e = 1", "parabola", "headlight and dish reflector, suspension bridge cable, "
                   "projectile path, road summit, optical instruments"),
                  ("e greater than 1", "hyperbola", "cooling tower shell, gear tooth flank in some "
                   "gears, navigation (Loran), shock-wave curves"),
              ])
              + h4("A cutting plane through a cone")
              + p("Cut a right circular cone by a plane: parallel to the base gives a circle, tilted "
                  "but cutting one nappe gives an ellipse, parallel to a generator (slant side) "
                  "gives a parabola, and steeper still, cutting both nappes, gives a hyperbola with "
                  "two branches. The construction methods are therefore interchangeable - a conic "
                  "may be drawn from its eccentricity or from its axes.")
              + h4("The three ways a conic is set in an exam")
              + ul("<b>Given the axes or the base and height</b> - draw the rectangle or the two "
                   "circles and project (the method used in this unit).",
                   "<b>Given the focus and the directrix</b> - use the eccentricity construction: "
                   "for every point, distance from the focus = e x distance from the directrix.",
                   "<b>Given a tangent and a point</b> - the tangent method, useful for a parabola "
                   "when only the base, the axis and one point are known.")
              + h4("How to set out any conic in five steps")
              + steps("Read what is given: the axes, the base and the height, the focus and the "
                      "directrix, or a tangent and a point. That choice decides the construction.",
                      "Compute the numbers before drawing - a, b, c and e for the ellipse; 4a and the "
                      "focus distance for the parabola; the constant x times y for the hyperbola.",
                      "Draw the skeleton thin: the axes or the base and axis, the asymptotes, the "
                      "directrix, and the circles or the rectangle that will be divided.",
                      "Divide the skeleton into equal parts, project from both families, and mark "
                      "every intersection - the points of the curve come from the intersections, "
                      "never from guessing.",
                      "Join the marks with a French curve in one smooth thick stroke and prove the "
                      "curve: the focal sum for the ellipse, the eccentricity for the parabola, the "
                      "constant product for the hyperbola.")
              + why("Once e is fixed the shape is fixed, whatever the size: an ellipse of e = 0.6 is "
                    "the same ellipse at 40 mm or 4 m. That is why every construction reduces to the "
                    "same ratio, drawn graphically.")
              + pit("Mixing the focus-directrix ratio the wrong way round turns an ellipse into a "
                    "hyperbola. Write e = distance from focus / distance from directrix on the sheet "
                    "before you start."),
              diagram="u2_conic", syllabus_item="2.1"),
         card("2.2 The ellipse by concentric circles",
              h4("Given the major axis 100 mm, the minor axis 60 mm")
              + p("The ellipse is the locus of a point whose sum of distances from the two foci is "
                  "constant and equal to the major axis. The concentric-circle method turns that "
                  "definition into a projection: every point of the ellipse is the meeting point of a "
                  "horizontal from the major circle and a vertical from the minor circle.")
              + steps("Draw the major axis AB = 100 mm and the minor axis CD = 60 mm, bisecting each "
                      "other at right angles at the centre O.",
                      "With O as centre and radius 50 mm (half the major axis) draw the major circle; "
                      "with radius 30 mm draw the minor circle.",
                      "Divide the major circle into twelve equal parts - 30 degrees apart - with the "
                      "protractor, and number the rays 1, 2, 3 ... 11.",
                      "From each division point on the major circle drop a line perpendicular to the "
                      "major axis; from the matching point on the minor circle draw a line parallel "
                      "to the major axis.",
                      "Where the vertical from point n meets the horizontal from point n, mark a "
                      "point of the ellipse. Repeat for all twelve rays, and add the two axis ends.",
                      "Join the points with a French curve in a smooth thick line, and erase nothing "
                      "of the construction until the curve is checked.")
              + h4("Sizes you must be able to predict")
              + ul("Major axis 100 mm, minor 60 mm, semi-axes a = 50 and b = 30.",
                   "Distance between the foci = 2 x sqrt(a squared - b squared) = 2 x sqrt(2500 - "
                   "900) = 2 x 40 = 80 mm, so each focus is 40 mm from the centre.",
                   "Eccentricity e = sqrt(1 - b squared / a squared) = 0.8, so the ellipse is fairly "
                   "flat.",
                   "Sum of the focal distances of any point = 2a = 100 mm - the quickest check on a "
                   "finished curve.")
              + h4("Tangent and normal at a point P")
              + ol("Join P to both foci F1 and F2.",
                   "Bisect the angle F1 P F2 externally; the bisector is the tangent at P.",
                   "The normal is perpendicular to that tangent at P, and it bisects the internal "
                   "angle between P F1 and P F2.")
              + why("A ray from one focus reflects to the other, which is exactly why an elliptical "
                    "room whispers across its foci and why elliptical gears run smoothly through a "
                    "variable speed.")
              + pit("Dividing the circle by stepping a chord instead of by angles makes the last ray "
                    "miss the vertical axis; use the protractor and check that ray 12 closes on the "
                    "starting point."),
              diagram="u2_ellipse", syllabus_item="2.1"),
     ]},
]

NOTES.append({"title": tr("2. The Parabola and the Hyperbola"),
              "items": [
    card("2.2 The parabola: ordinates and the focus-directrix",
         h4("Given the base 100 mm and the axis height 60 mm")
         + p("A parabola is the locus of a point equidistant from the focus and the directrix, so "
             "e = 1. Its second property is easier to draw with: the height falls off as the square "
             "of the distance from the axis. With the vertex at the top of the axis and the base "
             "horizontal, the height above the base at a distance x from the axis is "
             "h = r (1 - x squared / s squared), where s is half the base and r is the height.")
         + h4("Method A - ordinates (offsets) from the axis")
         + steps("Draw the base AB = 100 mm, erect the axis 60 mm at its midpoint O, and mark the "
                 "vertex V at the top of the axis.",
                 "Mark the ordinate positions on the base, 10 mm apart, at x = 10, 20, 30, 40 and 50 "
                 "mm either side of the axis.",
                 "Work out the height for each: x = 10 gives 57.6 mm; 20 gives 50.4 mm; 30 gives "
                 "38.4 mm; 40 gives 21.6 mm; 50 gives 0 mm, which is the base corner.",
                 "Erect perpendiculars of those heights at the marked points, above and below the "
                 "axis, and mark the ends.",
                 "Join the marks from A through V to B with a French curve and ink the parabola "
                 "thick; plot the mirror-image points to prove the curve is symmetric.")
         + h4("Method B - focus and directrix (the definition itself)")
         + steps("For the same parabola the focus is a = 10.4 mm from the vertex on the axis and the "
                 "directrix is the same distance on the other side, because 4a = 100 squared / "
                 "(4 x 60) = 41.7 mm.",
                 "Draw the directrix as a line parallel to the base at 10.4 mm behind the vertex, and "
                 "mark the focus F on the axis, 10.4 mm in front of it.",
                 "Take any distance d from the directrix, draw a line parallel to the directrix at "
                 "that distance, and strike an arc of radius d about F.",
                 "The two intersections are points of the parabola, because the point is then equally "
                 "far from F and from the directrix.",
                 "Repeat for d = 20, 30, 40, 50 mm and join the points - the same curve as Method A.")
         + h4("Sizes to check it with")
         + ul("Symmetry about the axis, and the vertex exactly at the top of the 60 mm axis.",
              "At x = 25 mm the height above the base is 60 x (1 - 0.25) = 45 mm.",
              "The latus rectum, the width of the curve at the focus, is 4a = 41.7 mm.",
              "The tangent at a point bisects the angle between the focal distance and a line "
              "parallel to the axis - the property every headlamp reflector uses.")
         + h4("Tangent and normal at a point P")
         + ol("From P drop a perpendicular to the axis, meeting it at M.",
              "Mark T on the axis so that the vertex V is the midpoint of M T.",
              "Join T to P: that is the tangent, and the normal is perpendicular to it at P.")
         + why("Both methods describe the same set of points: the square law is the definition "
               "squared, and the focus-directrix construction is the definition itself. Drawing with "
               "ordinates is quicker with a scale; drawing with the focus and directrix explains why "
               "the curve reflects parallel rays.")
         + pit("Measuring the ordinate from the vertex instead of from the base doubles the number of "
               "wrong points; write the formula on the sheet with r and s substituted before you "
               "start."),
         diagram="u2_parabola", syllabus_item="2.1"),
    card("2.2 The hyperbola from its asymptotes",
         h4("Given the asymptotes and one point on the curve")
         + p("A hyperbola has e greater than 1 and two branches. When its asymptotes are at right "
             "angles it is a <b>rectangular hyperbola</b>, and for that curve the product of the "
             "distances from the asymptotes is constant: x times y = a squared. That single number "
             "lets you set out as many points as you like with a scale.")
         + steps("Draw the two asymptotes at the given angle - here at 90 degrees - meeting at O, and "
                 "mark the given point P.",
                 "Measure the perpendicular distances of P from the two asymptotes: x = 40 mm and "
                 "y = 30 mm, so a squared = 40 x 30 = 1200.",
                 "Make a short table: x = 20 gives y = 60; x = 30 gives y = 40; x = 40 gives y = 30 "
                 "(the given point); x = 60 gives y = 20; x = 80 gives y = 15; x = 120 gives y = 10.",
                 "Set each pair of distances off along the two asymptotes with the divider, drop the "
                 "perpendiculars and mark the intersections - they are points of the curve.",
                 "Repeat in all four quadrants, using the same distances along the opposite arms; the "
                 "curve is symmetric about both asymptotes for a rectangular hyperbola.",
                 "Join the points of each branch with a French curve, drawing the branch asymptotic "
                 "to its two asymptotes and inking only the committed points thick.")
         + h4("The other two ways it is set")
         + ul("<b>Focus and directrix</b>: distance from the focus = e x distance from the directrix, "
              "with e greater than 1 - so points are found on arcs of circles struck from the focus.",
              "<b>Given the transverse axis and a point</b>: use the symmetry of the foci and the "
              "constant difference of the focal distances, which equals the transverse axis.")
         + h4("Tangent and normal")
         + p("Join the point P to the two foci; the tangent bisects the angle between one focal "
             "distance and the other produced, and the normal bisects the angle between the two focal "
             "distances themselves - the mirror image of the ellipse rule.")
         + why("A cooling tower, a lighthouse reflector and the Loran navigation chart all use the "
               "same curve: the hyperbola is the locus of a constant difference of distances, which "
               "is exactly what a time-difference measurement produces.")
         + pit("Using the same table for both branches with the signs ignored gives a curve that "
               "crosses the axis; plot each branch in its own quadrant and keep the asymptotes thin."),
         diagram="u2_hyperbola", syllabus_item="2.1"),
]})

NOTES.append({"title": tr("3. Cycloidal Curves, Involutes and Spirals"),
              "items": [
    card("2.2 The cycloid - a point on a rolling circle",
         h4("One turn of a circle on a straight line")
         + p("A cycloid is the path traced by a point on the circumference of a circle that rolls "
             "without slipping along a straight line. The same idea on a curved base gives an "
             "epicycloid (rolling outside a circle) or a hypocycloid (rolling inside it) - the shapes "
             "of gear teeth that do not slip.")
         + steps("For a circle of radius r = 25 mm, the length of one rolling turn is its "
                 "circumference 2 x pi x r = 157 mm. Draw the base line AX 157 mm long.",
                 "Draw the generating circle of radius 25 mm in its starting position with its centre "
                 "C on the base line, and mark the generating point P on the circumference at the "
                 "bottom, touching the base line.",
                 "Divide the circle into twelve equal parts, 30 degrees apart, and number them.",
                 "Divide the base line into the same twelve equal parts, each 157 / 12 = 13.1 mm, and "
                 "number the points 1 to 12.",
                 "Draw the circle again in each of its twelve positions, with its centre 13.1 mm "
                 "further along the base line each time.",
                 "Through the division points on the first circle draw lines parallel to the base "
                 "line; where the line from division n meets the circle in position n, mark a point "
                 "of the cycloid.",
                 "Join the twelve points with a French curve, starting and finishing on the base line "
                 "at the cusps, and ink the curve thick.")
         + h4("Tangent and normal at a point")
         + ol("Mark the point of contact T where the generating circle in that position touches the "
              "base line - this is the instantaneous centre.",
              "Join T to the point P on the curve: that line is the normal.",
              "Draw the tangent perpendicular to the normal at P.")
         + h4("Sizes to predict")
         + ul("Length of the base for one turn = 2 pi r = 6.283 r, so for r = 25 mm it is 157 mm.",
              "Height of the curve = 2 r = 50 mm, and it is not symmetric about its middle: the "
              "steepest part is near the cusps.",
              "Epicycloid: rolling outside a circle of radius R; hypocycloid: rolling inside it, and "
              "when r = R / 4 the hypocycloid becomes four straight lines - the familiar Trammel of "
              "Archimedes.")
         + why("A wheel rolling on a road traces the path a point on its rim actually travels; the "
               "cycloid is therefore the shape of a gear tooth that rolls without sliding, and the "
               "cheapest way to understand epicycloidal clock gearing.")
         + pit("Dividing the base line into twelve parts but leaving the circle at eight makes the "
               "two families mismatch; the count of divisions must be identical on the circle and on "
               "the base."),
         diagram="u2_cycloid", syllabus_item="2.2"),
    card("2.2 The involute - a thread unwinding from a circle",
         h4("The curve a taut thread leaves behind")
         + p("An involute is the path traced by a point on a taut string as the string unwinds from a "
             "circle or a polygon. Each point of the curve is a distance from the circle equal to the "
             "length of string already unwound, measured along the tangent - which makes the "
             "construction a matter of stepping lengths along tangents.")
         + steps("Draw the circle of radius 20 mm and divide it into twelve equal parts; the "
                 "circumference is 2 x pi x 20 = 125.7 mm.",
                 "At each division point draw a tangent to the circle, in the direction the string "
                 "would unwind.",
                 "On the first tangent set off 1/12 of the circumference = 10.5 mm; on the second "
                 "21.0 mm; on the third 31.4 mm, and so on, so that the length grows by 10.5 mm each "
                 "time.",
                 "Mark the end of each length - these twelve points lie on the involute.",
                 "Join them with a French curve, starting at the point where the string leaves the "
                 "circle and ending at the length for one full turn, 125.7 mm.",
                 "Draw the tangent and normal: the normal at any point is the tangent to the circle "
                 "from that point, and the tangent is perpendicular to it.")
         + h4("Why an involute and not a cycloid")
         + ul("Two involute gear teeth in contact keep a constant pressure angle, so the drive is "
              "smooth and the centre distance may vary slightly without changing the ratio.",
              "Length of the involute for one full turn of the circle = the circumference, 2 pi r.",
              "The same construction on a polygon - square, pentagon, hexagon - gives the involute of "
              "that polygon: unwrap side by side, adding the next side to the tangent each time.")
         + why("The string that unwinds is always taut, so it is always normal to the curve: that "
               "single fact gives both the construction and the rule for the normal.")
         + pit("Stepping the same length on every tangent gives an Archimedean spiral, not an "
               "involute; the length must grow by one twelfth of the circumference at each step."),
         diagram="u2_involute", syllabus_item="2.2"),
    card("2.2 The Archimedean spiral",
         h4("A point that moves out while the radius turns")
         + p("A spiral is the locus of a point that moves uniformly along a line while the line "
             "rotates uniformly about a fixed point. When the outward motion is uniform the curve is "
             "an Archimedean spiral, and its polar equation is r = a x theta - the radius is "
             "proportional to the angle turned.")
         + steps("Draw the largest circle of radius R = 50 mm, the circle reached after one full "
                 "turn, and draw twelve radii 30 degrees apart.",
                 "Divide the radius of that circle into twelve equal parts, 4.17 mm each.",
                 "On the first radius set off one part from the centre, on the second two parts, on "
                 "the third three, and so on; on the twelfth radius set off the whole radius R.",
                 "Mark each of the twelve points.",
                 "Join the points with a French curve, spiralling outwards from the centre and "
                 "finishing on the full circle.",
                 "For a second turn, repeat with radii up to 2R, using the same pitch - the distance "
                 "between successive turns is constant and equal to R / 12 for a one-turn spiral.")
         + h4("Where it is used")
         + ul("Cam profiles in which the follower rises with a uniform velocity - the Archimedean "
              "spiral is the only curve that gives a constant rise per degree.",
              "Volute springs, spiral staircases, clock springs, screw conveyor flights and the "
              "scroll of a pump casing.",
              "Logarithmic spiral: radius grows in proportion to itself, used for gear teeth of "
              "certain forms and found in nature; it is not drawn by this method.")
         + why("The construction is a race between two uniform motions - one round, one out - so the "
               "radius at the eleventh ray must be eleven twelfths of R, and the last point must land "
               "exactly on the circle.")
         + pit("Dividing the largest circle into unequal steps closes the spiral on the wrong radius; "
               "the radius divisions and the angle divisions must be the same in number."),
         diagram="u2_spiral", syllabus_item="2.2"),
]})

_PRACTICE = [
    ("Draw an ellipse of major axis 100 mm and minor axis 60 mm by the concentric-circle method. "
     "Find its eccentricity, the distance between the foci, and draw a tangent at a point 30 mm from "
     "the centre on the major axis.", 5,
     [h4("Given and required")
      + p("Major axis 2a = 100 mm, so a = 50 mm; minor axis 2b = 60 mm, so b = 30 mm."),
      h4("Construction, step by step")
      + ol("Draw the major axis AB = 100 mm, the minor axis CD = 60 mm, bisecting at O at right "
           "angles.",
           "With centre O and radius 50 mm draw the major circle; with radius 30 mm draw the minor "
           "circle.",
           "Divide the major circle into twelve equal parts with the protractor, 30 degrees apart, "
           "and draw all twelve radii.",
           "From each point on the major circle drop a perpendicular to AB; from the matching point "
           "on the minor circle draw a parallel to AB.",
           "Mark the intersection of the vertical from point n with the horizontal from point n; "
           "that is a point of the ellipse. Do all twelve and add A, B, C and D.",
           "Join the points with a French curve, thick, and leave the construction thin."),
      h4("The numbers")
      + p("c = sqrt(a squared - b squared) = sqrt(2500 - 900) = 40 mm, so the two foci are 80 mm "
          "apart, 40 mm each side of O, and e = c / a = 40 / 50 = 0.8. A check on the finished curve: "
          "for any point on it, the sum of the distances to the two foci is 2a = 100 mm."),
      h4("Tangent at the point P, 30 mm from O on the major axis")
      + ol("Mark P on the major axis 30 mm from O, inside the curve - it is the point of contact "
           "asked for on the axis, so use the tangent rule at a point on the ellipse nearest to it.",
           "Join P to both foci F1 and F2.",
           "Bisect the angle F1 P F2 externally with the compass; the bisector is the tangent.",
           "Draw the normal perpendicular to it at P; it bisects the internal angle between P F1 and "
           "P F2."),
      p("<b>Answer.</b> The ellipse of 100 mm by 60 mm has e = 0.8 and foci 80 mm apart; the tangent "
        "at a point on the major axis is perpendicular to that axis, and the general rule - the "
        "tangent bisects the external angle between the focal distances - gives it at once.")]),
    ("Draw an ellipse with a major axis of 100 mm and the distance between the foci equal to 60 mm, "
     "using the arcs-of-circles method. State the minor axis.", 4,
     [h4("Before drawing")
      + p("a = 50 mm and c = 30 mm, so b = sqrt(a squared - c squared) = sqrt(2500 - 900) = 40 mm and "
          "the minor axis is 80 mm."),
      h4("Construction, step by step")
      + ol("Draw the major axis AB = 100 mm and mark the foci F1 and F2, 30 mm either side of the "
           "centre O.",
           "Mark a series of points 1, 2, 3 ... on AB between O and B - say every 10 mm.",
           "With centre F1 and radius equal to the distance from A to point 1, draw an arc; with "
           "centre F2 and radius equal to the distance from B to point 1, draw an arc cutting the "
           "first. The intersection is a point of the ellipse, because the two radii add up to AB.",
           "Repeat for every marked point, above and below the axis, and interchange the two radii to "
           "get the mirror-image points.",
           "Mark the ends of the minor axis by striking arcs of radius a from each focus on the "
           "perpendicular through O.",
           "Join all the points with a French curve and ink the ellipse thick."),
      h4("Checks")
      + p("Every point must satisfy P F1 + P F2 = 100 mm; measure two of them with the scale. The "
          "curve must pass through A, B and the two ends of the 80 mm minor axis."),
      p("<b>Answer.</b> An ellipse of 100 mm major and 80 mm minor axis, built from arcs struck from "
        "the two foci with radii that always sum to the major axis.")]),
    ("Construct a parabola with a base of 100 mm and an axis height of 60 mm, and draw the tangent "
     "and normal at a point 25 mm from the axis.", 5,
     [h4("Given")
      + p("Base AB = 100 mm, so s = 50 mm; axis height r = 60 mm with the vertex V at the top of the "
          "axis above the midpoint O."),
      h4("Construction, step by step")
      + ol("Draw AB = 100 mm, erect the axis 60 mm at O, mark the vertex V, and mark the ordinate "
           "positions 10, 20, 30, 40 and 50 mm either side of the axis.",
           "Compute the heights from h = r (1 - x squared / s squared): 57.6, 50.4, 38.4, 21.6 and "
           "0 mm for x = 10, 20, 30, 40 and 50 mm.",
           "Erect those perpendiculars above and below the axis and mark the ends.",
           "Join the marks from A through V to B with a French curve and ink the parabola thick.",
           "Check the symmetry and check the height at x = 25 mm, which must measure 45 mm."),
      h4("Tangent and normal at the point 25 mm from the axis")
      + ol("Mark P on the curve 25 mm from the axis, 45 mm above the base.",
           "Drop a perpendicular from P to the axis, meeting it at M.",
           "Mark T on the axis so that the vertex V is the midpoint of M T.",
           "Join T to P for the tangent, and draw the normal perpendicular to it at P."),
      h4("The numbers")
      + p("x squared = 4 a y with the vertex as origin: 2500 = 4a x 60, so a = 10.4 mm and the latus "
          "rectum 4a = 41.7 mm. The focus is 10.4 mm from the vertex on the axis, and the directrix "
          "is the same distance on the other side."),
      p("<b>Answer.</b> A parabola of 100 mm base and 60 mm height through ten plotted ordinates; at "
        "25 mm from the axis the point stands 45 mm above the base and its tangent is found by making "
        "the vertex the midpoint of M T.")]),
    ("Draw a rectangular hyperbola through a point P whose distances from the two asymptotes are "
     "40 mm and 30 mm, the asymptotes being at right angles.", 5,
     [h4("The constant of the curve")
      + p("For a rectangular hyperbola x times y is constant, and here that constant is "
          "40 x 30 = 1200 mm squared. Every other point follows from it."),
      h4("Construction, step by step")
      + ol("Draw the two asymptotes at 90 degrees, meeting at O.",
           "Mark P at 40 mm from one asymptote and 30 mm from the other.",
           "Make the table: x = 20, y = 60; x = 30, y = 40; x = 40, y = 30; x = 60, y = 20; x = 80, "
           "y = 15; x = 120, y = 10.",
           "Set each pair off along the asymptotes with the divider, erect the perpendiculars and "
           "mark the intersection - that is a point of the curve.",
           "Plot the same pairs in the opposite quadrant to obtain the second branch, and complete "
           "the two branches symmetrically about O.",
           "Join each branch with a French curve, letting it approach both asymptotes without "
           "touching them, and ink the curve thick."),
      h4("Checks")
      + p("Every constructed point must satisfy x times y = 1200: at 60 mm out the height must be "
          "20 mm. The branches must never cross the asymptotes, and the curve must look smoother the "
          "further it runs from O."),
      p("<b>Answer.</b> A rectangular hyperbola x y = 1200 through P (40, 30), with six points per "
        "branch set out from the asymptotes and the branches asymptotic to both axes.")]),
    ("Draw one turn of the cycloid traced by a point on a circle of 50 mm diameter rolling on a "
     "straight line, and draw the tangent and normal three-eighths of a turn from the start.", 5,
     [h4("Lengths first")
      + p("r = 25 mm, so the base for one turn is 2 pi r = 157.1 mm and the height of the curve is "
          "2r = 50 mm. With twelve divisions the step on the base is 157.1 / 12 = 13.1 mm."),
      h4("Construction, step by step")
      + ol("Draw the base line AX = 157 mm and divide it into twelve equal parts of 13.1 mm.",
           "Draw the generating circle of radius 25 mm at the start, its centre C on the base line "
           "and the generating point P at the bottom point of contact.",
           "Divide the circle into twelve equal parts, 30 degrees apart.",
           "Draw the circle in all twelve positions, each centre 13.1 mm further along the base.",
           "Through the twelve division points of the first circle draw lines parallel to the base.",
           "Where the parallel from division n meets the circle in position n, mark a point; do all "
           "twelve.",
           "Join the points with a French curve from cusp to cusp and ink the cycloid thick."),
      h4("Tangent and normal at three-eighths of a turn")
      + ol("Three-eighths of a turn is 3 x 12 / 8 = 4.5 divisions along the base, 59 mm from the "
           "start.",
           "Draw the generating circle in that position and mark the point of contact T with the base "
           "line - the instantaneous centre.",
           "Join T to the point P on the curve: T P is the normal.",
           "Draw the tangent perpendicular to the normal at P."),
      p("<b>Answer.</b> A cycloid of 157 mm base and 50 mm height through twelve constructed points, "
        "with the normal at any point passing through the point of contact of the generating circle "
        "with the base line.")]),
    ("Draw the involute of a circle of 40 mm diameter for one complete turn, and state the length of "
     "the tangent at each of the twelve steps.", 4,
     [h4("Lengths first")
      + p("r = 20 mm, so the circumference is 2 pi r = 125.7 mm and one twelfth is 10.5 mm."),
      h4("Construction, step by step")
      + ol("Draw the circle of radius 20 mm and divide it into twelve equal parts.",
           "At each division point draw a tangent, in the direction in which the string would unwind.",
           "On the successive tangents set off 10.5, 21.0, 31.4, 41.9, 52.4 mm and so on - each "
           "length greater than the last by 10.5 mm.",
           "Mark the end of each length; the twelve marks lie on the involute.",
           "Join the marks with a French curve, starting at the circle and ending at 125.7 mm from "
           "it, and ink thick.",
           "Draw the tangent and normal: the normal at any point is the tangent to the circle drawn "
           "from that point."),
      p("<b>Answer.</b> An involute of one turn whose tangent lengths grow by 10.5 mm at each of the "
        "twelve steps, from 10.5 mm to 125.7 mm, with the normal at every point touching the circle.")]),
    ("Draw an Archimedean spiral of maximum radius 60 mm over one and a half turns, and state its "
     "pitch.", 3,
     [h4("Pitch first")
      + p("The outward growth must be uniform: over 1.5 turns the radius grows from 0 to 60 mm, so "
          "the pitch - the growth per full turn - is 60 / 1.5 = 40 mm. With twelve divisions per turn "
          "there are eighteen steps and each grows the radius by 60 / 18 = 3.33 mm."),
      h4("Construction, step by step")
      + ol("Draw the largest circle of radius 60 mm and draw radii 30 degrees apart, eighteen of them "
           "over the one and a half turns.",
           "Divide one radius into eighteen equal parts of 3.33 mm.",
           "On the first radius set off one part, on the second two, and so on, so that the radius "
           "grows by 3.33 mm at every 30 degrees.",
           "Mark each point, and after twelve steps the point must lie on the 40 mm circle - the end "
           "of the first turn.",
           "Join the points with a French curve from the centre outwards, finishing on the 60 mm "
           "circle."),
      p("<b>Answer.</b> A spiral growing 3.33 mm per 30 degrees, reaching 40 mm at the end of the "
        "first turn and 60 mm at the end of the half turn, with a pitch of 40 mm.")]),
]

EQUATIONS = [
    {"title": tr("Conic sections"),
     "items": [
         {"name": tr("Eccentricity"),
          "f": "e = distance from focus / distance from directrix",
          "terms": tr("e below 1 gives an ellipse, e = 1 a parabola, e above 1 a hyperbola. This one "
                      "ratio fixes the shape at every size.")},
         {"name": tr("Ellipse: foci and eccentricity"),
          "f": "c = sqrt(a squared - b squared),  e = c / a,  P F1 + P F2 = 2 a",
          "terms": tr("a and b are the semi-major and semi-minor axes; the focal sum 2a is the "
                      "quickest check on a finished curve.")},
         {"name": tr("Parabola"),
          "f": "x squared = 4 a y,  latus rectum = 4 a",
          "terms": tr("With the vertex as origin and the axis along y; for a 100 mm base and 60 mm "
                      "height, 4a = 100 squared / (4 x 60) = 41.7 mm.")},
         {"name": tr("Rectangular hyperbola"),
          "f": "x times y = a squared",
          "terms": tr("The product of the distances from the two asymptotes is constant, so a table "
                      "of x and y sets out any number of points.")},
     ]},
    {"title": tr("Cycloidal curves, involutes and spirals"),
     "items": [
         {"name": tr("Cycloid"),
          "f": "base = 2 pi r,  height = 2 r",
          "terms": tr("One turn of the generating circle lays out its circumference on the base line; "
                      "the step between positions is 2 pi r / n.")},
         {"name": tr("Epicycloid and hypocycloid"),
          "f": "base circle radius R, generating circle radius r",
          "terms": tr("Rolling outside the base circle gives an epicycloid, rolling inside gives a "
                      "hypocycloid; with r = R / 4 the hypocycloid is four straight lines.")},
         {"name": tr("Involute of a circle"),
          "f": "tangent length at step k = k x 2 pi r / n",
          "terms": tr("The length grows by one n-th of the circumference at each step; after one "
                      "full turn it is 2 pi r.")},
         {"name": tr("Archimedean spiral"),
          "f": "r = a x theta,  pitch = R / number of turns",
          "terms": tr("The radius grows by the same amount at every equal angle, so a 60 mm spiral "
                      "over 1.5 turns has a 40 mm pitch.")},
     ]},
    {"title": tr("Tangent and normal rules"),
     "items": [
         {"name": tr("Ellipse"),
          "f": "tangent bisects the external angle between the focal distances",
          "terms": tr("Join the point to both foci and bisect the outer angle; the normal bisects the "
                      "inner angle.")},
         {"name": tr("Parabola"),
          "f": "make V the midpoint of M T, then T P is the tangent",
          "terms": tr("M is the foot of the perpendicular from P to the axis and V the vertex; the "
                      "tangent bisects the angle between the focal distance and the axis.")},
         {"name": tr("Hyperbola"),
          "f": "tangent bisects the angle between one focal distance and the other produced",
          "terms": tr("The mirror image of the ellipse rule, and the normal bisects the angle "
                      "between the two focal distances.")},
         {"name": tr("Cycloid"),
          "f": "normal passes through the instantaneous centre on the base line",
          "terms": tr("Join the point on the curve to the point of contact of the generating circle "
                      "with the base line; the tangent is perpendicular to it.")},
         {"name": tr("Involute"),
          "f": "normal is the tangent to the base circle",
          "terms": tr("The unwound string is always taut, so it is always normal to the curve.")},
     ]},
]

VIVA = [
    {"title": tr("Conics"),
     "items": [
         {"q": tr("What is eccentricity and why does it decide the curve?"),
          "a": tr("It is the ratio of the distance of a point from the focus to its distance from the "
                  "directrix, and it is constant for a given conic. Below 1 the curve closes into an "
                  "ellipse, at exactly 1 it stays open as a parabola, and above 1 it opens into two "
                  "branches, a hyperbola. Because the ratio is fixed, one construction serves all "
                  "three curves.")},
         {"q": tr("How do you get the three conics from a cone?"),
          "a": tr("Cut a right circular cone by a plane. A plane parallel to the base gives a circle, "
                  "a plane tilted to the axis and cutting one nappe gives an ellipse, a plane parallel "
                  "to a generator gives a parabola, and a plane steeper than the generator, cutting "
                  "both nappes, gives a hyperbola with two branches.")},
         {"q": tr("Name two applications each of an ellipse, a parabola and a hyperbola."),
          "a": tr("Ellipse: gear blanks and elliptical arches, and the whispering gallery whose two "
                  "foci carry sound across the room. Parabola: the headlamp reflector that throws a "
                  "parallel beam, and the suspension bridge cable. Hyperbola: the cooling tower shell "
                  "and the Loran navigation chart, where a constant difference of distances is "
                  "measured.")},
         {"q": tr("Why is the focal sum a good check on a finished ellipse?"),
          "a": tr("Because for every point of an ellipse the sum of its distances from the two foci "
                  "equals the major axis. Setting a divider to the major axis and testing two or "
                  "three points catches a curve that has been drawn through a wrong projection point, "
                  "which is the commonest error in the concentric-circle method.")},
     ]},
    {"title": tr("Construction methods"),
     "items": [
         {"q": tr("Explain the concentric-circle method in one sentence."),
          "a": tr("Draw the major and minor circles about the same centre, divide the major circle "
                  "into equal angles, and for each ray the vertical from the major circle and the "
                  "horizontal from the minor circle meet on the ellipse.")},
         {"q": tr("Why is the rectangle method used for a parabola?"),
          "a": tr("Because a parabola is given in the exam by its base and its height, and the "
                  "rectangle built on those two dimensions supplies all the divisions at once: rays "
                  "from one base corner and parallels to the axis intersect exactly on the curve. No "
                  "focus and no directrix have to be found first.")},
         {"q": tr("How do you draw a tangent at a point on a parabola?"),
          "a": tr("Drop a perpendicular from the point to the axis to get M, mark T on the axis so "
                  "that the vertex is the midpoint of M T, and join T to the point - that is the "
                  "tangent. The normal is perpendicular to it at the point.")},
         {"q": tr("What is special about a rectangular hyperbola?"),
          "a": tr("Its asymptotes are at right angles and the product of the distances of any point "
                  "from them is constant, x times y = a squared. That makes it the only conic that can "
                  "be set out entirely from a table of numbers with a scale, without any projection "
                  "lines.")},
     ]},
    {"title": tr("Cycloidal curves, involutes and spirals"),
     "items": [
         {"q": tr("What is the length of the base line of a cycloid?"),
          "a": tr("One turn of the generating circle lays its circumference along the base, so the "
                  "base is 2 pi r. For a circle of 25 mm radius it is 157 mm, and the height of the "
                  "curve is 2 r = 50 mm.")},
         {"q": tr("What is the difference between a cycloid, an epicycloid and a hypocycloid?"),
          "a": tr("A cycloid rolls on a straight line, an epicycloid rolls on the outside of a base "
                  "circle, and a hypocycloid rolls inside a base circle. All three trace a point on "
                  "the generating circle, and all three are used for gear tooth profiles.")},
         {"q": tr("How is the normal to a cycloid found?"),
          "a": tr("Through the instantaneous centre - the point where the generating circle in that "
                  "position touches the base line. Joining that point of contact to the point on the "
                  "curve gives the normal, and the tangent is drawn perpendicular to it.")},
         {"q": tr("What is an involute and where is it used?"),
          "a": tr("The path of a point on a taut string as it unwinds from a circle or a polygon. It "
                  "is used for gear tooth flanks because two involute teeth keep a constant pressure "
                  "angle, so the drive is smooth and a small error in the centre distance does not "
                  "change the velocity ratio.")},
         {"q": tr("How is an Archimedean spiral constructed?"),
          "a": tr("Draw the largest circle for the number of turns required and divide it into twelve "
                  "or more equal angles; divide one radius into the same number of parts; set off one "
                  "part on the first ray, two on the second and so on; the twelve marks joined with a "
                  "French curve give the spiral, whose pitch is the growth per turn.")},
         {"q": tr("Why must the number of divisions on the circle equal the number on the base line?"),
          "a": tr("Because each position of the rolling circle is paired with one division of the "
                  "base - point n on the circle with position n on the line. If the counts differ, "
                  "the parallel from a division point has no matching circle to meet, and the curve "
                  "is drawn through the wrong intersections.")},
     ]},
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
