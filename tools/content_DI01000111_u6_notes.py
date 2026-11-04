"""DI01000111 Engineering Graphics - Unit 6: Isometric View.

GTU 6.1-6.2, 6 h, 20 %, 14 marks, CO5. English only. Every object is built on the three isometric
axes as a numbered construction - box it, measure along the axes, cut the corners away - and the
round solids are built on the exact isometric ellipse.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_DI01000111_u1_notes import (tr, p, h4, ul, ol, table, steps, why, check, pit,  # noqa
                                        card)

SOURCES = [
    ("GTU DI01000111 Engineering Graphics syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("N. D. Bhatt - Elementary Engineering Drawing, Charotar Publishing House, Anand (chapter 12: "
     "isometric projection)", "https://www.charotarbookstall.com/"),
    ("P. S. Gill - A Text Book of Engineering Drawing, S. K. Kataria & Sons, Delhi (isometric view, "
     "isometric scale and solids in isometric)", "https://www.skkatariaandsons.com/"),
    ("BIS SP 46 - Engineering drawing practice: isometric drawing and isometric scale",
     "https://www.bis.gov.in/"),
]

NOTES = [
    {"title": tr("1. The Isometric Frame and the Box Method"),
     "items": [
         card("6.1 The three axes, the 30 degree lines and the isometric scale",
              h4("One picture instead of three views")
              + p("An <b>isometric view</b> is a single pictorial view in which the three axes of the "
                  "object are drawn 120 degrees apart in space and appear on paper as two lines at "
                  "<b>30 degrees to the horizontal</b> and one line straight up. All three axes are "
                  "foreshortened equally, which is why the three visible faces look equally important "
                  "and no face is seen square-on.")
              + table(["term", "what it means", "what you draw"], [
                  ("isometric axes", "the three directions of the object, 120 degrees apart in space",
                   "two lines at 30 degrees, one vertical"),
                  ("isometric lines", "edges parallel to the three axes",
                   "drawn parallel to the axes, at full scale"),
                  ("non-isometric line", "an edge not parallel to an axis, such as a slope or a "
                   "diagonal", "found by offsets, never measured directly"),
                  ("isometric scale", "0.816 of the true length", "used only in the isometric "
                   "projection"),
              ])
              + h4("Drawing or projection - the one difference")
              + ul("<b>Isometric drawing</b> (what you draw in an exam): every length along an axis is "
                   "set off at <b>full scale</b>, so a 30 mm edge is drawn 30 mm.",
                   "<b>Isometric projection</b>: every axis length is multiplied by "
                   "<b>0.816</b>, so the same 30 mm edge is drawn 24.5 mm.",
                   "The picture is identical in shape; only the size changes, so a drawing made at "
                   "full scale is simply a larger copy.")
              + steps("Draw the three axes from one point, the origin: one vertical and two at 30 "
                      "degrees above the horizontal, one each side.",
                      "Decide which axis carries the length, the width and the height of the object, "
                      "and write them on the axes.",
                      "Set every dimension off along the axes at full scale from the origin, using a "
                      "scale or a divider, never by eye.",
                      "Join the marks parallel to the axes to build the visible faces, and finish "
                      "with the outer outline thickened.",
                      "Check: every edge parallel to an axis in the object must be parallel to the "
                      "same axis in the drawing, and the three axes must never be drawn at right "
                      "angles.")
              + why("The isometric view looks along the body diagonal of a cube, so the three faces of "
                    "the cube are seen equally - which is why each axis is shortened by the same "
                    "factor, 0.816, and why all three appear at 120 degrees in space.")
              + pit("Using 30 degrees for the vertical as well. Only two axes are inclined; the third "
                    "is always vertical, and the angles between the three drawn axes are 120 degrees.")
              ,
              diagram="u6_axes", syllabus_item="6.1"),

         card("6.1 The box method - from three views to one picture",
              h4("A block 60 x 40 x 30, given as front, top and side views")
              + p("Every isometric drawing starts as a box. The overall length, width and height are "
                  "measured along the three axes, giving a box that encloses the object; the object "
                  "is then cut out of that box, face by face. For a plain block the box <i>is</i> the "
                  "object, and only three faces are drawn - the three that face the observer.")
              + steps("From the views, write down the overall size: 60 along one axis, 40 along the "
                      "second, 30 up the third.",
                      "Draw the three axes from the lowest corner and set the three sizes off along "
                      "them, giving three points.",
                      "Through each of those points draw lines parallel to the other two axes: the "
                      "three lines meet in the three visible edges of the box.",
                      "Complete the top face, the front face and the side face as parallelograms, "
                      "each bounded by two axis directions.",
                      "Thicken the outer outline, and leave out every hidden edge - an isometric view "
                      "shows only what is visible, unless a hidden line is asked for.")
              + h4("How the sizes appear")
              + table(["edge", "true size", "drawn", "direction"], [
                  ("length", "60 mm", "60 mm", "along the 30 degree axis to the right"),
                  ("width", "40 mm", "40 mm", "along the 30 degree axis to the left"),
                  ("height", "30 mm", "30 mm", "vertical"),
              ])
              + why("The three views give the three sizes and the isometric axes give the three "
                    "directions; once a size is set off along the right axis, the corner is fixed. "
                    "That is why a drawing made from three views and one made from a pictorial view "
                    "come out identical.")
              + check("Measure the outline: the box's silhouette is a hexagon whose opposite sides are "
                      "equal and parallel, and the three visible faces meet at the front corner with "
                      "120 degrees between their edges.")
              + pit("Making the front face a true rectangle. In isometric no face is seen square-on: "
                    "every face is a parallelogram whose sides follow two of the three axes."),
              diagram="u6_box", syllabus_item="6.1"),

         card("6.1 Offsets: points and slopes that are off the axes",
              h4("A wedge 50 x 30 with a height of 20 at one end")
              + p("The sloping face of a wedge is a <b>non-isometric line</b>: it is not parallel to "
                  "any axis, so it cannot be measured along an axis and it is not true to length in "
                  "the drawing. Its ends are located by <b>offsets</b> - distances measured along the "
                  "axes from a known corner - and then joined.")
              + steps("Draw the base rhombus on the two horizontal axes: 50 along X and 30 along Y.",
                      "Erect the vertical edges at the corners where the object has height - here "
                      "20 mm at the far end of X.",
                      "Mark the top edge at that end, 20 mm up, parallel to the 30 mm side.",
                      "Locate any other point on the sloping face by offsets: go 25 along X, 15 along "
                      "Y, and 10 up - each offset measured from the origin along an axis and joined "
                      "by a line parallel to that axis.",
                      "Join the corners of the sloping face and thicken it; the slope's true length "
                      "is never measured on the drawing.")
              + h4("Which lines are which")
              + ul("<b>Isometric lines</b> - parallel to an axis: drawn at full length along the "
                   "axis, no offsets needed.",
                   "<b>Non-isometric lines</b> - slopes, diagonals, chamfers: both ends found by "
                   "offsets, then joined.",
                   "A circle in an isometric face is an ellipse - never a compass circle.")
              + why("An offset is a pair (or a triple) of axis measurements, and axis measurements are "
                    "the only ones the isometric frame preserves. Any point in space is therefore "
                    "reachable, which is why the offset method can build a shape of any outline.")
              + pit("Measuring a sloping edge along its own direction on the paper. A slope is "
                    "foreshortened differently from every axis, so its drawn length means nothing - "
                    "locate its ends, then join them."),
              diagram="u6_offsets", syllabus_item="6.1"),
     ]},

    {"title": tr("2. Round and Regular Solids in Isometric"),
     "items": [
         card("6.2 The cylinder: the isometric ellipse and its tangents",
              h4("Cylinder of 40 mm diameter and 40 mm height, axis vertical")
              + p("A circle in an isometric face is drawn as an <b>ellipse</b>, and the exact ellipse "
                  "is easy to remember: its major axis is <b>1.22 d</b> and its minor axis "
                  "<b>0.71 d</b>, with the major axis square to the axis about which the face is "
                  "tilted. For a circle of 40 mm in a horizontal face the ellipse is therefore 49 mm "
                  "by 28 mm, lying inside the isometric square of side 40.")
              + steps("Draw the isometric square of side 40 mm on the two horizontal axes; its four "
                      "side mid-points are the points where the ellipse touches it.",
                      "Through the centre draw the long axis, 1.22 x 40 = 49 mm, parallel to the "
                      "longer diagonal of the square, and the short axis, 0.71 x 40 = 28 mm, square "
                      "to it.",
                      "Sketch the ellipse through the four touching points and the four axis ends, or "
                      "plot it by offsets from the square.",
                      "Repeat the same ellipse 40 mm higher for the top face, keeping the same centre "
                      "line.",
                      "Join the two ellipses with the two vertical tangents, drawn at the ends of the "
                      "major axis, and thicken the visible outline: the far half of the bottom "
                      "ellipse stays thin or dashed.")
              + h4("Numbers for round solids")
              + table(["true circle", "isometric ellipse", "used for"], [
                  ("40 mm diameter", "49 mm x 28 mm", "the two ends of a 40 mm cylinder"),
                  ("30 mm diameter", "36.6 mm x 21.3 mm", "a 30 mm rod in a bearing"),
                  ("20 mm diameter", "24.4 mm x 14.2 mm", "a hole through a plate"),
              ])
              + why("The foreshortening is the same 0.816 in every direction, so a circle - which is "
                    "the same in every direction - becomes an ellipse whose axes are the two extreme "
                    "foreshortenings of that face: 1.22 across the tilt and 0.71 along it.")
              + check("The ellipse must touch its isometric square at the middle of each side, and "
                      "the long axis must lie along the longer diagonal. If it touches a corner, the "
                      "square is the wrong size.")
              + pit("Drawing the top and bottom circles the same way round and joining them with "
                    "vertical lines at the sides of the ellipse. The tangents belong at the ends of "
                    "the <b>major</b> axis, which is wider than the square.")
              ,
              diagram="u6_cylinder", syllabus_item="6.1"),

         card("6.2 Prism, pyramid and cone - and the free-hand sketches",
              h4("Base first, then up the axis")
              + p("A prism, a pyramid and a cone are all built the same way: draw the base polygon in "
                  "the two horizontal axes, then take the vertical edges - or the apex - up the third "
                  "axis. The base is drawn true in isometric, which for a square means a rhombus and "
                  "for a hexagon means the hexagon squeezed on to the two 30 degree axes.")
              + steps("Draw the base polygon on the two horizontal axes: a rhombus for a square or "
                      "hexagon base, a circle (ellipse) for a cylinder or cone.",
                      "From every corner of the base draw the vertical edges, at full height, along "
                      "the vertical axis.",
                      "For a prism, join the top corners to give the second base; for a pyramid or "
                      "cone, mark the apex on the vertical axis through the centre of the base.",
                      "Join the apex to the visible base corners - only the two or three that face the "
                      "observer - and leave the rest out or thin.",
                      "Sketch free-hand in the same order: base rhombus, verticals, top or apex; a "
                      "free-hand isometric is only the same construction done quickly.")
              + h4("The four solids the syllabus names")
              + table(["solid", "base in isometric", "the rest"], [
                  ("prism", "regular polygon on the two horizontal axes", "vertical edges and a "
                   "second polygon on top"),
                  ("pyramid", "regular polygon, drawn with its diagonals", "apex on the vertical axis "
                   "through the centre"),
                  ("cylinder", "ellipse 1.22 d by 0.71 d", "second ellipse above and two tangents"),
                  ("cone", "ellipse 1.22 d by 0.71 d", "apex on the axis and two tangents to the base "
                   "ellipse"),
              ])
              + why("Every one of these solids is a base carried up a vertical axis, so the isometric "
                    "frame only has to be set up once: the base is a true polygon on the two "
                    "horizontal axes and the height is read straight up the vertical axis.")
              + check("For a pyramid or cone the apex must sit exactly above the centre of the base - "
                      "measured to the crossing of the diagonals or the centre of the ellipse, not "
                      "guessed by eye.")
              + pit("Drawing the apex above the nearest corner instead of above the centre. The axis "
                    "of the solid is vertical, so the apex is directly over the centre of the base."),
              diagram="u6_solids", syllabus_item="6.2"),
     ]},
]

_PRACTICE = [
    ("A rectangular block 60 mm x 40 mm x 30 mm is given by its three views. Draw its isometric view, "
     "taking full scale along the axes.", 5,
     [h4("Given")
      + p("Length 60, width 40, height 30. The isometric view is drawn at full scale, so the three "
          "sizes go straight along the axes."),
      h4("Construction, step by step")
      + ol("Draw the three axes from the lowest corner: one vertical and two at 30 degrees to the "
           "horizontal.",
           "Set 60 mm along the right-hand axis, 40 mm along the left-hand axis and 30 mm up the "
           "vertical axis.",
           "Through each of those three points draw lines parallel to the other two axes, giving the "
           "three visible faces.",
           "Complete the three parallelograms - front face 60 x 30, side face 40 x 30, top face "
           "60 x 40 - and thicken the outer outline.",
           "Check that every edge is parallel to one of the axes, and that no face is a true "
           "rectangle."),
      h4("The answer")
      + p("A hexagonal outline 60 mm and 40 mm along the two 30 degree directions with vertical edges "
          "of 30 mm. Every line in the drawing is parallel to one of the three axes, and all three "
          "visible faces are parallelograms.")]),

    ("The same block is to be drawn as an isometric projection. What lengths go along the axes, and "
     "how do the two drawings differ?", 4,
     [h4("The scale")
      + p("An isometric projection shortens every axis length by 0.816, so a 60 mm edge is drawn "
          "60 x 0.816 = 49 mm."),
      h4("Construction, step by step")
      + ol("Work out the three shortened lengths: 60 x 0.816 = 49.0 mm, 40 x 0.816 = 32.6 mm and "
           "30 x 0.816 = 24.5 mm.",
           "Draw the same three axes and set these three lengths off along them.",
           "Complete the same three parallelograms as before.",
           "Measure the outline: every dimension is 0.816 of the drawing made at full scale.",
           "State in the answer which of the two you have drawn, because the pictures look identical "
           "apart from size."),
      h4("The answer")
      + p("49.0, 32.6 and 24.5 mm. The isometric projection is the same picture reduced to 0.816, so "
          "the shape is identical and only the size differs; exam questions normally ask for the "
          "isometric view at full scale.")]),

    ("A wedge has a base 50 mm x 30 mm and rises to 20 mm at one end, the top face sloping down to the "
     "opposite edge of the base. Draw its isometric view and state which of its lines are "
     "non-isometric.", 5,
     [h4("Given")
      + p("The base lies on the two horizontal axes; the sloping face is not parallel to any axis, so "
          "it is a non-isometric line."),
      h4("Construction, step by step")
      + ol("Draw the base rhombus: 50 mm along X and 30 mm along Y.",
           "Erect the 20 mm vertical edge at the corners at the high end and join their tops.",
           "Locate any intermediate point on the slope by offsets - for example 25 along X, 15 along "
           "Y and 10 up - each measured from the origin.",
           "Join the high edge to the far edge of the base to complete the sloping face.",
           "Thicken the visible edges and check that the four sloping edges are the only ones not "
           "parallel to an axis."),
      h4("The answer")
      + p("The base edges and the vertical edges are isometric lines; the four edges of the sloping "
          "face are non-isometric, and a point on that face is fixed by offsets such as 25, 15 and 10 "
          "mm from the origin.")]),

    ("A cylinder of 40 mm diameter and 40 mm height stands on its base. Draw its isometric view, "
     "stating the axes of both ellipses.", 6,
     [h4("Given")
      + p("The base is a horizontal circle of 40 mm, so it is drawn as an ellipse of 1.22 x 40 = 49 mm "
          "by 0.71 x 40 = 28 mm."),
      h4("Construction, step by step")
      + ol("Draw the isometric square of side 40 mm on the two horizontal axes and mark the mid-points "
           "of its four sides.",
           "Through the centre draw the long axis 49 mm, along the longer diagonal, and the short "
           "axis 28 mm square to it.",
           "Sketch the ellipse through the four mid-points and the four axis ends.",
           "Repeat the ellipse 40 mm higher for the top face, using the same centre line.",
           "Join the two ellipses with vertical tangents at the ends of the long axis, thicken the "
           "visible outline, and leave the hidden half of the base thin or dashed."),
      h4("The answer")
      + p("Two ellipses of 49 mm by 28 mm with their long axes parallel, joined by two vertical "
          "tangents 49 mm apart. The tangents are at the ends of the major axis, not at the sides of "
          "the 40 mm square.")]),

    ("A square pyramid has a base of 30 mm side and an axis of 45 mm. Draw its isometric view.", 5,
     [h4("Given")
      + p("The base square is drawn as a rhombus on the two horizontal axes; the apex stands on the "
          "vertical axis above the centre of the base."),
      h4("Construction, step by step")
      + ol("Draw the rhombus for the 30 mm square on the two 30 degree axes.",
           "Draw both diagonals of the rhombus; their crossing is the centre of the base.",
           "Through that centre draw the vertical axis and mark the apex 45 mm up.",
           "Join the apex to the three visible corners of the base, and leave the fourth edge thin or "
           "dashed.",
           "Check that the apex is vertically above the crossing of the diagonals."),
      h4("The answer")
      + p("A rhombus base 30 mm on a side with the apex 45 mm above its centre, giving a pyramid whose "
          "visible edges are the two front base edges and the three edges up to the apex.")]),

    ("Sketch free-hand the isometric view of a triangular prism with a base of 40 mm side and a height "
     "of 50 mm, leaving the construction visible.", 4,
     [h4("The order to sketch in")
      + p("Base first, uprights second, top third - the same order as with instruments, only faster "
          "and lighter."),
      h4("Construction, step by step")
      + ol("Lightly draw the three axes from a corner.",
           "Lay the triangular base on the two horizontal axes: 40 mm on one, 40 mm on the other, and "
           "the third corner placed by offsets.",
           "Draw the three vertical edges 50 mm high from the base corners.",
           "Join the tops to give the second triangle, and thicken only the visible edges.",
           "Check that the three vertical edges are equal and parallel and that both triangles are "
           "the same shape."),
      h4("The answer")
      + p("A prism whose two triangles lie one above the other with three vertical edges of 50 mm "
          "between them. The construction axes and the light base lines stay visible - that is what "
          "marks it as a proper free-hand isometric sketch.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)

EQUATIONS = [
    {"title": tr("The isometric frame"), "items": [
        {"name": tr("Isometric scale"), "f": "isometric length = 0.816 x true length",
         "terms": tr("Every axis is foreshortened by the same factor, 0.816, in the isometric "
                     "projection; the isometric drawing takes the factor as 1 and uses full scale.")},
        {"name": tr("Angles between the axes"), "f": "120 degrees in space; 30, 30 and vertical on "
         "paper",
         "terms": tr("The two horizontal axes are drawn at 30 degrees above the horizontal and the "
                     "third straight up, giving 120 degrees between every pair.")},
        {"name": tr("Isometric square"), "f": "a true square of side a becomes a rhombus of side a",
         "terms": tr("Its long diagonal is 1.22 a and its short diagonal 0.71 a, which is the frame "
                     "the isometric ellipse is drawn in.")},
    ]},
    {"title": tr("Circles and solids in isometric"), "items": [
        {"name": tr("Isometric ellipse"), "f": "major axis 1.22 d, minor axis 0.71 d",
         "terms": tr("A circle of diameter d in one of the coordinate faces projects as an ellipse "
                     "with those axes; the major axis lies along the longer diagonal of the isometric "
                     "square.")},
        {"name": tr("Cylinder in isometric"), "f": "two ellipses 1.22 d by 0.71 d joined by tangents",
         "terms": tr("The tangents are drawn at the ends of the major axis, because that is where the "
                     "ellipse's own tangent is vertical.")},
        {"name": tr("Cone or pyramid in isometric"), "f": "apex on the vertical axis above the centre "
         "of the base",
         "terms": tr("The base is drawn true as a polygon or an ellipse, and every visible apex edge "
                     "is drawn from the base corner to the apex.")},
        {"name": tr("Offset to a point"), "f": "(x, y, z) measured along the three axes from a known "
         "corner",
         "terms": tr("A point that does not lie on an axis is fixed by three distances along the "
                     "axes, joined by lines parallel to the axes.")},
    ]},
]

VIVA = [
    {"title": tr("Axes and scale"), "items": [
        {"q": tr("What are the isometric axes and why are they 30 degrees apart on paper?"),
         "a": tr("They are the three edges of a cube meeting at one corner, which are 120 degrees "
                 "apart in space. The isometric view looks along the body diagonal of the cube, so "
                 "that corner points at the observer and the three edges appear on paper as two lines "
                 "at 30 degrees to the horizontal and one line straight up.")},
        {"q": tr("What is the difference between an isometric view and an isometric projection?"),
         "a": tr("In an isometric projection every axis length is multiplied by 0.816, so the picture "
                 "is smaller. In an isometric drawing the axis lengths are set off at their true "
                 "sizes, so the picture is the same shape but 1/0.816 = 1.22 times larger. Exams "
                 "normally ask for the isometric view.")},
        {"q": tr("What is the isometric scale and where does 0.816 come from?"),
         "a": tr("It is the factor by which every axis is shortened in the projection: 0.816, the "
                 "cosine of the angle between the axis and the plane of the picture, which is about "
                 "35 degrees 16 minutes. All three axes are shortened by the same factor.")},
        {"q": tr("Which lines are true in an isometric drawing?"),
         "a": tr("Only the isometric lines - the edges parallel to the three axes. Any edge not "
                 "parallel to an axis is a non-isometric line and is foreshortened in a way that "
                 "cannot be measured along the paper.")},
    ]},
    {"title": tr("Drawing the objects"), "items": [
        {"q": tr("How do you start the isometric view of any object?"),
         "a": tr("With the box. Take the overall length, width and height from the views, set them "
                 "along the three axes from one corner, and complete the enclosing box; then cut the "
                 "object out of that box face by face, drawing only the visible faces.")},
        {"q": tr("How is a circle drawn in an isometric face?"),
         "a": tr("As an ellipse with a major axis of 1.22 d and a minor axis of 0.71 d, drawn inside "
                 "the isometric square of side d so that it touches the mid-points of the four sides. "
                 "The long axis lies along the longer diagonal of that square.")},
        {"q": tr("Where are the vertical tangents of a cylinder drawn?"),
         "a": tr("At the ends of the major axis of the ellipse, because that is where the ellipse's "
                 "own tangent is vertical. They are therefore 1.22 d apart, not d apart.")},
        {"q": tr("How is the apex of a cone or a pyramid located?"),
         "a": tr("On the vertical axis through the centre of the base - the crossing of the diagonals "
                 "for a polygon, the centre of the ellipse for a circle - at the given axial height. "
                 "Then only the visible base corners are joined to it.")},
        {"q": tr("How do you locate a point that lies on a sloping face?"),
         "a": tr("By offsets: measure its distances along the three axes from a known corner and draw "
                 "lines parallel to the axes to meet in the point. Its position on the sloping face "
                 "is then fixed without ever measuring along the slope itself.")},
        {"q": tr("Which edges are left out of an isometric view?"),
         "a": tr("The hidden ones. An isometric view is a pictorial view of what the observer can "
                 "see, so the outline and the visible edges are drawn thick and the back edges are "
                 "omitted unless the question asks for hidden detail.")},
        {"q": tr("What check proves an isometric drawing?"),
         "a": tr("Every edge must be parallel to one of the three axes, apart from the deliberately "
                 "non-isometric edges; equal edges of the object must come out equal; and the three "
                 "visible faces must meet at the front corner with 120 degrees between their edges.")},
    ]},
]
