"""DI01000111 Engineering Graphics - Unit 5: Orthographic Projections.

GTU 5.1-5.3, 6 h, 20 %, 14 marks, CO4. English only. Objects are read from a pictorial view and
drawn as front, top and side views in first angle, plus the free-hand sketches the syllabus names.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_DI01000111_u1_notes import (tr, p, h4, ul, ol, table, steps, why, check, pit,  # noqa
                                        card)

SOURCES = [
    ("GTU DI01000111 Engineering Graphics syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("N. D. Bhatt - Elementary Engineering Drawing, Charotar Publishing House, Anand (chapters 7-8: "
     "orthographic projections, first and third angle)", "https://www.charotarbookstall.com/"),
    ("P. S. Gill - A Text Book of Engineering Drawing, S. K. Kataria & Sons, Delhi (reading a "
     "pictorial view and drawing the three views)", "https://www.skkatariaandsons.com/"),
    ("BIS SP 46 - Engineering drawing practice: layout of views, hidden detail, centre lines",
     "https://www.bis.gov.in/"),
]

NOTES = [
    {"title": tr("1. From the Pictorial View to the Three Views"),
     "items": [
         card("5.1 First angle: what the three views are and where they go",
              h4("The object is placed between you and the paper")
              + p("In <b>first-angle projection</b> the object stands between the observer and the "
                  "plane of projection, so every view lands on the far side of the object. Open the "
                  "box out and the three views sit like this: the <b>front view</b> (elevation) in "
                  "the middle, the <b>top view</b> (plan) directly <b>below</b> it, and the "
                  "<b>side view</b> taken from the left, placed directly to the <b>right</b>.")
              + table(["view", "what it shows", "where it is placed"], [
                  ("front view", "width and height, as seen from the front", "centre"),
                  ("top view", "width and depth, as seen from above", "below the front view"),
                  ("side view", "depth and height, as seen from the left", "right of the front view"),
              ])
              + steps("Decide the front view first. Choose the direction that shows the most shape "
                      "and the fewest hidden lines, and call it the front.",
                      "Draw the front view in the middle of the sheet, leaving room below and to the "
                      "right for the other two views.",
                      "Project down from every corner of the front view with thin lines square to "
                      "the base line, and draw the top view between them.",
                      "Project across from the front view to the right, and carry each depth round "
                      "from the top view with a 45 degree mitre line, to draw the side view.",
                      "Check the three views: height the same in the front and the side, width the "
                      "same in the front and the top, depth the same in the top and the side.")
              + h4("Lines and what they mean")
              + ul("<b>Visible outline</b> - a continuous thick line: an edge you can see.",
                   "<b>Hidden edge</b> - a dashed line of the same thickness: an edge behind "
                   "material.",
                   "<b>Centre line</b> - a thin chain line through the axis of a hole or a cylinder.",
                   "No view is ever drawn on top of another, and no dimension is repeated in two "
                   "views.")
              + why("The three views are three directions of looking at one object, so each pair "
                    "must agree in the dimension they share. That agreement is not decoration - it is "
                    "the proof that the views describe one solid.")
              + pit("Placing the top view above the front view. That is third angle; in first angle "
                    "the top view goes below and the left side view goes on the right."),
              diagram="u5_layout", syllabus_item="5.2"),

         card("5.1 Reading a pictorial view - the three shapes in this unit",
              h4("A stepped block: 60 wide, 40 deep, 40 high")
              + p("Read the pictorial view as a set of boxes. This object is a base plate 60 x 40 x 15 "
                  "with an upright 20 x 40 x 25 standing on its left end. Its three views come out as "
                  "one L, one rectangle divided in two, and one rectangle with a hidden line.")
              + steps("Box the object in: write down the overall width, depth and height from the "
                      "pictorial view - here 60, 40 and 40.",
                      "Decide the front direction and list what you see from there: a base 60 wide and "
                      "15 high, and an upright 20 wide and 25 high on the left, so the front view is an "
                      "L.",
                      "Look from above: the plate 60 x 40 with a visible line across it at 20 from the "
                      "left end, where the upright's face meets the plate, so the top view is a 60 x 40 "
                      "rectangle divided into 20 and 40.",
                      "Look from the left: the upright face 40 wide by 40 high on the near side, and "
                      "the top of the plate hidden behind it - so the side view is a 40 x 40 square "
                      "with a dashed line 15 up from the base.",
                      "Place the front view, project to the top view below and the side view to the "
                      "right, and check the three shared dimensions before inking.")
              + h4("Shapes that always draw the same way")
              + table(["solid", "front view", "top view", "side view"], [
                  ("rectangular block", "rectangle", "rectangle", "rectangle"),
                  ("cylinder standing", "rectangle", "circle", "rectangle"),
                  ("cylinder lying", "rectangle", "rectangle", "circle"),
                  ("cone standing", "triangle", "circle with a centre dot", "triangle"),
                  ("prism standing", "rectangle", "regular polygon", "rectangle"),
              ])
              + why("An object made of prisms and cylinders has views made of rectangles, circles and "
                    "polygons only. Once you can name the three views in words, the drawing is just "
                    "the sizes put in the right places.")
              + check("Count the corners in the pictorial view and the corners in each of your views; "
                      "every visible edge of the object must appear in at least one view, thick or "
                      "dashed.")
              + pit("Drawing the top view 60 wide and 40 deep but the side view 60 deep. The side view "
                    "shows the depth, and the depth of this block is 40."),
              diagram="u5_stepped", syllabus_item="5.1"),

         card("5.2 Objects of revolution: cylinder, cone and hole",
              h4("A cylinder of 40 mm diameter and 50 mm height standing on HP")
              + p("A circular edge is a circle when seen square-on, a straight line when seen edge-on, "
                  "and an ellipse when seen at an angle. So a standing cylinder gives a rectangle "
                  "40 x 50 in the front and side views and a circle of diameter 40 in the top view, "
                  "with a centre line through the axis in both rectangles.")
              + steps("Draw the top view first when the object is round: the circle of diameter 40 "
                      "with two centre lines crossing at its centre.",
                      "Project up from the two extreme generators of the circle to get the front "
                      "view, 40 wide.",
                      "Set the height 50 above the base line and close the rectangle 40 x 50.",
                      "Draw the axis as a thin chain line down the middle of the rectangle.",
                      "Repeat the front view at the side position, or project across from it - the "
                      "side view of a standing cylinder is the same rectangle.")
              + why("Every point of a circular edge is at the same distance from the axis, so the view "
                    "along the axis is a circle and the view across the axis is the same silhouette "
                    "as the extreme generators - a rectangle.")
              + pit("Drawing an ellipse in the side view of a standing cylinder. Side and front views "
                    "of a standing cylinder are identical rectangles; the ellipse appears only when "
                    "the axis is tilted to the line of sight."),
              diagram="u5_cylinder", syllabus_item="5.2"),

         card("5.2 A hole: a circle in one view, a dashed pair in the others",
              h4("A plate 60 x 40 x 15 with a 20 mm hole drilled vertically through it")
              + p("The hole removes material, and the edges of the material it removes are edges of the "
                  "object. From above you look straight down the hole and see a clean circle; from the "
                  "front and from the side the hole is behind the face of the plate, so its two sides "
                  "are drawn as <b>dashed vertical lines 20 mm apart</b>.")
              + steps("Draw the front view first: a rectangle 60 mm by 15 mm, with the base line as "
                      "the lowest edge.",
                      "Mark the two sides of the hole 20 mm apart, centred on the plate, and draw them "
                      "as thin chain-centre lines first so that they stay vertical.",
                      "Change those two lines to dashed lines running the full 15 mm thickness - the "
                      "hole passes right through the material.",
                      "Project down and draw the top view 60 x 40, with a solid circle of diameter 20 "
                      "at the centre and two thin chain centre lines crossing there.",
                      "Project across to the side view, 40 x 15, and repeat the two dashed lines in "
                      "the same relative position; check that all three views show the same 20 mm.")
              + h4("Line conventions you must apply")
              + ul("<b>Visible outline</b> - continuous thick: the edges of the plate.",
                   "<b>Hidden edge</b> - dashed, same thickness: the hole's sides in the front and side "
                   "views.",
                   "<b>Centre line</b> - thin chain line, extending a little past the outline: the "
                   "hole's axis in the top view and the centre of the hole in the other views.",
                   "Dashed lines start and end on the visible outline, and where they cross each other "
                   "the dash pattern continues.")
              + why("A hole is a circular edge seen along its axis in one view - a circle - and across "
                    "its axis in the others. Across the axis the two extreme points of the circle are "
                    "the only edges that show, and they are hidden behind the material.")
              + check("The circle's diameter and the distance between the two dashed lines must be the "
                      "same 20 mm; the dashed lines must stop at the top and bottom faces of the "
                      "plate, never run past them.")
              + pit("Drawing the hole as a solid circle in the front view. In a view where the material "
                    "is in front of the hole, only the hidden (dashed) lines are drawn."),
              diagram="u5_hidden", syllabus_item="5.2"),

         card("5.2 Hidden lines and the two-view problem",
              h4("Given two views, draw the third")
              + p("The examiner often gives the front and top views and asks for the side view. It is "
                  "built from two rules only: <b>every corner is projected across from the front view "
                  "and carried round from the top view</b>, and <b>every dimension already shown is "
                  "repeated, never invented</b>.")
              + steps("Draw the two given views in their correct relative positions and add the "
                      "projectors between them.",
                      "Take the height of every corner from the front view: draw light horizontals "
                      "across to the right, where the side view will stand.",
                      "Take the depth of every corner from the top view: carry each depth round with a "
                      "45 degree mitre line, or with a pair of dividers, to the side view position.",
                      "Mark where each height meets each depth - those are the corners of the side "
                      "view - and join them, thick where the edge is seen and dashed where it is "
                      "hidden.",
                      "Check that the side view's height equals the front view's height and its width "
                      "equals the top view's depth.")
              + h4("Lines you must not forget")
              + table(["line", "used for", "example here"], [
                  ("continuous thick", "visible outlines", "the L of the front view"),
                  ("dashed", "hidden edges", "the step hidden behind the upright in the side view"),
                  ("thin chain", "axes and centre lines", "the axis of a hole"),
                  ("thin continuous", "projectors and construction", "the lines joining the views"),
              ])
              + why("The side view is nothing but the same object seen from a third direction, so its "
                    "height must come out of the front view and its depth out of the top view. "
                    "Projecting the two sets of measurements on to one view is the whole method.")
              + check("Before inking, trace one corner round: height from the front, depth from the "
                      "top, and the point where they cross must be a corner in the side view. If any "
                      "corner is left over, a line is missing.")
              + pit("Inventing a dimension in the third view because the other two views did not "
                    "obviously supply it. Every size in the third view is already in the other two."),
              diagram="u5_missing", syllabus_item="5.2"),

         card("5.3 Free-hand sketches the syllabus asks for",
              h4("Square, triangle, circle, semicircle, hexagon, pentagon - in one minute each")
              + p("A free-hand sketch is a drawing made without instruments but with the same "
                  "construction: a light box or circle to hold the proportions, the construction "
                  "lines, and the outline in one confident stroke. Speed comes from the order of the "
                  "strokes, not from a steadier hand.")
              + steps("Draw a light square or circle to hold the shape: it fixes the proportions "
                      "before any outline is committed.",
                      "For a square, mark the four corners on the box and join them with long strokes "
                      "from the shoulder, not the wrist; check the diagonals are equal.",
                      "For a triangle, draw the base first, mark the apex above its midpoint, then "
                      "join; an equilateral triangle is as tall as 0.866 of its side.",
                      "For a circle, draw the light square, mark the four tangents, then join with four "
                      "arcs; a circle that fits its square is round.",
                      "For a semicircle, draw the diameter, erect the radius at the centre and sweep "
                      "half the circle from that centre.",
                      "For a hexagon, draw the light circle, step the radius round it six times, and "
                      "join alternate points; for a pentagon, draw the circle, mark the top point and "
                      "step 72 degrees round it.")
              + h4("Proportions worth remembering")
              + ul("Equilateral triangle: height = 0.866 x side; the apex is above the midpoint.",
                   "Regular hexagon: side = circumradius, across corners = 2 x side, across flats = "
                   "1.732 x side.",
                   "Regular pentagon: side = 1.176 x circumradius, and each interior angle is 108 "
                   "degrees.",
                   "Semicircle: the angle in the semicircle is a right angle, which is the quickest "
                   "check on the sketch.")
              + why("Every one of these shapes is built from a circle or a box, so sketching them "
                    "free-hand is the same construction as drawing them with instruments - only the "
                    "light construction is done by eye instead of by a compass.")
              + pit("Sketching the outline first and the construction afterwards. The construction is "
                    "what makes the sketch look right; it must come first, lightly, and stay visible."),
              diagram="u5_freehand", syllabus_item="5.3"),
     ]},
]

_PRACTICE = [
    ("A stepped block has a base plate 60 mm x 40 mm x 15 mm and an upright 20 mm x 40 mm x 25 mm on "
     "its left end. Draw its front, top and side views in first angle.", 6,
     [h4("Read the object")
      + p("Overall 60 wide, 40 deep and 40 high. The upright stands on the left end of the plate and "
          "runs the full depth, so the side view is a plain square."),
      h4("Construction, step by step")
      + ol("Draw the front view in the middle of the sheet: an L, 60 wide and 40 high, with the "
           "upright 20 wide and 25 high on the left and the plate 15 high across the bottom.",
           "Project down from every corner and draw the top view below: a 60 x 40 rectangle with a "
           "visible line across it 20 from the left end.",
           "Project across to the right and draw the side view: a 40 x 40 square, because the upright "
           "fills the depth and the height.",
           "Add the hidden line in the side view: the top of the plate is 15 up from the base and is "
           "hidden behind the upright, so it is drawn dashed.",
           "Check the shared dimensions: 40 high in the front and the side, 60 wide in the front and "
           "the top, 40 deep in the top and the side."),
      h4("The answer")
      + p("Front view: an L 60 x 40 with a 20 x 25 upright. Top view: a 60 x 40 rectangle divided at "
          "20. Side view: a 40 x 40 square with one dashed line 15 up from the base.")]),

    ("A cylinder of 40 mm diameter and 50 mm height stands on HP. Draw its three views, showing the "
     "axis.", 5,
     [h4("Read the object")
      + p("A standing cylinder is round about a vertical axis, so the view down the axis is a circle "
          "and the other two views are the same rectangle."),
      h4("Construction, step by step")
      + ol("Draw the top view first: a circle of 40 mm diameter, with two thin chain centre lines "
           "crossing at its centre.",
           "Project up from the two extreme points of the circle, 40 mm apart.",
           "Set the height 50 mm above the base line and close the front view as a rectangle 40 x 50.",
           "Draw the vertical axis as a thin chain line through the middle of the rectangle.",
           "Draw the side view as the identical rectangle 40 x 50 to the right, with the same axis, "
           "and check both rectangles are the same height."),
      h4("The answer")
      + p("Top view: a circle of diameter 40 with centre lines. Front and side views: the same "
          "rectangle 40 x 50 with a chain centre line. Nothing is hidden, so no dashed line is "
          "needed.")]),

    ("A rectangular plate 60 mm x 40 mm x 15 mm has a hole of 20 mm diameter drilled vertically "
     "through its centre. Draw the three views.", 6,
     [h4("Read the object")
      + p("The hole runs through the 15 mm thickness, so it is seen as a circle from above and as two "
          "hidden lines from the front and the side."),
      h4("Construction, step by step")
      + ol("Draw the front view: a rectangle 60 x 15 with two vertical dashed lines 20 mm apart, "
           "centred.",
           "Project down and draw the top view: a 60 x 40 rectangle with the circle of diameter 20 in "
           "the middle and cross centre lines through it.",
           "Project the front view across to the right and draw the side view: a rectangle 40 x 15.",
           "Draw the hole in the side view as two vertical dashed lines 20 mm apart, in the same "
           "relative position as in the front view.",
           "Check the circle and the dashed lines are the same 20 mm, and that the dashed lines run "
           "the full 15 mm thickness."),
      h4("The answer")
      + p("Front and side views: solid outline 60 x 15 and 40 x 15 with a pair of dashed lines 20 mm "
          "apart. Top view: 60 x 40 with a solid circle of diameter 20 and centre lines. The hole is "
          "hidden in two views and visible in one.")]),

    ("A square pyramid has a base 40 mm square and an axis 50 mm long, standing on HP with two sides "
     "of the base parallel to VP. Draw its three views.", 6,
     [h4("Read the object")
      + p("With the base square sitting square to the viewer, the front view shows the true triangle "
          "of the pyramid and the top view shows the square with its diagonals meeting at the apex."),
      h4("Construction, step by step")
      + ol("Draw the top view first: a square 40 x 40 with both diagonals, which meet at the centre - "
           "that centre is the apex seen from above.",
           "Project up from the four corners and from the centre.",
           "Set the axis 50 mm above the base line and mark the apex at the centre.",
           "Join the apex to the two base corners that are visible in the front view, giving a "
           "triangle of base 40 and height 50.",
           "Draw the two edges to the far corners as thin or dashed lines, and repeat the triangle in "
           "the side view, where the base shows 40 mm again."),
      h4("The answer")
      + p("Top view: a 40 mm square with diagonals. Front and side views: a triangle 40 wide and 50 "
          "high. The slant edge measures the square root of (50 squared + 20 squared + 20 squared) = "
          "57.4 mm, which is the check on the pyramid.")]),

    ("The front view of an object is an L 60 mm wide and 40 mm high with the upright 20 mm wide, and "
     "its top view is a 60 mm x 40 mm rectangle divided 20 mm from one end. Draw the side view and "
     "state what it must contain.", 5,
     [h4("Given")
      + p("Two views of a stepped block are given; the third must be derived from them and must not "
          "invent a single dimension."),
      h4("Construction, step by step")
      + ol("Project the two given views and add the projector lines between them.",
           "Carry the heights across from the front view: the base line, 15 mm and 40 mm.",
           "Carry the depth, 40 mm, round from the top view with a 45 degree mitre line.",
           "Draw the outline: a 40 x 40 square, because the upright fills both the depth and the "
           "height.",
           "Add the hidden line 15 mm above the base, since the top of the plate is behind the "
           "upright, and ink the outline thick."),
      h4("The answer")
      + p("A 40 mm x 40 mm square with one dashed horizontal line 15 mm above the base. Its height "
          "equals the front view's height and its width equals the top view's depth - the two checks "
          "that prove the third view belongs to the same object.")]),

    ("Sketch free-hand, in about a minute each: a square, an equilateral triangle, a circle, a "
     "semicircle, a regular hexagon and a regular pentagon, each about 50 mm across, leaving the "
     "construction lines visible.", 5,
     [h4("The method for all six")
      + p("A light box or circle first, the construction lines second, the outline last and in one "
          "stroke. The construction is what makes the sketch correct; it is not erased."),
      h4("Construction, step by step")
      + ol("Square: a light box with equal diagonals, corners joined with long strokes.",
           "Triangle: base first, apex above its midpoint at 0.866 of the base, then the two sides.",
           "Circle: a light square, the four tangent points, then four arcs joined smoothly.",
           "Semicircle: the diameter, the radius erected at its centre, and half a circle swept from "
           "that centre.",
           "Hexagon: a light circle, the radius stepped round six times, alternate points joined; "
           "across flats = 1.732 x side.",
           "Pentagon: a light circle, the top point and then 72 degrees steps, points joined; each "
           "interior angle is 108 degrees."),
      h4("The checks")
      + p("The square's diagonals must be equal, the triangle's sides equal, the circle must touch all "
          "four sides of its box, the hexagon must be 1.732 times its side across the flats, and the "
          "pentagon's five chords must all measure the same.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)

EQUATIONS = [
    {"title": tr("Placement and agreement of the views"), "items": [
        {"name": tr("First angle layout"),
         "f": "top view below the front view, left side view to the right",
         "terms": tr("In first-angle projection the view is placed on the far side of the object, so "
                     "the plan swings down below the elevation and the left side view sits on the "
                     "right.")},
        {"name": tr("Shared dimensions"),
         "f": "front/side share height, front/top share width, top/side share depth",
         "terms": tr("Each pair of views looks along the axis of the third, so the two dimensions "
                     "they share must come out identical; this is the check on any set of views.")},
        {"name": tr("Depth transfer"), "f": "45 degree mitre line from the top view to the side view",
         "terms": tr("A line at 45 degrees to the base line turns a depth measured below the front "
                     "view into the same depth measured across the side view.")},
    ]},
    {"title": tr("Shapes in the views"), "items": [
        {"name": tr("Cylinder standing"), "f": "front and side 2r x h, top a circle of diameter 2r",
         "terms": tr("The view along the axis is a circle and the views across it show the extreme "
                     "generators, so both are the same rectangle.")},
        {"name": tr("Cone standing"), "f": "front and side an isosceles triangle 2r x h, top a circle",
         "terms": tr("The slant height is the square root of (r squared + h squared), and it is the "
                     "true length of the generator drawn in the elevation.")},
        {"name": tr("Square pyramid"), "f": "top a square with diagonals, views a triangle b x h",
         "terms": tr("The apex appears in the plan as the crossing of the diagonals and in the "
                     "elevation at the height of the axis.")},
        {"name": tr("Hexagon, free hand"), "f": "across flats = 1.732 x side",
         "terms": tr("Side equals circumradius, so the across-corners size is twice the side and the "
                     "across-flats size is 1.732 times it.")},
        {"name": tr("Pentagon, free hand"), "f": "side = 1.176 x R, interior angle 108 degrees",
         "terms": tr("Stepping 72 degrees round the circumcircle gives the five vertices; every chord "
                     "and every interior angle comes out equal.")},
    ]},
]

VIVA = [
    {"title": tr("First angle and layout"), "items": [
        {"q": tr("What is the difference between first-angle and third-angle projection?"),
         "a": tr("In first angle the object is between the observer and the plane, so the view is "
                 "placed on the far side of the object: the top view goes below the front view. In "
                 "third angle the plane is between the observer and the object, so the top view goes "
                 "above. India uses first angle by BIS convention.")},
        {"q": tr("Where is the side view placed in first angle, and which side is it taken from?"),
         "a": tr("To the right of the front view, and it is the view from the left of the object, "
                 "because the left side view formed on the right-hand plane swings round to the right "
                 "when the box is opened out.")},
        {"q": tr("Which dimensions do the front and side views share?"),
         "a": tr("The height. The front and the top views share the width, and the top and the side "
                 "views share the depth. If any pair disagrees the three views do not describe one "
                 "object.")},
        {"q": tr("What is the use of the 45 degree mitre line?"),
         "a": tr("It transfers a depth from the top view across to the side view: a horizontal line "
                 "from the top view meets the mitre line and is then turned into a vertical at the "
                 "side view, so the depth is carried round accurately without measuring twice.")},
        {"q": tr("Why is a hidden edge drawn dashed and not left out?"),
         "a": tr("Because it is still an edge of the object, and the drawing must describe the whole "
                 "object. A dashed line shows where an edge lies behind material, which is exactly "
                 "what the reader needs in order to picture the shape.")},
    ]},
    {"title": tr("Reading the object"), "items": [
        {"q": tr("How do you choose the front view of an object?"),
         "a": tr("Pick the direction that shows the most of the shape and the fewest hidden edges, and "
                 "that leaves the object in a natural standing position. That view becomes the front "
                 "view and the other two follow from it.")},
        {"q": tr("What are the three views of a standing cylinder?"),
         "a": tr("A circle of diameter 2r in the top view and identical rectangles 2r by h in the "
                 "front and side views, each with a thin chain centre line on the axis. Nothing is "
                 "hidden, so no dashed line appears.")},
        {"q": tr("What are the three views of a standing cone?"),
         "a": tr("A circle with a centre point in the top view, and an isosceles triangle in the front "
                 "and side views: base 2r, height h, and the slant sides equal to the square root of "
                 "(r squared plus h squared).")},
        {"q": tr("A hole passes vertically through a plate. How does it appear in each view?"),
         "a": tr("As a solid circle with centre lines in the top view, and as two dashed vertical "
                 "lines 20 mm apart in the front and side views, running the full thickness of the "
                 "material, because the hole is hidden there.")},
        {"q": tr("How do you draw the third view when two are given?"),
         "a": tr("Project every corner of the given views into the position of the new view, taking "
                 "the height from the front view and the depth from the top view, and joining the "
                 "crossings. No new dimension is invented; every size is already in the two views.")},
    ]},
    {"title": tr("Free-hand sketching"), "items": [
        {"q": tr("What makes a free-hand sketch acceptable in an examination?"),
         "a": tr("Correct proportions and correct construction shown lightly: the box or circle that "
                 "holds the shape, the construction lines, and a clean outline. Instruments are not "
                 "needed, but the geometry must still be right.")},
        {"q": tr("How do you sketch a circle free-hand?"),
         "a": tr("Draw a light square first, mark the four tangent points at the middle of each side, "
                 "and join them with four arcs, turning the paper rather than the hand. A circle that "
                 "touches all four sides of its square is round enough for a sketch.")},
        {"q": tr("How do you sketch a regular hexagon?"),
         "a": tr("Draw a light circle, step the radius round its circumference six times, and join "
                 "alternate points for the three long diagonals. The across-corners size is twice the "
                 "side and the across-flats size is 1.732 times the side.")},
        {"q": tr("What check proves a sketched pentagon?"),
         "a": tr("All five sides equal, all five interior angles 108 degrees, and the five vertices "
                 "72 degrees apart on the circumcircle. The side is 1.176 times the circumradius.")},
    ]},
]
