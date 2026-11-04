"""DI01000111 Engineering Graphics - Unit 1: Introduction to Engineering Graphics.

GTU 1.1-1.3, 4 h, 10 %, 7 marks, CO1. English only (user decision), and every drawing topic is
taught as a numbered construction so the student learns how the sheet is built step by step.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from subject_DI01000111 import tr as _tr  # noqa: E402


class Txt(dict):
    def __add__(self, other):
        return Txt({"en": self["en"] + str(other)})

    def __radd__(self, other):
        return Txt({"en": str(other) + self["en"]})


def tr(s):
    return Txt({"en": s})


def p(x):
    return f"<p>{x}</p>"


def h4(x):
    return f"<h4>{x}</h4>"


def ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(*items):
    return "<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>"


def table(head, rows):
    return ("<table><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
            + "</table>")


def steps(*items):
    """The core teaching device of this subject: one numbered construction step per line."""
    return h4("Construction, step by step") + ol(*items)


def why(x):
    return p(f"<b>Why it works.</b> {x}")


def check(x):
    return p(f"<b>Check before you ink.</b> {x}")


def pit(x):
    return p(f"<b>Common mistake.</b> {x}")


def card(heading, body, diagram=None, syllabus_item=None):
    item = {"h": tr(heading), "body": tr(body)}
    if diagram:
        item["diagram"] = diagram
    if syllabus_item:
        item["syllabus_item"] = syllabus_item
    return item


SOURCES = [
    ("GTU DI01000111 Engineering Graphics syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("BIS SP 46 - Engineering drawing practice for schools and colleges: line types, lettering and "
     "dimensioning", "https://www.bis.gov.in/"),
    ("N. D. Bhatt - Elementary Engineering Drawing, Charotar Publishing House, Anand (chapters 1-3: "
     "instruments, lines, dimensioning, scales and polygons)", "https://www.charotarbookstall.com/"),
    ("P. S. Gill - A Text Book of Engineering Drawing, S. K. Kataria & Sons, Delhi (sheet layout, "
     "BIS conventions and polygon constructions)", "https://www.skkatariaandsons.com/"),
]

NOTES = [
    {"title": tr("1. The Sheet, the Lines and the Instrument Box"),
     "items": [
         card("1.1 The drawing sheet, the border and the title block",
              h4("What is on the sheet before any object")
              + p("A drawing is a legal document: the part is made exactly as the sheet says, so the "
                  "sheet itself follows a standard. BIS SP 46 fixes the paper sizes, the border, the "
                  "title block and the lettering. The A series halves at every step - A0 is 841 x "
                  "1189 mm, A1 is 594 x 841, A2 is 420 x 594, A3 is 297 x 420 and A4 is 210 x 297 - "
                  "and your practical work is done on A2.")
              + h4("Instruments and what each one is for")
              + table(["Instrument", "Used for"], [
                  ("Drawing board and T-square", "a true horizontal, and the guide for every "
                   "vertical through a set square"),
                  ("45 and 30-60 set squares", "15, 30, 45, 60, 75 and 90 degree lines, parallel "
                   "lines and perpendiculars"),
                  ("Compass", "circles and arcs, with the needle point exactly at the centre"),
                  ("Divider", "transferring a length - dividing a line or a circle into equal parts"),
                  ("Scale (plain and diagonal)", "measuring to 1 mm, and reading a drawing at its "
                   "reduced size"),
                  ("Protractor", "any angle that a set square cannot give, such as 72 degrees for a "
                   "pentagon"),
                  ("French curve", "smooth curves that are not circular, such as an ellipse or a "
                   "parabola"),
                  ("Pencils 2H, H and HB", "2H for construction lines, H for the final outlines, "
                   "HB for lettering"),
              ])
              + steps("Clean the board and fix the sheet with its top edge parallel to the board "
                      "edge; test with the T-square before you tape the four corners.",
                      "Draw the border 10 mm inside the trimming edge on three sides and 20 mm on "
                      "the left, which is the filing margin.",
                      "Draw the title block in the bottom right corner, 65 mm wide and about 30 mm "
                      "high, and divide it into rows for the name, roll number, class, subject, "
                      "title, scale, date and sheet number.",
                      "Write the title of the problem in 7 mm capitals inside the block and every "
                      "other entry in 5 mm letters; lettering is part of the drawing, not a note "
                      "added later.",
                      "Draw all construction work in 2H thin lines, then ink the final outline in a "
                      "thick H line, and only then letter the dimensions.")
              + why("The border and the block are always in the same place, so a stranger can pick "
                    "up the sheet and find out what it is, who drew it and at what scale without "
                    "asking. The 20 mm margin is punched for filing and never used for a drawing.")
              + pit("Fixing the sheet by eye makes every horizontal slightly tilted, and no T-square "
                    "can repair that later. Test the top edge first."),
              diagram="u1_sheet", syllabus_item="1.1"),
         card("1.2 Line types and what each one means",
              h4("The alphabet of the drawing")
              + p("Every line on a drawing has one meaning, and the thickness carries as much "
                  "information as the shape. BIS SP 46 gives two thicknesses only, in the ratio 2:1 "
                  "or 3:1 - a thick line of about 0.5 mm and a thin line of about 0.25 mm - and the "
                  "reader must never have to guess which is which.")
              + table(["Line", "Thickness", "Meaning and use"], [
                  ("Continuous thick", "0.5 mm", "visible outlines and visible edges of the object"),
                  ("Continuous thin", "0.25 mm", "dimension lines, extension lines, leaders, "
                   "hatching, short centre lines"),
                  ("Dashed thin", "0.25 mm", "hidden outlines and hidden edges"),
                  ("Continuous thin wavy or zig-zag", "0.25 mm", "the limit of a partial view or a "
                   "broken-out section"),
                  ("Chain thin", "0.25 mm", "centre lines, pitch circles, the path of a moving part"),
                  ("Chain thin with thick ends", "0.25 / 0.5 mm", "the cutting plane line of a "
                   "section"),
                  ("Chain thick", "0.5 mm", "the surface that has to be heat treated or coated"),
                  ("Continuous thin, double dash", "0.25 mm", "outline of an adjacent part, or an "
                   "alternate position"),
              ])
              + steps("Draw every horizontal with the T-square, sliding it along the board with the "
                      "left hand and keeping the pencil at a steady 60 degrees.",
                      "Draw every vertical and every 15, 30, 45, 60 or 75 degree line with the set "
                      "square resting on the T-square; never rotate the board.",
                      "Draw a circle with the compass: prick the centre with the needle, set the "
                      "radius on the scale, and turn the compass by the knurled knob, not by the "
                      "legs.",
                      "Keep the gap between dashes equal to about four times the dash length, and "
                      "start and end a hidden line with a dash, never with a gap.",
                      "Let a centre line project 2 to 3 mm beyond the outline on both sides.")
              + why("Hidden edges are dashed, not thin continuous, so that a hole behind a face can "
                    "be told apart from a groove on the face. A cutting-plane line has thick ends so "
                    "that the arrows showing the direction of sight cannot be missed.")
              + check("Stand back a metre: the thick outline must be clearly heavier than the "
                      "dimension lines, and no two lines of the same weight should meet at a point "
                      "where the meaning is unclear."),
              diagram="u1_lines", syllabus_item="1.2"),
     ]},
]

NOTES.append({"title": tr("2. Dimensioning and the Plane Scale"),
              "items": [
    card("1.2 Dimensioning: the four parts of one dimension",
         h4("Anatomy of a dimension")
         + p("A dimension has an extension line, a dimension line, two arrowheads and a figure. "
             "BIS SP 46 fixes the proportions: the arrowhead is about 3 mm long and 1 mm wide, the "
             "figure is 3 mm high and sits 1 mm above an unbroken dimension line, and the extension "
             "line starts 2 mm away from the object and runs 3 mm past the dimension line.")
         + table(["Element", "Rule as per BIS SP 46"], [
             ("Unit", "millimetres, written without the symbol; 60 means 60 mm"),
             ("Extension line", "thin, perpendicular to the dimension line, 2 mm clear of the "
              "outline and 3 mm beyond the arrow"),
             ("Dimension line", "thin, parallel to the edge being measured, with a gap in the "
              "middle when the space is too small for the figure"),
             ("Figure", "3 mm high, placed above the dimension line and read from the bottom or "
              "from the right - the unidirectional system"),
             ("Arrowhead", "3:1 long to wide, filled, touching the extension line"),
             ("Leader", "thin line with a shoulder, used for a radius, a diameter or a note when "
              "the dimension will not fit inside"),
             ("Symbols", "Ø for diameter, R for radius, SR for spherical radius, □ for a square "
              "face, C or 45 x 5 for a chamfer"),
             ("Repetition", "give a size once, and use 4 x Ø 8 for a repeated feature instead of "
              "four separate leaders"),
         ])
         + steps("Mark the overall length, the overall breadth and the overall height first; they "
                 "are what a machinist checks the material against.",
                 "Add the location dimensions that fix every hole, step or slot from one datum face "
                 "rather than from each other, so errors do not add up.",
                 "Add the size dimensions - the diameter of each hole, the radius of each fillet - "
                 "each once only.",
                 "Draw the extension lines first, then the dimension lines, then the arrowheads, and "
                 "write the figures last so that nothing is written twice.",
                 "Take every dimension off the object or the drawing, never off a scaled printout, "
                 "and check that no dimension is missing and none is repeated.")
         + why("A drawing that is fully dimensioned needs no scale: the reader never measures the "
               "print, only reads the numbers. That is why one missing dimension stops production "
               "and one repeated dimension invites two different readings.")
         + pit("Dimensioning to a hidden line, or leaving the dimension line inside the object, "
               "forces the reader to measure - both are rejected in the exam and in the shop.")
         + check("Every feature has a size and a location, nothing is dimensioned twice, and the "
                 "figures are all readable from the bottom or the right of the sheet."),
         diagram="u1_dim", syllabus_item="1.2"),
    card("1.2 Plane scale and the representative fraction",
         h4("The one number that makes a drawing readable")
         + p("A drawing is nearly always smaller than the object, so every length is multiplied by "
             "the same fraction. The <b>representative fraction</b> is the drawing length divided by "
             "the actual length, and it is written under the scale on every sheet:")
         + h4("Formulae")
         + ul("<b>RF = drawing length / actual length</b>, and it is always written as 1 : 50, not "
              "as 1/50, so that both terms carry a unit-free ratio.",
              "<b>Length of the scale on paper = RF x maximum distance to be measured.</b>",
              "For RF 1:50 and a maximum distance of 6 m: length = (1/50) x 6 x 1000 = 120 mm.",
              "A plain scale reads two units - metres and decimetres; a diagonal scale reads three - "
              "metres, decimetres and centimetres.")
         + h4("Worked example - a plain scale of RF 1:50 to read 6 m and 1 dm")
         + steps("Convert the maximum distance to the same unit as the drawing: 6 m = 6000 mm.",
                 "Length of scale = 6000 / 50 = 120 mm. Draw a rectangle 120 mm long and 5 mm high "
                 "and mark its centre line.",
                 "Divide the length into six equal parts of 20 mm each; each part represents 1 m.",
                 "Subdivide the leftmost part into ten equal parts of 2 mm each; each of these "
                 "represents 1 dm.",
                 "Write 0 at the first division, then 1, 2, 3, 4 and 5 to the right - the metres - "
                 "and 0.1, 0.2 ... 0.9 to the left of zero, reading outwards, for the decimetres.",
                 "Write the RF as 1:50 and the units as metres and decimetres below the scale.")
         + why("The scale is drawn once and used for every length on the sheet: a distance on the "
               "drawing is picked up with the divider, laid on the scale, and read as metres plus "
               "decimetres without any arithmetic - which is exactly what a scale is for.")
         + check("The whole length must be RF x the largest distance, and the smallest division must "
                 "equal the smallest distance to be read: 2 mm for 1 dm at 1:50.")
         + pit("Forgetting to convert metres to millimetres makes the scale 1000 times too short; "
               "checking that the 6 m scale is 120 mm long catches it at once."),
         diagram="u1_scale", syllabus_item="1.2"),
]})

NOTES.append({"title": tr("3. Regular Polygons, Step by Step"),
              "items": [
    card("1.3 The general method - any polygon in a circle",
         h4("One construction for five sides, seven sides or eleven")
         + p("A regular polygon has every side equal and every angle equal, so all its corners lie on "
             "one circle. The general method inscribes a polygon of any number of sides n in a circle "
             "of known radius, and the exam accepts it for any polygon because no particular method "
             "may be asked.")
         + steps("Draw the circle of radius R about the centre O, and draw the vertical diameter AB "
                 "with the T-square and set square.",
                 "Divide AB into n equal parts with the divider - for a pentagon, five parts; number "
                 "the division points 1, 2, 3 ... from A downwards.",
                 "With centre A and radius equal to the diameter AB, draw an arc on each side of AB "
                 "to cut the horizontal centre line at P and Q.",
                 "From P draw a straight line through the second division point and produce it to "
                 "cut the circle at C; from Q draw a line through the same second division point to "
                 "cut the circle at D. C and D are two corners of the polygon.",
                 "Step the chord CD round the circle with the divider - it goes exactly n times - and "
                 "join the points in order to get the polygon.",
                 "Ink the outline thick, leave the construction thin, and letter the side length.")
         + h4("The sizes you can predict before you start")
         + ul("Central angle of a regular polygon = 360 / n degrees; for a pentagon, 72 degrees.",
              "Side of a polygon inscribed in a circle of diameter D: s = D x sin(180 / n).",
              "Interior angle = (n - 2) x 180 / n; for a pentagon, 108 degrees.",
              "Circumradius of a pentagon of side s: R = s / (2 sin 36) = 0.8507 s.")
         + why("The two arcs from A and Q deliver the corner D because the chord of a circle is set "
               "out by equal angles at the circumference; the construction is a graphical solution of "
               "the same trigonometry listed above.")
         + check("The last side must close exactly on the first point. If it overlaps by 2 mm, the "
                 "divider slipped - divide again rather than average the error."),
         diagram="u1_poly", syllabus_item="1.3"),
    card("1.3 Hexagon and octagon - the fast constructions",
         h4("When n divides 360 or 90, use the set square")
         + p("A hexagon and an octagon can be built far faster than by the general method because 60 "
             "and 45 degrees are the angles of the two set squares. Both constructions are shown in "
             "the diagram and both are acceptable in the exam.")
         + h4("Hexagon in a circle, radius R - across corners given")
         + steps("Draw the circle of radius R and one horizontal centre line.",
                 "Without changing the compass from R, step round the circle from any point on it: "
                 "each chord of a circle is equal to R at the centre when the angle is 60 degrees, "
                 "so the divider goes exactly six times and closes.",
                 "Join the six points; the hexagon is complete.",
                 "For a hexagon given across flats F instead, draw a circle of radius F / 1.732, "
                 "then draw the six sides at 60 degrees from the flats.")
         + h4("Octagon in a square of side a")
         + steps("Draw the square of side a and both diagonals; their crossing is the centre.",
                 "With the centre as centre and radius equal to half the diagonal, draw the "
                 "circumscribing circle - it touches the four sides of the square.",
                 "With each corner of the square as centre and radius equal to a / 2, draw an arc "
                 "cutting the two sides that meet at that corner; repeat at all four corners.",
                 "Join the eight points in order: four on the sides of the square and four on the "
                 "circle where the diagonals cut it.",
                 "Check that all eight sides measure 0.414 a, which is the side of a regular octagon "
                 "inscribed in a square of side a.")
         + why("The hexagon works because a chord equal to the radius subtends exactly 60 degrees at "
               "the centre, and six 60 degree chords fill the circle. The octagon works because the "
               "corner trimmed off is an isosceles right triangle whose legs are a / 2.")
         + pit("Opening the compass while stepping round the hexagon closes the figure on a gap or "
               "an overlap; set the radius once, and never change it until the six points are marked."),
         diagram="u1_hex", syllabus_item="1.3"),
]})

_PRACTICE = [
    ("Lay out an A2 drawing sheet, ready to start a problem.", 4,
     [h4("What the sheet must carry")
      + p("A2 is 420 x 594 mm and is used in the landscape position. The layout is fixed by BIS SP 46, "
          "so it is drawn first, in 2H thin lines, and inked only at the end."),
      h4("Construction, step by step")
      + ol("Draw the trimming outline 420 x 594 mm and check both diagonals with the scale; a sheet "
           "that is not square cannot be corrected later.",
           "Draw the border 10 mm inside the trimming edge on the top, right and bottom, and 20 mm "
           "on the left. The left margin is the filing margin and nothing is drawn in it.",
           "Draw the title block in the bottom right corner, 65 mm wide and 30 mm high, with its "
           "right and bottom edges on the border.",
           "Divide the block into rows and write: name of the institute, title of the problem, name "
           "and roll number of the student, class and division, subject and code, scale, date, and "
           "sheet number.",
           "Write the title in 7 mm capitals and every other entry in 5 mm capitals, using HB pencil "
           "and single-stroke letters.",
           "Leave the space above the title block free for the view that will be drawn, and check "
           "that there is room to dimension it."),
      p("<b>Answer.</b> A2 landscape, 10 mm border on three sides and 20 mm filing margin on the "
        "left, a 65 x 30 mm title block in the bottom right corner, all construction in 2H and all "
        "lettering in HB - the sheet is then ready for the first view.")]),
    ("Draw a plain scale of RF 1:50 to read metres and decimetres, long enough for 6 m. Show a "
     "distance of 3.7 m on it.", 5,
     [h4("Given and required")
      + p("RF = 1:50, maximum distance = 6 m, and the scale must read to 1 dm = 0.1 m."),
      h4("Construction, step by step")
      + ol("Convert the maximum distance into millimetres: 6 m = 6000 mm.",
           "Length of scale = RF x maximum distance = (1/50) x 6000 = 120 mm.",
           "Draw a rectangle 120 mm long and 5 mm high, and a centre line through it.",
           "Divide the 120 mm into six equal parts of 20 mm; each part is 1 m.",
           "Divide the leftmost 20 mm part into ten equal parts of 2 mm; each part is 1 dm = 0.1 m.",
           "Mark 0 at the first division, 1, 2, 3, 4 and 5 to the right for the metres, and 0.1, "
           "0.2 ... 0.9 to the left of zero for the decimetres.",
           "Write RF = 1:50 and the units - metres and decimetres - below the scale."),
      h4("Showing 3.7 m")
      + p("Set the divider from 0 to 3 on the right (3 m), then add 0.7 m by opening it from the 0.7 "
          "mark on the left to the 3 m mark: the total span is 3.7 m. On this scale 3.7 m measures "
          "3.7 x 20 = 74 mm."),
      h4("Check")
      + p("The whole scale must be 120 mm for 6 m, and the smallest division 2 mm for 0.1 m. Both "
          "confirm that the RF and the arithmetic are right before any ink is used."),
      p("<b>Answer.</b> A 120 mm plain scale, six 20 mm metre divisions, the leftmost split into ten "
        "2 mm decimetre parts, graduated 0 to 5 m to the right of zero and 0.1 to 0.9 m to the left; "
        "3.7 m measures 74 mm on it.")]),
    ("Dimension the stepped plate shown, fully and as per BIS SP 46.", 5,
     [h4("The plate")
      + p("A plate 100 mm long, 60 mm wide and 20 mm thick has a step 40 mm from the left end, a "
          "Ø 20 mm hole whose centre is 25 mm from the left end and 30 mm from the bottom edge, a "
          "R 10 mm fillet at the top right corner and a 45 x 5 mm chamfer at the bottom left."),
      h4("Construction, step by step")
      + ol("Draw the three overall dimensions first - 100, 60 and 20 - outside the outline, 10 mm "
           "away from it, so that every other dimension sits inside them.",
           "Choose the left face and the bottom face as the datum and give the location of the step "
           "and of the hole from those two faces only: 40 for the step, 25 and 30 for the hole "
           "centre.",
           "Give the size of each feature once: Ø 20 with a leader to the circle, R 10 with a leader "
           "to the fillet, and 45 x 5 written as a note for the chamfer.",
           "Draw the extension lines 2 mm clear of the outline and 3 mm past the dimension line, "
           "then the thin dimension lines, then filled arrowheads 3 mm long.",
           "Write each figure 3 mm high, 1 mm above its dimension line, all readable from the bottom "
           "or from the right of the sheet.",
           "Check the list: every feature has a size and a location, no dimension is repeated, and "
           "no dimension is attached to a hidden line."),
      h4("What is deliberately not dimensioned")
      + p("The position of the fillet centre is implied by R 10 and the two faces it touches, and "
          "the chamfer is fully described by 45 x 5, so neither needs a second figure. Adding them "
          "is over-dimensioning, which is an error, not extra care."),
      p("<b>Answer.</b> Three overall dimensions 100 x 60 x 20 outside the outline; location "
        "dimensions 40, 25 and 30 from the datum faces; sizes Ø 20, R 10 and 45 x 5 led once each; "
        "all figures 3 mm high, unidirectional, with 2 mm gaps at the outline.")]),
    ("Construct a regular pentagon of 40 mm side by the general method.", 5,
     [h4("Before drawing, predict the answer")
      + p("Central angle = 360 / 5 = 72 degrees; interior angle = 108 degrees; circumradius "
          "R = 40 / (2 sin 36) = 40 / 1.1756 = 34.03 mm. So the pentagon fits in a circle of radius "
          "34 mm, which is what the construction draws."),
      h4("Construction, step by step")
      + ol("Draw a circle of radius 34 mm about the centre O, and the vertical diameter AB.",
           "Divide AB into five equal parts with the divider, and number the points 1 to 4 from A.",
           "With centre A and radius equal to the diameter (68 mm), draw an arc on each side of AB "
           "to cut the horizontal centre line at P and Q.",
           "Join P to the second division point and produce it to cut the circle at C; join Q to the "
           "same division point and produce it to cut the circle at D.",
           "Step the chord CD round the circle with the divider; it closes exactly after five steps "
           "and gives the vertices C, D, E, F, G.",
           "Join the five vertices in order in a thick line, and ink the construction in thin lines.",
           "Measure one side: it must read 40 mm. If it does not, the division of AB was inaccurate, "
           "not the stepping."),
      h4("Checking the angle")
      + p("At every corner the interior angle must measure 108 degrees. A quick check with the "
          "protractor at C and D is enough to catch a wrong division point."),
      p("<b>Answer.</b> A pentagon of 40 mm side inscribed in a circle of radius 34.03 mm, built from "
        "the five-part division of the diameter and the two arcs of radius 68 mm from A; every side "
        "measures 40 mm and every angle 108 degrees.")]),
    ("Construct a regular hexagon of 60 mm across flats by the set-square method.", 4,
     [h4("The two sizes of a hexagon")
      + p("Across flats (AF) is the distance between two opposite sides; across corners (AC) is the "
          "distance between two opposite corners. For a regular hexagon AF = 1.732 R and AC = 2 R, "
          "and the side equals R."),
      h4("Construction, step by step")
      + ol("From AF = 60 mm, find the circumradius: R = 60 / 1.732 = 34.64 mm, and the side = "
           "34.64 mm. Across corners = 2 x 34.64 = 69.3 mm.",
           "Draw the two centre lines crossing at O at 90 degrees, and set out 34.64 mm each way "
           "along both, giving the top, bottom, left and right points of the circle.",
           "Draw the circle of radius 34.64 mm, then the two horizontal flats 30 mm above and below "
           "O, each tangent to the circle.",
           "Place the 30-60 set square on the T-square with its 60 degree edge through the top "
           "point, and draw the two sloping sides to meet the flats.",
           "Turn the set square over and repeat through the bottom point, giving the remaining two "
           "sloping sides.",
           "Measure the two pairs of parallel sides: each flat must be 34.64 mm and the flats "
           "60 mm apart."),
      h4("Why the set square is allowed")
      + p("Every side of a regular hexagon lies at 60 degrees to the next, and 60 degrees is exactly "
          "an edge of the 30-60 set square, so the construction needs no compass work after the "
          "circle."),
      p("<b>Answer.</b> A hexagon with 60 mm between opposite flats, 69.3 mm between opposite "
        "corners, six sides of 34.64 mm, drawn with the circle and the 30-60 set square.")]),
    ("Construct a regular octagon inside a square of 60 mm side.", 5,
     [h4("The number to remember")
      + p("In a square of side a the largest regular octagon has side 0.4142 a. For a = 60 mm the "
          "side is 24.85 mm, and the four corner triangles trimmed off are isosceles right triangles "
          "with legs 60 - 24.85 = 17.6 mm on each side of the corner, i.e. 60 x 0.293 = 17.6 mm."),
      h4("Construction, step by step")
      + ol("Draw the square ABCD of 60 mm side and both diagonals; their crossing is the centre O.",
           "With centre O and radius 30 mm (half the diagonal is 42.4 mm, but the circle that "
           "touches the sides is the easier reference) draw the circle inscribed in the square.",
           "With each corner as centre and radius 30 mm, draw an arc cutting the two sides that meet "
           "at that corner; mark the eight points so produced, two on each side.",
           "Join the eight points in order: the four mid-side points of the circle and the four "
           "points where the diagonals cut the circle.",
           "Measure a side: it must read 24.85 mm, and 0.4142 x 60 = 24.85 mm confirms it.",
           "Ink the octagon thick and leave the square and the diagonals thin."),
      h4("Second acceptable method")
      + p("Mark 17.6 mm from each corner along both sides, join the neighbouring marks across the "
          "corner, and the eight points are obtained without the circle. Both methods are accepted; "
          "the second is faster and the first shows the geometry."),
      p("<b>Answer.</b> A regular octagon of 24.85 mm side inside the 60 mm square, with four sides "
        "on the square and four sides cutting the corners, each corner trimmed by 17.6 mm.")]),
    ("Draw a regular polygon of seven sides in a circle of 70 mm diameter and state its side.",
     3,
     [h4("Prediction")
      + p("Side s = D sin(180/7) = 70 x sin 25.714 degrees = 70 x 0.4339 = 30.37 mm; central angle = "
          "360/7 = 51.43 degrees; interior angle = (7 - 2) x 180 / 7 = 128.57 degrees."),
      h4("Construction, step by step")
      + ol("Draw the circle of radius 35 mm and the vertical diameter AB.",
           "Divide AB into seven equal parts with the divider and number them from A.",
           "With centre A and radius 70 mm, cut the horizontal centre line on both sides at P and Q.",
           "Join P and Q to the second division point and produce them to meet the circle at C and D.",
           "Step the chord CD round the circle seven times; it must close on the starting point.",
           "Join the seven vertices; measure a side and compare it with 30.37 mm."),
      p("<b>Answer.</b> A heptagon in a 70 mm circle with side 30.37 mm, central angle 51.43 degrees "
        "and interior angle 128.57 degrees.")]),
]

EQUATIONS = [
    {"title": tr("Scale"),
     "items": [
         {"name": tr("Representative fraction"),
          "f": "RF = drawing length / actual length = 1 : n",
          "terms": tr("Written under the scale of every drawing; both lengths in the same unit, so "
                      "the ratio has no unit.")},
         {"name": tr("Length of the scale"),
          "f": "L = RF x maximum distance to be measured",
          "terms": tr("For RF 1:50 and 6 m, L = (1/50) x 6000 = 120 mm. This is the length drawn on "
                      "the paper, not the length of the object.")},
         {"name": tr("Smallest division"),
          "f": "smallest division = RF x smallest distance to be read",
          "terms": tr("At 1:50 a decimetre is 100 / 50 = 2 mm on paper, which is the practical limit "
                      "for a plain scale.")},
     ]},
    {"title": tr("Regular polygons"),
     "items": [
         {"name": tr("Central angle"),
          "f": "theta = 360 / n degrees",
          "terms": tr("The angle each side subtends at the centre: 72 degrees for a pentagon, "
                      "60 degrees for a hexagon, 45 degrees for an octagon.")},
         {"name": tr("Side from the diameter"),
          "f": "s = D sin(180 / n)",
          "terms": tr("For n = 5 and D = 70 mm, s = 70 sin 36 = 41.15 mm; this is the number the "
                      "construction must reproduce.")},
         {"name": tr("Interior angle"),
          "f": "angle = (n - 2) x 180 / n",
          "terms": tr("108 degrees for a pentagon, 120 degrees for a hexagon, 135 degrees for an "
                      "octagon.")},
         {"name": tr("Pentagon circumradius"),
          "f": "R = s / (2 sin 36) = 0.8507 s",
          "terms": tr("A pentagon of 40 mm side needs a circle of radius 34.03 mm.")},
         {"name": tr("Hexagon, across flats and corners"),
          "f": "AF = 1.732 R,  AC = 2 R,  side = R",
          "terms": tr("Across flats is 1.732 times the circumradius; across corners is twice it, and "
                      "equals twice the side.")},
         {"name": tr("Octagon in a square"),
          "f": "s = 0.4142 a,  corner trim = 0.293 a",
          "terms": tr("Inside a square of side a the largest regular octagon has side 0.4142 a and "
                      "each corner is trimmed by 0.293 a.")},
     ]},
    {"title": tr("BIS SP 46 drawing practice"),
     "items": [
         {"name": tr("Line thickness"),
          "f": "thick : thin = 2 : 1 (0.5 mm : 0.25 mm)",
          "terms": tr("Only two thicknesses on one drawing; visible outlines thick, everything that "
                      "helps to read them thin.")},
         {"name": tr("Arrowhead proportion"),
          "f": "length : width = 3 : 1",
          "terms": tr("A filled arrowhead about 3 mm long and 1 mm wide, touching the extension line.")},
         {"name": tr("Dimension figure"),
          "f": "height 3 mm, 1 mm above the dimension line",
          "terms": tr("Unidirectional system: every figure readable from the bottom or from the right "
                      "of the sheet; millimetres, no unit symbol.")},
         {"name": tr("Extension line clearances"),
          "f": "2 mm gap at the object, 3 mm beyond the arrow",
          "terms": tr("The gap keeps the outline clean; the overrun shows where the dimension ends.")},
     ]},
]

VIVA = [
    {"title": tr("Instruments and the sheet"),
     "items": [
         {"q": tr("Why is the filing margin 20 mm, not 10 mm?"),
          "a": tr("Because the sheet is punched and bound on the left edge, and the punched holes "
                  "would cut into any drawing inside a 10 mm border. The other three sides carry the "
                  "10 mm border, the title block sits in the bottom right corner, and the margin is "
                  "never used for a view or a dimension.")},
         {"q": tr("What is the difference between 2H, H and HB pencils on a drawing?"),
          "a": tr("2H is hard and light, so it is used for construction lines that must not print "
                  "black in a copy; H is used for the final outlines, because it is dark enough to "
                  "reproduce and still erases cleanly; HB is used for lettering and dimension figures, "
                  "where a slightly darker and softer line reads better. Using HB for construction "
                  "makes the sheet dirty and hard to correct.")},
         {"q": tr("What are the A-series paper sizes and which is used for the practical?"),
          "a": tr("A0 is 841 x 1189 mm and each size is half the one before: A1 594 x 841, A2 420 x "
                  "594, A3 297 x 420, A4 210 x 297. A2 is used for the drawing sheets of this "
                  "subject, and the problems are first worked in the sketch book.")},
         {"q": tr("What does the title block contain?"),
          "a": tr("The name of the institute, the title of the problem, the name and roll number of "
                  "the student, the class and division, the subject and its code, the scale of the "
                  "drawing, the date and the sheet number. It is 65 mm wide and sits in the bottom "
                  "right corner, so a reader knows at once what the sheet is and at what scale.")},
     ]},
    {"title": tr("Lines and dimensioning"),
     "items": [
         {"q": tr("Why are hidden edges drawn dashed thin instead of continuous thin?"),
          "a": tr("Because a continuous thin line already means a dimension, an extension line or a "
                  "hatch. If a hidden edge used the same line, the reader could not tell a hole "
                  "behind a face from a dimension. A dashed thin line is reserved for what is hidden, "
                  "and the dashes start and end with a dash so that the extent is clear.")},
         {"q": tr("What is the difference between a centre line and a cutting plane line?"),
          "a": tr("A centre line is chain thin and runs through the centre of a circle or along the "
                  "axis of a cylinder, projecting 2 to 3 mm beyond the outline. A cutting plane line "
                  "is chain thin but thick at its two ends, with arrows showing the direction of "
                  "sight and letters naming the section, because it tells the reader where the object "
                  "has been cut.")},
         {"q": tr("Why is a dimension never placed on a hidden line?"),
          "a": tr("Because the dimension would be ambiguous - the reader cannot see the edge it "
                  "refers to - and because the dashes and the arrowheads would overlap and become "
                  "unreadable. The view is arranged, or a section is taken, so that the edge is "
                  "visible; only then is it dimensioned.")},
         {"q": tr("What does Ø 20, R 10, □ 15 and 45 x 5 mean?"),
          "a": tr("Ø 20 is a diameter of 20 mm, R 10 is a radius of 10 mm, □ 15 is a square face of "
                  "15 mm side, and 45 x 5 is a chamfer 45 degrees to the axis and 5 mm long. All are "
                  "written without a unit symbol, because every dimension on the sheet is in "
                  "millimetres.")},
         {"q": tr("What is a datum and why are location dimensions taken from it?"),
          "a": tr("A datum is the face, edge or axis chosen as the zero for measurements - usually "
                  "the machined face that will locate the part in the fixture. Taking every location "
                  "dimension from that one face stops the tolerances of several dimensions adding up, "
                  "which is what happens when each hole is dimensioned from the previous one.")},
     ]},
    {"title": tr("Scales and polygons"),
     "items": [
         {"q": tr("What is a reducing scale and what is an enlarging scale?"),
          "a": tr("A reducing scale draws the object smaller than it is, so the RF is less than one "
                  "- 1:2, 1:50, 1:100 - and it is what every building or machine drawing uses. An "
                  "enlarging scale draws it bigger, so the RF is more than one - 2:1 or 10:1 - and "
                  "it is used for a watch part or a printed circuit detail. Full size is 1:1. The "
                  "RF always starts with 1, so 1:50 and 50:1 are two entirely different drawings.")},
         {"q": tr("What is the representative fraction?"),
          "a": tr("The ratio of the drawing length to the actual length, written 1 : 50 and read as "
                  "one millimetre on the paper for every fifty millimetres of the object. It is the "
                  "number that makes the whole sheet readable at a glance, and it is written under "
                  "the scale and in the title block.")},
         {"q": tr("When do you use a plain scale and when a diagonal scale?"),
          "a": tr("A plain scale reads two units - metres and decimetres - and is used when the "
                  "smallest distance can be shown by a 2 mm division. A diagonal scale reads three "
                  "units, because the diagonal divides a small division into ten more parts by "
                  "similar triangles, and is used when the third unit would otherwise be smaller than "
                  "a millimetre on the paper.")},
         {"q": tr("Why does the hexagon construction work without any arithmetic?"),
          "a": tr("Because a chord equal to the radius subtends exactly 60 degrees at the centre, so "
                  "six such chords fill 360 degrees. Setting the compass to R and stepping round the "
                  "circle therefore marks all six corners exactly, and the chord stepped is also the "
                  "length of the side.")},
         {"q": tr("How do you check a polygon before inking it?"),
          "a": tr("Measure one side against the value from s = D sin(180/n), and check one interior "
                  "angle against (n - 2) x 180 / n. In the general method the last step must close "
                  "exactly on the first point; a gap or an overlap means the diameter was divided "
                  "inaccurately, so the division is repeated rather than the error averaged out.")},
     ]},
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)
