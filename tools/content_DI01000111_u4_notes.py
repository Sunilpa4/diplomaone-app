"""DI01000111 Engineering Graphics - Unit 4: Projections of Planes.

GTU 4.1, 4 h, 10 %, 7 marks, CO3. English only. Square, hexagonal and circular planes in every
position, each as a numbered construction: which view is the edge, which is the apparent shape, and
how much each dimension is shortened.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_DI01000111_u1_notes import (tr, p, h4, ul, ol, table, steps, why, check, pit,  # noqa
                                        card)

SOURCES = [
    ("GTU DI01000111 Engineering Graphics syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("N. D. Bhatt - Elementary Engineering Drawing, Charotar Publishing House, Anand (chapter 11: "
     "projections of planes)", "https://www.charotarbookstall.com/"),
    ("P. S. Gill - A Text Book of Engineering Drawing, S. K. Kataria & Sons, Delhi (planes inclined "
     "to one and to both reference planes)", "https://www.skkatariaandsons.com/"),
    ("BIS SP 46 - Engineering drawing practice: apparent shape and edge view",
     "https://www.bis.gov.in/"),
]

NOTES = [
    {"title": tr("1. How a Plane Looks in the Two Views"),
     "items": [
         card("4.1 Edge view or true shape - the one rule of this unit",
              h4("A plane is shown by its boundary")
              + p("A square, a hexagon or a circle is drawn as what it is, a flat area, and the two "
                  "views are the boundary seen from the front and from above. The whole unit rests on "
                  "one rule: <b>a plane parallel to a reference plane is seen in its true shape in "
                  "that view, and as a straight edge in the other view</b>.")
              + table(["position of the plane", "elevation", "plan"], [
                  ("parallel to HP", "edge, parallel to XY", "true shape"),
                  ("parallel to VP", "true shape", "edge, parallel to XY"),
                  ("perpendicular to both HP and VP", "edge, square to XY", "edge, square to XY"),
                  ("perpendicular to VP, inclined to HP", "edge at the true angle",
                   "apparent shape"),
                  ("perpendicular to HP, inclined to VP", "apparent shape",
                   "edge at the true angle"),
                  ("inclined to both HP and VP", "apparent shape", "apparent shape"),
              ])
              + steps("Draw XY and decide, from the words of the question, which reference plane the "
                      "plane is parallel or perpendicular to.",
                      "Draw the view that shows the edge first - that is the view of the plane the "
                      "surface is perpendicular to - as one straight line.",
                      "Project every corner from the edge view into the other view with thin "
                      "projectors square to XY.",
                      "Complete the apparent shape by setting off the dimension along the hinge "
                      "line true and the dimension across it multiplied by the cosine of the angle.",
                      "Ink the two views, keep the projectors and the hinge line thin, and write "
                      "the two dimensions beside the apparent shape.")
              + h4("The three words you will use")
              + ul("<b>Edge view</b> - the view in which the plane collapses to a line; it appears "
                   "in the view of the plane the surface is perpendicular to.",
                   "<b>True shape</b> - the outline with no foreshortening, seen only when the plane "
                   "is parallel to that reference plane.",
                   "<b>Apparent shape</b> - the foreshortened outline: one dimension true, the other "
                   "multiplied by the cosine of the angle of tilt.")
              + why("A plane has no thickness, so a line of sight lying in the plane sees the whole "
                    "surface as its own edge; a line of sight square to the plane sees the surface "
                    "without foreshortening. Those two directions are the two reference planes.")
              + pit("Drawing the apparent shape with both dimensions true. Only the dimension "
                    "parallel to the hinge (the line where the plane meets the reference plane) keeps "
                    "its full size."),
              diagram="u4_basic", syllabus_item="4.1"),

         card("4.1 Square plane perpendicular to VP, inclined to HP",
              h4("Square ABCD, side 50 mm, 40 degrees to HP, side AB in HP")
              + p("The plane is perpendicular to VP, so the VP looks along it and the "
                  "<b>elevation is the edge</b>. The plane rises at 40 degrees, so the edge is drawn "
                  "at 40 degrees to XY, and the side that lies in the plane and faces VP is seen "
                  "there at its true length of 50 mm.")
              + steps("Draw XY. Put a' and b' on XY, because A and B lie in HP and a point in HP has "
                      "its elevation on XY; they share one point because AB is square to VP.",
                      "From that point draw the edge a'd' 50 mm long at 40 degrees to XY - this single "
                      "line is the whole elevation.",
                      "Project a' and d' down to the plan with thin lines square to XY.",
                      "Set A 20 mm in front of VP on its projector; that fixes the plan's position "
                      "below XY.",
                      "From a set off 50 cos 40 = 38.3 mm along XY to reach d, and 50 mm square to XY "
                      "to reach b - the side AB has no tilt, so it keeps its 50 mm.",
                      "Complete the rectangle a b c d, ink it, and check that its sides are 50 mm "
                      "across the depth and 38.3 mm along XY.")
              + h4("Numbers to write on the drawing")
              + ul("Edge view: 50 mm at 40 degrees to XY, and the far corners stand "
                   "50 sin 40 = 32.1 mm above HP.",
                   "Plan: 50 mm square to XY (true) and 38.3 mm along XY (shortened).",
                   "Every corner keeps the depth it had in the edge view, so the plan's depth side "
                   "is parallel to XY.",
                   "The area of the plan is 38.3 / 50 = 76.6 per cent of the true area, the cosine "
                   "of the angle.")
              + why("A tilt about a horizontal hinge cannot change any distance measured along the "
                    "hinge, so that dimension stays true; the dimension measured across the hinge is "
                    "foreshortened by the cosine of the tilt. The elevation holds the edge, so the "
                    "tilt itself is drawn true.")
              + pit("Putting the edge in the plan. The edge belongs to the view of the plane the "
                    "surface is perpendicular to - here VP, so the elevation."),
              diagram="u4_edge_vp", syllabus_item="4.1"),

         card("4.1 Hexagonal plane perpendicular to HP, inclined to VP",
              h4("Regular hexagon, 30 mm side, 45 degrees to VP")
              + p("Now the plane is perpendicular to HP, so HP looks along it and the <b>plan is the "
                  "edge</b>, drawn at 45 degrees to XY. The elevation is the apparent hexagon: the "
                  "width across the corners parallel to the hinge stays 60 mm, and the other "
                  "dimension is multiplied by cos 45.")
              + steps("Draw the true hexagon first on a scrap of the sheet, or draw XY and keep the "
                      "hexagon's centre and its 30 mm radius in mind: side 30 mm means "
                      "circumradius 30 mm, across corners 60 mm, across flats 51.96 mm.",
                      "In the plan draw the edge as one line at 45 degrees to XY, long enough to "
                      "carry the 60 mm across corners.",
                      "Mark the six corners on that edge line at their true distances, measured "
                      "along the edge from the corner nearest VP.",
                      "Project each corner up, square to XY.",
                      "In the elevation set each corner's height at its true distance from the "
                      "hinge line multiplied by cos 45 = 0.707: the 30 mm apothem becomes 21.2 mm, "
                      "so the apparent hexagon is 42.4 mm wide and 52 mm from flat to flat.",
                      "Join the six points and ink the apparent hexagon, leaving the edge and the "
                      "projectors thin.")
              + h4("Sizes to predict")
              + table(["dimension", "true hexagon", "apparent hexagon at 45 deg"], [
                  ("across corners", "60 mm", "60 mm (parallel to the hinge)"),
                  ("across flats", "51.96 mm", "51.96 mm (parallel to the hinge)"),
                  ("thickness across the hinge", "60 mm", "60 cos 45 = 42.4 mm"),
              ])
              + why("The hexagon is a polygon like any other: the tilt squeezes one direction only, "
                    "and because the tilt is about a line parallel to XY that direction is measured "
                    "square to the hinge. Every vertex moves towards the hinge line by the same "
                    "factor, so the sides parallel to the hinge keep their length and the rest "
                    "shorten in proportion.")
              + pit("Using cos 45 on every dimension. Anything measured along the hinge is unchanged; "
                    "only the distance from the hinge shortens."),
              diagram="u4_edge_hp", syllabus_item="4.1"),

         card("4.1 Circular plane inclined to HP - the ellipse",
              h4("Circle of 60 mm diameter, perpendicular to VP, 30 degrees to HP")
              + p("A circle has no corners to project, so the apparent shape is built point by point: "
                  "divide the circle, project each division to the other view and set its distance "
                  "from the hinge off at cos 30. The result is an <b>ellipse</b> with the major axis "
                  "equal to the diameter, 60 mm, and the minor axis 60 cos 30 = 51.96 mm.")
              + steps("Draw XY and the elevation as the edge: a line 60 mm long at 30 degrees to XY, "
                      "the elevation of the diameter that faces VP.",
                      "Divide the diameter in the plan, or divide a semicircle, into twelve equal "
                      "parts and draw ordinates to the circle.",
                      "Project each ordinate up to the edge view: every point of the circle lies on "
                      "one of these projectors.",
                      "In the plan, set each point's distance from the hinge line off at "
                      "d cos 30 from the line through the centre, on both sides.",
                      "Join the points with a French curve: the ellipse 60 mm by 52 mm, with the "
                      "60 mm axis along the hinge and the 52 mm axis square to it.")
              + h4("Predicting the apparent shape")
              + table(["true shape", "apparent shape at angle t to the other plane"], [
                  ("circle of diameter d", "ellipse d x d cos t"),
                  ("square of side a", "rectangle a x a cos t"),
                  ("hexagon across corners 2R", "hexagon squeezed to 2R cos t across the hinge"),
                  ("any shape", "same shape with one dimension multiplied by cos t"),
              ])
              + why("Every point of the circle is at a different height, and the plan shows the "
                    "height only through the foreshortened ordinate. The longest ordinate is the "
                    "diameter square to the hinge and it shortens by cos t, which is exactly what "
                    "makes the ellipse.")
              + check("The plan's long axis must equal the true diameter and must lie parallel to "
                      "the hinge; the short axis is the cosine-shrunk one. If the ellipse is longer "
                      "than 60 mm anywhere, a distance was measured from the wrong line.")
              + pit("Drawing a circle in the plan because the object is a circle. The plan shows what "
                    "the eye sees from above, and at 30 degrees that is an ellipse."),
              diagram="u4_circle", syllabus_item="4.1"),

         card("4.1 Plane inclined to both HP and VP - the two-stage method",
              h4("Square 50 mm, 45 degrees to HP and 30 degrees to VP")
              + p("When the plane is inclined to both reference planes, neither view can be the edge "
                  "and neither can be the true shape, so the drawing is made in two stages, exactly "
                  "as a line is: <b>stage 1</b> makes the plane perpendicular to VP so that the edge "
                  "shows in the elevation, and <b>stage 2</b> swings the plan to the second angle, "
                  "reading the final elevation off the locus lines.")
              + steps("Draw XY and, in the elevation, the edge of the square at 45 degrees to XY with "
                      "the side 50 mm long.",
                      "Project down and complete the intermediate plan: 50 mm across the depth, "
                      "50 cos 45 = 35.4 mm along XY - this plan is the apparent shape for the first "
                      "angle only.",
                      "Stage 2: with the corner on the hinge as centre, swing the whole intermediate "
                      "plan through 30 degrees, so that the side which was parallel to XY now makes "
                      "30 degrees with XY.",
                      "Draw the locus lines: horizontals through each corner of the stage-1 "
                      "elevation, because a swing about a vertical axis cannot change a height.",
                      "Raise projectors from the swung plan and cut the loci to get the final "
                      "elevation.",
                      "Ink the final plan and the final elevation and leave stage 1, the swing and "
                      "the loci thin and dashed.")
              + h4("What is preserved at each stage")
              + table(["quantity", "stage 1", "after the swing"], [
                  ("length of a side", "true, 50 mm", "true, unchanged by the swing"),
                  ("height of each corner", "50 sin 45 = 35.4 mm", "unchanged - the swing is about a "
                   "vertical axis"),
                  ("dimension along XY", "35.4 mm", "35.4 cos 30 = 30.6 mm"),
                  ("dimension across the depth", "50 mm", "50 cos 30 with the 35.4 kept"),
              ])
              + why("The two stages separate the two tilts. Stage 1 tilts the plane about a hinge in "
                    "HP, which changes heights and leaves the along-XY dimension honest; stage 2 "
                    "rotates about a vertical axis, which changes depths and leaves every height "
                    "exactly where stage 1 put it.")
              + check("Each final corner must sit on its own horizontal locus, at the same height as "
                      "the corner in stage 1. If a corner has moved up or down, the swing was made "
                      "about a sloping axis instead of a vertical one.")
              + pit("Swinging the plan before the edge view is complete. Finish stage 1 first: an "
                    "edge view with the true angle is the only reliable start for a plane inclined "
                    "to both planes."),
              diagram="u4_both", syllabus_item="4.1"),
     ]},
]

_PRACTICE = [
    ("A square plane ABCD of side 50 mm is perpendicular to VP and inclined at 40 degrees to HP. The "
     "side AB lies in HP and A is 20 mm in front of VP. Draw its projections and state the size of "
     "the plan.", 5,
     [h4("Given")
      + p("Perpendicular to VP gives the edge in the elevation; inclined 40 degrees gives that edge "
          "at 40 degrees to XY; the side AB in HP puts the elevations of A and B on XY."),
      h4("Construction, step by step")
      + ol("Draw XY and mark a' and b' together on XY, since A and B are in HP and AB is square "
           "to VP.",
           "Draw a'd' 50 mm at 40 degrees to XY - the edge view and the whole elevation.",
           "Project a' and d' down, square to XY.",
           "Set a 20 mm below XY (A is 20 mm in front of VP) and mark d on the same level, "
           "50 cos 40 = 38.3 mm along XY from a.",
           "From a set off 50 mm square to XY to get b, and complete c opposite d.",
           "Ink the rectangle a b c d and check the sides: 50 mm across the depth, 38.3 mm along XY."),
      h4("The answer")
      + p("The plan is a rectangle 50 mm by 38.3 mm; the elevation is the single edge line 50 mm "
          "long at 40 degrees, with the corners d' and c' standing 50 sin 40 = 32.1 mm above HP.")]),

    ("A circular plate of 60 mm diameter is perpendicular to VP and inclined at 30 degrees to HP. "
     "Draw its projections and state the axes of the apparent shape.", 5,
     [h4("Given")
      + p("The edge is in the elevation, 60 mm long at 30 degrees to XY; the plan is the apparent "
          "shape, an ellipse."),
      h4("Construction, step by step")
      + ol("Draw XY and the edge view 60 mm long at 30 degrees, one end on XY.",
           "Divide the diameter into twelve equal parts and draw the ordinates.",
           "Project every ordinate up to the edge view, square to XY.",
           "Project each point down into the plan and set its depth off at d cos 30 from the centre "
           "line.",
           "Join the twelve points with a French curve, on both sides of the long axis."),
      h4("The answer")
      + p("An ellipse with its major axis 60 mm along the hinge and its minor axis "
          "60 cos 30 = 51.96 mm square to it. The area is 0.866 of the true circle, the cosine of "
          "30 degrees.")]),

    ("A rectangular plate 60 mm by 40 mm is perpendicular to HP and inclined at 35 degrees to VP. "
     "Draw its projections and state the sizes of both views.", 5,
     [h4("Given")
      + p("Perpendicular to HP puts the edge in the plan at 35 degrees to XY; the elevation is the "
          "apparent shape with the 40 mm side foreshortened."),
      h4("Construction, step by step")
      + ol("Draw XY and, below it, the edge as a line 60 mm long at 35 degrees to XY.",
           "Mark the two ends of the 40 mm side on that edge line at their true position.",
           "Project the four corners up, square to XY.",
           "In the elevation set the heights: the 40 mm side shortens to 40 cos 35 = 32.8 mm, while "
           "the 60 mm side stays 60 mm.",
           "Complete the rectangle a' b' c' d' and ink it."),
      h4("The answer")
      + p("Plan: the edge, 60 mm at 35 degrees. Elevation: a rectangle 60 mm by 32.8 mm. Check that "
          "the 60 mm side is the one parallel to the hinge, which is the side that never shortens.")]),

    ("An equilateral triangle of 50 mm side is perpendicular to VP and inclined at 45 degrees to HP, "
     "with one side in HP. Draw its projections and state the apparent height.", 5,
     [h4("Given")
      + p("The edge is in the elevation; the plan is the apparent triangle with its height "
          "foreshortened and its base true."),
      h4("Construction, step by step")
      + ol("Draw XY and, above it, the edge at 45 degrees to XY with the side that faces VP drawn "
           "true.",
           "Project the three corners down, square to XY.",
           "Keep the base 50 mm as it is, because the base lies along the hinge.",
           "Reduce the height by cos 45: the true height is 50 sin 60 = 43.3 mm, so the apparent "
           "height is 43.3 x 0.707 = 30.6 mm.",
           "Join the three points to complete the apparent triangle and ink it."),
      h4("The answer")
      + p("Plan: a triangle of base 50 mm and height 30.6 mm; elevation: the edge at 45 degrees. The "
          "true area is halved by the 45 degree tilt, because cos 45 = 0.707 and the area follows the "
          "same factor.")]),

    ("A regular hexagonal plate of 30 mm side is perpendicular to HP and inclined at 45 degrees to "
     "VP. Draw its projections and give the sizes of the apparent hexagon.", 6,
     [h4("Given")
      + p("The plan is the edge at 45 degrees; the elevation is the apparent hexagon, squeezed square "
          "to the hinge."),
      h4("Construction, step by step")
      + ol("Work out the true hexagon first: side 30 mm, circumradius 30 mm, across corners 60 mm, "
           "apothem 30 cos 30 = 25.98 mm and across flats 51.96 mm.",
           "Draw XY and the edge in the plan at 45 degrees to XY, 60 mm long.",
           "Mark the six corners on the edge line at their true distances from the first corner.",
           "Project all six up, square to XY.",
           "In the elevation set the heights using cos 45 = 0.707 on every distance from the hinge: "
           "42.4 mm across the hinge instead of 60 mm, and 18.4 mm instead of the 25.98 mm apothem.",
           "Join the six points and ink the apparent hexagon."),
      h4("The answer")
      + p("Plan: the edge, 60 mm at 45 degrees. Elevation: a hexagon 60 mm across the corners "
          "parallel to the hinge and 42.4 mm across the corners square to it, with the flats 36.8 mm "
          "apart. Both views are drawn with thin projectors and the hinge left as a construction "
          "line.")]),

    ("A square plane of 50 mm side has one corner in HP and is inclined at 45 degrees to HP and 30 "
     "degrees to VP. Draw its projections by the two-stage method.", 6,
     [h4("Given")
      + p("Inclined to both planes, so neither view is an edge: stage 1 puts the edge in the "
          "elevation at 45 degrees, stage 2 swings the plan through 30 degrees."),
      h4("Construction, step by step")
      + ol("Draw XY and, in the elevation, the edge of the square at 45 degrees to XY with the side "
           "50 mm, one end on XY.",
           "Project down and complete the intermediate plan: 50 mm across the depth and "
           "50 cos 45 = 35.4 mm along XY.",
           "Check the intermediate plan: it is the apparent shape for 45 degrees only.",
           "Stage 2: with the corner on XY as centre, swing the whole plan through 30 degrees so "
           "that the side that was along XY now makes 30 degrees with it.",
           "Draw horizontal loci through the stage-1 elevations of the corners.",
           "Raise projectors from the swung plan and cut the loci; join the four points for the final "
           "elevation and ink both final views."),
      h4("The answers")
      + p("Final plan: sides 50 mm and 35.4 mm, the long side at 30 degrees to XY, one corner on the "
          "hinge. Final elevation: a parallelogram whose corners stand 0, 35.4, 35.4 and 0 mm above "
          "HP, because the swing about a vertical axis kept every height. The dimension along XY "
          "falls to 35.4 cos 30 = 30.6 mm in the final plan.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)

EQUATIONS = [
    {"title": tr("Foreshortening in an apparent shape"), "items": [
        {"name": tr("Dimension across the hinge"),
         "f": "apparent = true x cos(angle of tilt)",
         "terms": tr("The dimension measured square to the hinge line shortens by the cosine of the "
                     "angle the plane makes with the reference plane; the dimension along the hinge "
                     "is unchanged.")},
        {"name": tr("Edge view length"), "f": "edge = true length of the side that faces the plane",
         "terms": tr("In the edge view the plane collapses to a line, but that line still carries "
                     "the true length of the side lying in it, so it is drawn at full size at the "
                     "true angle to XY.")},
        {"name": tr("Height of a corner above HP"), "f": "h = L sin(angle to HP)",
         "terms": tr("A corner at distance L from the hinge rises L sin of the tilt, which is the "
                     "distance of its elevation from XY.")},
    ]},
    {"title": tr("The three shapes of the syllabus"), "items": [
        {"name": tr("Square, side a, tilted t"), "f": "plan a x a cos(t)",
         "terms": tr("The side parallel to the hinge stays a, the side square to it becomes a cos t, "
                     "so the plan is always a rectangle.")},
        {"name": tr("Hexagon, side s, tilted t"),
         "f": "across corners 2s, across hinge 2s cos(t)",
         "terms": tr("Circumradius equals the side, so the across-corners dimension is 2s and the "
                     "apothem 0.866 s; only the dimension square to the hinge shortens.")},
        {"name": tr("Circle, diameter d, tilted t"), "f": "ellipse d x d cos(t)",
         "terms": tr("The diameter along the hinge is the major axis and the diameter square to it is "
                     "the minor axis d cos t, which is why a tilted circle draws as an ellipse.")},
        {"name": tr("Area of an apparent shape"), "f": "apparent area = true area x cos(t)",
         "terms": tr("Every element of the area is foreshortened by the same factor, so the whole "
                     "area follows the cosine - a useful check on a finished drawing.")},
    ]},
]

VIVA = [
    {"title": tr("Edge view and apparent shape"), "items": [
        {"q": tr("When does a plane appear as a straight line in a view?"),
         "a": tr("When the plane is perpendicular to the reference plane of that view, because the "
                 "line of sight then lies in the surface and the whole area collapses on to its own "
                 "edge. That line is called the edge view.")},
        {"q": tr("When does a view show the true shape of a plane?"),
         "a": tr("Only when the plane is parallel to the reference plane of that view, because then "
                 "the line of sight is square to the surface and nothing is foreshortened. In any "
                 "other position the outline is the apparent shape.")},
        {"q": tr("What is the apparent shape and how is it calculated?"),
         "a": tr("The outline a tilted plane presents: the dimension parallel to the hinge line stays "
                 "true and the dimension square to the hinge is multiplied by the cosine of the angle "
                 "of tilt. The area likewise falls to the true area times that cosine.")},
        {"q": tr("Which view carries the edge when the plane is perpendicular to VP?"),
         "a": tr("The elevation, because VP is the plane the surface is perpendicular to, so the "
                 "elevation looks along the plane and shows it as a line at the true angle of tilt. "
                 "The plan is then the apparent shape.")},
    ]},
    {"title": tr("Square, hexagon and circle"), "items": [
        {"q": tr("A square of 50 mm side is tilted 40 degrees to HP. What size is the plan?"),
         "a": tr("A rectangle 50 mm by 50 cos 40 = 38.3 mm, with the 50 mm side along the hinge. The "
                 "tilt only shortens the dimension square to the hinge.")},
        {"q": tr("Why does a circle appear as an ellipse in the plan?"),
         "a": tr("Because each diameter is foreshortened according to its direction: the diameter "
                 "parallel to the hinge keeps its length and becomes the major axis, while the "
                 "diameter square to the hinge shortens to d cos t and becomes the minor axis.")},
        {"q": tr("A hexagon of 30 mm side has circumradius 30 mm. What is its across-flats size?"),
         "a": tr("Twice the apothem: 2 x 30 cos 30 = 51.96 mm, while the across-corners size is "
                 "2 x 30 = 60 mm. Those two dimensions are the ones quoted in the apparent shape.")},
        {"q": tr("How do you start a problem where the plane is inclined to both reference planes?"),
         "a": tr("With the two-stage method. Stage 1 makes the plane perpendicular to VP so the edge "
                 "appears in the elevation at the first angle; stage 2 swings the plan about a "
                 "vertical axis through the second angle and the final elevation is read off the "
                 "locus lines.")},
        {"q": tr("What must not change during the second stage?"),
         "a": tr("The heights of the corners, because the swing is about a vertical axis. That is why "
                 "each corner keeps its own horizontal locus and the new elevation is found where the "
                 "projector from the swung plan cuts that locus.")},
        {"q": tr("What check proves a finished plane drawing?"),
         "a": tr("Every corner must lie on its projector, each view must be the same size in the "
                 "dimension along the hinge, and the foreshortened dimension must come out as the "
                 "true dimension times the cosine of the tilt.")},
        {"q": tr("What is the hinge line of a tilted plane?"),
         "a": tr("The line in which the plane meets the reference plane it is tilted about - in these "
                 "problems the line where the surface cuts HP or VP. Every distance measured along "
                 "that line is unaffected by the tilt, which is why it is the one dimension that "
                 "stays true in the apparent shape.")},
        {"q": tr("Why is the edge view drawn at the angle given to the other plane?"),
         "a": tr("Because the view perpendicular to the plane shows the surface edge-on, and the line "
                 "of that edge is the surface seen from the side: its slope is exactly the angle the "
                 "surface makes with the reference plane, so a 40 degree plane draws a 40 degree "
                 "edge.")},
        {"q": tr("What happens when a plane is perpendicular to both HP and VP?"),
         "a": tr("Both views are edges and both are square to XY: the plane stands on the ground like "
                 "a fence at right angles to the vertical plane, so neither view can see any part of "
                 "its area, and no dimension appears in its true size except along the edge itself.")},
        {"q": tr("How would you find the true shape of a plane from an inclined drawing?"),
         "a": tr("By the auxiliary plane method: draw a new reference line parallel to the edge view, "
                 "project the corners square to it and set each corner's distance off from the edge "
                 "line in that new view. The result is the true shape, and the same view gives the "
                 "true angle of tilt.")},
    ]},
]
