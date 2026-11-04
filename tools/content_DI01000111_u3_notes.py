"""DI01000111 Engineering Graphics - Unit 3: Projections of Points and Lines.

GTU 3.1-3.2, 5 h, 20 %, 14 marks, CO3. English only. Every construction is a numbered procedure on
the sheet: draw XY, mark the distances, project square to XY, and check the pair sits on one projector.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from content_DI01000111_u1_notes import (tr, p, h4, ul, ol, table, steps, why, check, pit,  # noqa
                                        card)

SOURCES = [
    ("GTU DI01000111 Engineering Graphics syllabus (uploaded PDF, w.e.f. 2024-25)",
     "https://syllabus.gtu.ac.in/"),
    ("N. D. Bhatt - Elementary Engineering Drawing, Charotar Publishing House, Anand (chapters 9-10: "
     "projections of points and straight lines)", "https://www.charotarbookstall.com/"),
    ("P. S. Gill - A Text Book of Engineering Drawing, S. K. Kataria & Sons, Delhi (points, lines "
     "and traces)", "https://www.skkatariaandsons.com/"),
    ("BIS SP 46 - Engineering drawing practice: first-angle projection and the reference line",
     "https://www.bis.gov.in/"),
]

NOTES = [
    {"title": tr("1. The Reference Planes and the Projection of Points"),
     "items": [
         card("3.1 Two planes, four quadrants, one XY line",
              h4("What the two planes are")
              + p("The <b>horizontal plane (HP)</b> is the flat plane you look down on and the "
                  "<b>vertical plane (VP)</b> is the upright plane you look at. They meet at right "
                  "angles in the <b>reference line XY</b>. In the drawing both planes are opened out "
                  "flat, so XY becomes one horizontal line: everything drawn above XY is on the VP "
                  "(an <b>elevation</b>, the view from the front) and everything below XY is on the "
                  "HP (a <b>plan</b>, the view from above).")
              + h4("The notation you must use")
              + ul("A point in space is a capital letter: <b>A</b>.",
                   "Its elevation is the same letter with a dash: <b>a'</b>, always above or below "
                   "XY on the VP side.",
                   "Its plan is the plain small letter: <b>a</b>, on the HP side.",
                   "A point and both its views lie on one thin <b>projector</b> drawn square to XY - "
                   "this is the one rule that never breaks.")
              + h4("The four quadrants")
              + table(["quadrant", "the point is", "elevation a'", "plan a"], [
                  ("first", "above HP, in front of VP", "above XY", "below XY"),
                  ("second", "above HP, behind VP", "above XY", "above XY"),
                  ("third", "below HP, behind VP", "below XY", "above XY"),
                  ("fourth", "below HP, in front of VP", "below XY", "below XY"),
              ])
              + steps("Draw XY as a thin line across the middle of the sheet and letter it X at the "
                      "left and Y at the right.",
                      "Measure the height of the point above HP along a perpendicular to XY and mark "
                      "a' there: above XY for a point above HP, below XY for one below HP.",
                      "On the same perpendicular measure the distance in front of VP and mark a: "
                      "below XY for a point in front of VP, above XY for one behind it.",
                      "Darken only the two letters and the short projector between them; XY, the "
                      "projector and the construction stay thin.",
                      "Check the pair: both views on one line square to XY, each at the right "
                      "distance from XY, and the quadrant written in words beside the point.")
              + why("Only two measurements fix a point - its height and its depth - and each of the "
                    "two planes can show only one of them truly. The elevation shows height, the plan "
                    "shows depth, and the projector is the same vertical line seen from both sides.")
              + pit("Marking a plan above XY for a point in the first quadrant. Above HP puts the "
                    "elevation above XY; in front of VP puts the plan below XY. Learn the two "
                    "sentences, not the picture."),
              diagram="u3_quadrants", syllabus_item="3.1"),

         card("3.1 Six points and how to read a drawing backwards",
              h4("The set of points used in this unit")
              + table(["point", "position", "a' from XY", "a from XY"], [
                  ("A", "25 above HP, 30 in front of VP", "25 above", "30 below"),
                  ("B", "20 below HP, 35 in front of VP", "20 below", "35 below"),
                  ("C", "30 above HP, 25 behind VP", "30 above", "25 above"),
                  ("D", "15 below HP, 40 behind VP", "15 below", "40 above"),
                  ("E", "on HP, 25 in front of VP", "on XY", "25 below"),
                  ("F", "on VP, 20 above HP", "20 above", "on XY"),
              ])
              + steps("Draw XY once for all six points and put the six projectors in a row, each "
                      "square to XY, spaced so the letters will not touch.",
                      "For every point mark the elevation first, measuring the height above or below "
                      "HP, and letter it with a dash.",
                      "Mark the plan on the same projector, measuring the depth in front of or "
                      "behind VP, and letter it plain.",
                      "A point that lies on a plane throws one view on to XY itself: E on HP puts "
                      "e' on XY, F on VP puts f on XY.",
                      "Number the answers in words under each point, as in the table, so the "
                      "drawing states the quadrant it belongs to.")
              + h4("Reading a drawing backwards - the exam favourite")
              + p("When the question gives you the two views and asks for the position, read the "
                  "signs and the distances, never the picture: <b>a' above XY</b> means the point is "
                  "that far above HP; <b>a below XY</b> means it is that far in front of VP. Both "
                  "views above XY is the second quadrant, both below XY is the fourth.")
              + steps("Measure the distance of a' from XY and write it as a height: above XY = above "
                      "HP, below XY = below HP.",
                      "Measure the distance of a from XY and write it as a depth: below XY = in front "
                      "of VP, above XY = behind VP.",
                      "Combine the two sentences to name the quadrant, then state the point in the "
                      "form 'A is 25 mm above HP and 30 mm in front of VP'.",
                      "As a proof, draw the projector: if a and a' are not on one line square to XY, "
                      "the drawing you were given is wrong.")
              + why("The two planes are the only measuring sticks you have; every question about a "
                    "point is really a question about two distances from XY and the side each one "
                    "falls on.")
              + pit("Calling the second quadrant 'behind HP'. Behind belongs to VP, below belongs to "
                    "HP; mixing the words costs marks even when the drawing is right."),
              diagram="u3_points", syllabus_item="3.1"),
     ]},

    {"title": tr("2. Projections of Lines: Inclinations and True Length"),
     "items": [
         card("3.2 The three positions worth memorising",
              h4("A line is fixed by its end points")
              + p("A straight line is projected by projecting both ends and joining the two views. "
                  "Its true length appears only in a view taken parallel to it, so the whole of this "
                  "unit is one idea: put the line in a position where one view looks along it and the "
                  "other looks across it, then read the true length off the view that sees it flat.")
              + table(["position of the line", "elevation", "plan"], [
                  ("parallel to both HP and VP", "true length, parallel to XY",
                   "true length, parallel to XY"),
                  ("perpendicular to HP, parallel to VP", "a point", "true length, square to XY"),
                  ("perpendicular to VP, parallel to HP", "true length, square to XY", "a point"),
                  ("parallel to HP, inclined to VP", "shortened to L cos of the angle",
                   "true length at the true angle"),
                  ("parallel to VP, inclined to HP", "true length at the true angle",
                   "shortened to L cos of the angle"),
              ])
              + steps("Draw XY, then mark the first end from its two distances exactly as if it were "
                      "a point.",
                      "Decide which plane the line is parallel to: the view on that plane is the "
                      "true-length view and the other view comes out shortened.",
                      "Draw the true-length view at the given angle, mark the second end there, and "
                      "drop or raise a projector from it.",
                      "Complete the shortened view along a line parallel to XY through the first "
                      "end, and check its length by L cos of the angle.",
                      "Ink the two views of the line, keep the projectors and the locus lines thin, "
                      "and write the true length and the angle beside the true-length view.")
              + why("A line perpendicular to a plane is seen end-on, so it collapses to a point in "
                    "that view; a line parallel to a plane is seen flat, so that view is a true "
                    "length. Every construction in this unit is a way of arranging one of those two "
                    "happy accidents.")
              + pit("Drawing a line 60 mm long in both views when it is inclined: only the view of "
                    "the plane it is parallel to may show the full 60 mm."),
              diagram="u3_line_basic", syllabus_item="3.2"),

         card("3.2 Inclined to HP and parallel to VP",
              h4("AB = 70 mm at 30 degrees to HP, A 20 mm above HP and 25 mm in front of VP")
              + p("Because the line is parallel to VP, no depth is lost and the elevation is the "
                  "true-length view: <b>a'b' = 70 mm at 30 degrees to XY</b>. The plan is then just "
                  "that view dropped down, parallel to XY and shortened to 70 cos 30 = 60.6 mm.")
              + steps("Draw XY and mark a' 20 mm above it and a 25 mm below it, on one projector.",
                      "From a' draw a line at 30 degrees to XY, 70 mm long, and mark b' at its end - "
                      "this one line is the whole answer for length and angle.",
                      "Drop a projector from b' perpendicular to XY.",
                      "Through a draw a line parallel to XY (the locus of b) and cut it with the "
                      "projector from b' - that gives b, and ab is the plan.",
                      "Measure ab: it must be 60.6 mm and parallel to XY, and b' must stand "
                      "20 + 70 sin 30 = 55 mm above XY.")
              + h4("The numbers to predict before you draw")
              + ul("Elevation: true length 70 mm at 30 degrees, so b' is 55 mm above XY.",
                   "Plan: 70 cos 30 = 60.6 mm, parallel to XY, 25 mm below XY.",
                   "Height gained along the line: 70 sin 30 = 35 mm.",
                   "Both views sit between the same pair of projectors, 60.6 mm apart.")
              + why("Parallel to VP means the VP sees the line without foreshortening in the "
                    "vertical sense: the height it gains and the length it runs are both seen truly, "
                    "so the elevation is the real line. The HP sees only the run, so the plan keeps "
                    "the run and loses the rise.")
              + pit("Making the plan slope as well. With the line parallel to VP the plan must be "
                    "parallel to XY; a sloping plan belongs to a line inclined to VP."),
              diagram="u3_line_hp", syllabus_item="3.2"),

         card("3.2 Inclined to VP and parallel to HP",
              h4("AB = 65 mm at 40 degrees to VP, A 20 mm above HP and 25 mm in front of VP")
              + p("The same argument with the planes swapped: parallel to HP means the plan is the "
                  "true-length view, so the <b>plan is 65 mm at 40 degrees to XY</b>, and the "
                  "elevation is that view lifted up, parallel to XY and shortened to "
                  "65 cos 40 = 49.8 mm.")
              + steps("Draw XY and mark a' 20 mm above it and a 25 mm below it.",
                      "From a draw a line at 40 degrees to XY, 65 mm long, and mark b at its end.",
                      "Raise a projector from b perpendicular to XY.",
                      "Through a' draw a line parallel to XY (the locus of b') and cut it with the "
                      "projector from b - that gives b', and a'b' is the elevation.",
                      "Check: a'b' = 49.8 mm parallel to XY, and both ends keep the same height, so "
                      "the elevation is horizontal.")
              + h4("Where each angle is seen")
              + table(["given in the question", "which view is true length", "which view is "
                       "shortened"], [
                  ("parallel to VP, inclined to HP", "elevation, at the true angle to XY",
                   "plan, parallel to XY, L cos of the angle"),
                  ("parallel to HP, inclined to VP", "plan, at the true angle to XY",
                   "elevation, parallel to XY, L cos of the angle"),
                  ("inclined to both planes", "neither view - both are shortened",
                   "the true length has to be constructed"),
              ])
              + why("The plane that the line is parallel to sees the line square-on, so it can show "
                    "the length and the angle; the other plane sees the line end-on to the tilt and "
                    "can show only the run.")
              + pit("Writing the angle in the elevation when the line is inclined to VP. The angle "
                    "belongs to the plan in this case, and to the elevation only when the line is "
                    "inclined to HP."),
              diagram="u3_line_vp", syllabus_item="3.2"),

         card("3.2 Inclined to both planes - the two-stage construction",
              h4("AB = 80 mm, 35 degrees to HP, plan at 45 degrees to XY, A 20 mm above HP, 25 mm "
                 "in front of VP")
              + p("Neither view can be the true length now, so the line is built in two stages. "
                  "<b>Stage 1</b> parks the line parallel to VP and inclined at 35 degrees to HP, "
                  "where the elevation is honest. <b>Stage 2</b> swings the plan about a through the "
                  "second angle; a swing about a vertical axis cannot change any height, so the "
                  "elevation's second end must stay on the level it reached in stage 1 - the locus "
                  "of b'.")
              + steps("Draw XY, a' 20 mm above it and a 25 mm below it, on one projector.",
                      "Stage 1: from a' draw a'b1' = 80 mm at 35 degrees to XY. This is the true "
                      "length at the true angle to HP.",
                      "Drop a projector from b1' to the locus of b (the line through a parallel to "
                      "XY) and mark b1: ab1 = 65.5 mm is the plan of that parked position.",
                      "Stage 2: with a as centre and radius ab1 draw an arc, and strike the plan at "
                      "45 degrees to XY to get b2. The arc keeps the plan length, so no length is "
                      "lost in the swing.",
                      "Draw the locus of b', the line through b1' parallel to XY. Raise a projector "
                      "from b2 to cut it at b2', the new elevation of the second end.",
                      "Join a to b2 for the final plan and a' to b2' for the final elevation, ink "
                      "them, and leave the stage-1 lines thin and dashed as construction.")
              + h4("What the finished drawing must measure")
              + table(["quantity", "value", "how it comes out"], [
                  ("true length", "80 mm", "a'b1' in stage 1 - the arc and the locus preserve it"),
                  ("angle to HP", "35 degrees", "the elevation of stage 1"),
                  ("plan", "65.5 mm at 45 degrees to XY", "80 cos 35, swung round about a"),
                  ("elevation", "65.2 mm", "46.3 run with the 45.9 rise kept from stage 1"),
                  ("b1' height", "45.9 mm above a'", "80 sin 35"),
              ])
              + why("Rotating the plan about a vertical axis through a keeps every point at its own "
                    "height, and the arc keeps every point at its own distance from a in plan. Those "
                    "two invariants are why the second stage is only a swing on the locus: the "
                    "length and the heights were settled in stage 1 and cannot drift.")
              + check("The elevation's end must lie on the horizontal locus through b1', and b2 "
                      "must lie on the arc of radius ab1 - if either is off, the second stage was "
                      "rotated about the wrong centre.")
              + pit("Swinging the elevation instead of the plan. Stage 2 is always a rotation of the "
                    "plan about a: the elevation is then read off the locus, never rotated itself.")
              + p("<b>What the 45 degrees means.</b> The stage-2 swing is made to the angle given "
                  "with the VP, and that angle is measured on the plan. If a question asks for the "
                  "true inclination of the finished line with VP, it comes from the plan: "
                  "sin (inclination) = (plan length x sin 45) / true length = 65.5 x 0.707 / 80, "
                  "which is 35.4 degrees. Draw the construction as above - that is what the "
                  "examiner expects - and use this line only when the true angle is asked for."),
              diagram="u3_line_both", syllabus_item="3.2"),

         card("3.2 True length, inclinations and traces from the two views",
              h4("The reverse problem: the projections are given")
              + p("Sometimes the plan and the elevation are given and the true length, the true "
                  "angles and the traces are wanted. Take the plan 45 mm long at 30 degrees to XY "
                  "and the elevation 50 mm long at 38.8 degrees to XY, with a' 20 mm above XY and a "
                  "25 mm below it.")
              + steps("Draw XY and the two given views, a' 20 above with the elevation rising, a 25 "
                      "below with the plan falling.",
                      "Drop perpendiculars from b' to the plan line and from b to the elevation line "
                      "to confirm both views share the same run along XY: 45 cos 30 = 39 mm and "
                      "50 cos 38.8 = 39 mm agree, which proves the pair.",
                      "For the true length, set the height difference against the plan: TL squared "
                      "= 45 squared + 31.3 squared, so TL = 54.8 mm.",
                      "True inclination to HP: sin of the angle = rise / TL = 31.3 / 54.8, so the "
                      "line rises at 34.9 degrees. True inclination to VP: sin = depth / TL = "
                      "22.5 / 54.8, so it leans 24.3 degrees.")
              + h4("Traces - where the line meets the two planes")
              + steps("Produce the elevation until it cuts XY and letter that point h'.",
                      "From h' drop a projector to meet the plan produced: that point is the "
                      "<b>horizontal trace HT</b>, the place where the line would hit HP.",
                      "Produce the plan until it cuts XY and letter that point v.",
                      "From v raise a projector to meet the elevation produced: that point is the "
                      "<b>vertical trace VT</b>, where the line would hit VP.",
                      "Ink HT and VT and leave the produced parts of the views thin and dashed.")
              + h4("Rules worth quoting")
              + ul("A line parallel to HP never meets HP, so it has no HT; parallel to VP it has no "
                   "VT - the trace has gone to infinity.",
                   "A line in HP has its HT on the line itself, and a line in VP likewise.",
                   "The HT lies on the plan produced, the VT on the elevation produced, and each "
                   "projects back to XY.",
                   "True length squared = (run along XY) squared + (rise) squared + (depth) squared.")
              + why("A trace is simply a point of the line that happens to lie on one of the planes, "
                    "and a point on a plane has one of its views on XY. That is why the trace is "
                    "found by cutting XY and projecting back into the other view.")
              + pit("Projecting h' upwards. The elevation meets XY at h', and h' is the elevation of "
                    "the HT, so the HT itself is found by dropping down to the plan produced."),
              diagram="u3_traces", syllabus_item="3.2"),
     ]},
]

_PRACTICE = [
    ("Draw the projections of four points and name the quadrant of each: A 25 mm above HP and 30 mm "
     "in front of VP; B 20 mm below HP and 35 mm in front of VP; C 30 mm above HP and 25 mm behind "
     "VP; D 15 mm below HP and 40 mm behind VP.", 5,
     [h4("Given")
      + p("Four points with a height above or below HP and a depth in front of or behind VP. One XY "
          "line carries all four, with the projectors square to it."),
      h4("Construction, step by step")
      + ol("Draw XY across the middle of the sheet and space four projectors along it, square to XY.",
           "A: mark a' 25 mm above XY and a 30 mm below XY on the first projector.",
           "B: mark b' 20 mm below XY and b 35 mm below XY on the second.",
           "C: mark c' 30 mm above XY and c 25 mm above XY on the third - both views above XY, "
           "because the point is behind VP.",
           "D: mark d' 15 mm below XY and d 40 mm above XY on the fourth.",
           "Letter every view and write the quadrant in words under each point."),
      h4("The answers")
      + p("A is in the first quadrant - above HP, in front of VP. B is in the fourth - below HP, in "
          "front of VP. C is in the second - above HP, behind VP. D is in the third - below HP, "
          "behind VP. In every case the pair sits on one projector, each view at its own distance "
          "from XY.")]),

    ("The elevation a' of a point P is 30 mm above XY and its plan p is 40 mm below XY. State the "
     "position of P and its quadrant, then repeat for a point Q whose elevation is 25 mm above XY "
     "and whose plan is 18 mm above XY.", 4,
     [h4("Read the signs first")
      + p("Both views can only be read against XY: a' above XY means the point is above HP, a below "
          "XY means it is in front of VP."),
      h4("Point P")
      + ol("a' is 30 mm above XY, so P is 30 mm above HP.",
           "p is 40 mm below XY, so P is 40 mm in front of VP.",
           "Above HP and in front of VP is the first quadrant.",
           "Write the answer as a sentence: P is 30 mm above HP and 40 mm in front of VP, first "
           "quadrant."),
      h4("Point Q")
      + ol("q' is 25 mm above XY, so Q is 25 mm above HP.",
           "q is 18 mm above XY, so Q is 18 mm behind VP.",
           "Above HP and behind VP is the second quadrant.",
           "Q is 25 mm above HP and 18 mm behind VP, second quadrant."),
      h4("The check")
      + p("On the drawing, both views of P and both views of Q must each lie on a single projector "
          "square to XY. If they do not, the point has been read from the wrong side of XY.")]),

    ("A line AB 60 mm long is parallel to both HP and VP, 25 mm above HP and 30 mm in front of VP. "
     "Draw its projections.", 3,
     [h4("Given")
      + p("A line parallel to both planes keeps both distances, so both views show the true length "
          "of 60 mm and both are parallel to XY."),
      h4("Construction, step by step")
      + ol("Draw XY and mark a' 25 mm above it, a directly below at 30 mm below XY.",
           "Draw a'b' 60 mm long parallel to XY from a'.",
           "Drop projectors from a' and from b' and mark a and b at 30 mm below XY.",
           "Join ab: it is 60 mm and parallel to XY.",
           "Check that the projectors from a' and b' pass through a and b, and that both views "
           "measure 60 mm."),
      h4("The answer")
      + p("Both the elevation a'b' and the plan ab are 60 mm long and parallel to XY, the elevation "
          "25 mm above XY and the plan 30 mm below it. A line in this position is the only one that "
          "shows its true length in both views.")]),

    ("A line AB 70 mm long is inclined at 30 degrees to HP and parallel to VP. Its end A is 20 mm "
     "above HP and 25 mm in front of VP. Draw its projections and state the plan length.", 5,
     [h4("Given")
      + p("Parallel to VP, so the elevation is the true-length view; inclined 30 degrees to HP, so "
          "the elevation rises at 30 degrees to XY. Plan length = 70 cos 30 = 60.6 mm."),
      h4("Construction, step by step")
      + ol("Draw XY and mark a' 20 mm above it and a 25 mm below it on one projector.",
           "From a' draw a line at 30 degrees to XY, mark b' at 70 mm along it - that is the true "
           "length at the true angle.",
           "Drop a projector from b' perpendicular to XY.",
           "Through a draw a line parallel to XY and cut it with the projector from b' to get b.",
           "Join ab and measure it: 60.6 mm, parallel to XY."),
      h4("The numbers")
      + p("b' stands 20 + 70 sin 30 = 55 mm above XY and the plan is 60.6 mm long, so the run along "
          "XY is 60.6 mm and the rise is 35 mm; 60.6 squared + 35 squared = 4900 = 70 squared, which "
          "proves the construction.")]),

    ("A line AB 65 mm long is inclined at 40 degrees to VP and parallel to HP. Its end A is 20 mm "
     "above HP and 25 mm in front of VP. Draw its projections and state the elevation length.", 5,
     [h4("Given")
      + p("Parallel to HP, so the plan is now the true-length view at 40 degrees to XY; the elevation "
          "is parallel to XY and shortened to 65 cos 40 = 49.8 mm."),
      h4("Construction, step by step")
      + ol("Draw XY and mark a' 20 mm above it and a 25 mm below it.",
           "From a draw a line at 40 degrees to XY and mark b 65 mm along it.",
           "Raise a projector from b perpendicular to XY.",
           "Through a' draw a line parallel to XY and cut it with the projector from b to get b'.",
           "Join a'b' and check that it is 49.8 mm and horizontal."),
      h4("The numbers")
      + p("The plan gives the run 65 cos 40 = 49.8 mm and the depth 65 sin 40 = 41.8 mm; the "
          "elevation is 49.8 mm long and stays at 20 mm above XY because both ends are at the same "
          "height. Depth check: 49.8 squared + 41.8 squared = 4225 = 65 squared.")]),

    ("A line AB 80 mm long is inclined at 35 degrees to HP, and its plan is at 45 degrees to XY. Its "
     "end A is 20 mm above HP and 25 mm in front of VP. Draw its projections and give the lengths of "
     "both views.", 6,
     [h4("Given")
      + p("The line is inclined to both planes, so both views are shortened and the construction has "
          "two stages: park the line parallel to VP, then swing the plan."),
      h4("Construction, step by step")
      + ol("Draw XY, a' 20 mm above it, a 25 mm below it, on one projector.",
           "Stage 1: draw a'b1' = 80 mm at 35 degrees to XY - the true length at the true angle to "
           "HP.",
           "Drop a projector from b1' to the locus of b, the line through a parallel to XY, and "
           "mark b1. ab1 = 80 cos 35 = 65.5 mm.",
           "Stage 2: with a as centre and radius 65.5 mm draw an arc, and strike the plan at 45 "
           "degrees to XY to get b2.",
           "Draw the locus of b', the line through b1' parallel to XY, and raise a projector from b2 "
           "to cut it at b2'.",
           "Join a to b2 for the plan and a' to b2' for the elevation; ink both and leave the "
           "stage-1 lines dashed."),
      h4("The numbers")
      + p("Plan 65.5 mm at 45 degrees to XY; elevation 65.2 mm, because the second end keeps its "
          "45.9 mm rise and now stands 46.3 mm along XY, and 46.3 squared + 45.9 squared = 4250. "
          "The true inclination with VP, when asked, is sin = 65.5 x sin 45 / 80, that is 35.4 "
          "degrees.")]),

    ("The plan of a line AB is 45 mm long at 30 degrees to XY and its elevation is 50 mm long, with "
     "a' 20 mm above XY and a 25 mm below it. Find the true length, the true inclinations and both "
     "traces.", 6,
     [h4("Given")
      + p("Both views are given, so the true length and the inclinations have to be built from them, "
          "and the traces are found where the produced views meet XY."),
      h4("Construction, step by step")
      + ol("Draw XY and the two views: a' 20 mm above XY with the elevation rising 50 mm, a 25 mm "
           "below XY with the plan falling 45 mm.",
           "Check the pair: both views must share the run 45 cos 30 = 39 mm and 50 cos 38.8 = 39 mm.",
           "From b' drop a perpendicular to the level of a and measure the rise 31.3 mm; from b drop "
           "one to the level of a and measure the depth 22.5 mm.",
           "True length = square root of (39 squared + 31.3 squared + 22.5 squared) = 54.8 mm.",
           "True inclination to HP: sin = 31.3 / 54.8 = 0.571, so 34.9 degrees. True inclination to "
           "VP: sin = 22.5 / 54.8 = 0.411, so 24.3 degrees.",
           "Produce the elevation to cut XY at h' and drop a projector to the plan produced - that "
           "is HT, 10.7 mm below XY on the plan side.",
           "Produce the plan to cut XY at v and raise a projector to the elevation produced - that "
           "is VT, 14.9 mm below XY on the elevation side - the produced line has dipped below HP "
           "as well as behind VP."),
      h4("The answers")
      + p("True length 54.8 mm, inclined 34.9 degrees to HP and 24.3 degrees to VP. HT lies 10.7 mm "
          "below XY on the plan produced and VT 14.9 mm below XY on the elevation produced, because "
          "the line produced backwards goes below HP as well as behind VP. Both traces are finite "
          "because the line is inclined to both planes.")]),
]

EXAM = [{"q": tr(q), "marks": m} for q, m, _parts in _PRACTICE]
PRACTICE_ANSWERS = [tr("".join(parts)) for _q, _m, parts in _PRACTICE]
LESSON_COUNT = sum(len(s["items"]) for s in NOTES)

EQUATIONS = [
    {"title": tr("Positions of a point"), "items": [
        {"name": tr("Elevation from HP"), "f": "a' distance from XY = height above or below HP",
         "terms": tr("Measured on a projector square to XY: above XY for a point above HP, below XY "
                     "for a point below HP.")},
        {"name": tr("Plan from VP"), "f": "a distance from XY = distance in front of or behind VP",
         "terms": tr("Below XY for a point in front of VP, above XY for a point behind VP.")},
        {"name": tr("Quadrant test"), "f": "sign of (a' - XY) and sign of (a - XY)",
         "terms": tr("Above-above is the second quadrant, below-below the fourth, above-below the "
                     "first and below-above the third.")},
    ]},
    {"title": tr("Apparent and true lengths"), "items": [
        {"name": tr("True length, tilted in one view"), "f": "plan = TL x cos(angle to HP)",
         "terms": tr("The plan keeps the run and loses the rise, so it is the true length times the "
                     "cosine of the angle the line makes with HP.")},
        {"name": tr("True length, tilted the other way"), "f": "elevation = TL x cos(angle to VP)",
         "terms": tr("The elevation keeps the rise and the run along XY and loses the depth, so it is "
                     "shortened by the cosine of the angle with VP.")},
        {"name": tr("True length from both views"),
         "f": "TL = square root of (run squared + rise squared + depth squared)",
         "terms": tr("Run is measured along XY, rise between the elevations and depth between the "
                     "plans; the three are at right angles, so they add as squares.")},
        {"name": tr("True inclination to HP"), "f": "sin(theta) = rise / TL",
         "terms": tr("The rise is the difference between the distances of the two ends above HP, "
                     "read off the elevation.")},
        {"name": tr("True inclination to VP"), "f": "sin(phi) = depth / TL",
         "terms": tr("The depth is the difference between the distances of the two ends in front of "
                     "VP, read off the plan.")},
    ]},
    {"title": tr("Traces"), "items": [
        {"name": tr("Horizontal trace"), "f": "elevation produced meets XY at h', project down",
         "terms": tr("A point on HP has its elevation on XY, so the HT is found by cutting XY with "
                     "the elevation produced and projecting to the plan produced.")},
        {"name": tr("Vertical trace"), "f": "plan produced meets XY at v, project up",
         "terms": tr("A point on VP has its plan on XY, so the VT is found by cutting XY with the "
                     "plan produced and projecting to the elevation produced.")},
    ]},
]

VIVA = [
    {"title": tr("Planes and points"), "items": [
        {"q": tr("What are the principal planes of projection?"),
         "a": tr("The horizontal plane HP, on which the plan (top view) is drawn, and the vertical "
                 "plane VP, on which the elevation (front view) is drawn. They are at right angles in "
                 "space and meet in the reference line XY, and the drawing is the two planes opened "
                 "out flat about XY.")},
        {"q": tr("Why is the plan drawn below XY?"),
         "a": tr("In first-angle projection the object sits between the observer and the plane, so "
                 "the plan is formed on the HP behind the object and, when the HP is rotated down "
                 "about XY to lie in the paper, the plan ends up below XY. The elevation, formed on "
                 "the VP behind the object, stays above XY.")},
        {"q": tr("How many measurements fix a point in space?"),
         "a": tr("Two: its distance above or below HP and its distance in front of or behind VP. "
                 "Each plane can show only one of them truly, which is why both views are needed.")},
        {"q": tr("What is a projector and what is it always perpendicular to?"),
         "a": tr("The thin line joining a point's elevation to its plan. It is always perpendicular "
                 "to XY, because the two views are of the same point seen from two directions at "
                 "right angles.")},
        {"q": tr("A point has both its views above XY. Where is it?"),
         "a": tr("In the second quadrant: above HP, because the elevation is above XY, and behind VP, "
                 "because the plan is above XY. The distances of the two views from XY are the height "
                 "above HP and the distance behind VP, and both views sit on one projector.")},
        {"q": tr("Where do the views of a point lying on HP fall?"),
         "a": tr("The elevation falls on XY itself, because the point is at zero height, while the "
                 "plan lies below XY at the distance the point is in front of VP.")},
    ]},
    {"title": tr("Lines, inclinations and true length"), "items": [
        {"q": tr("When does a view of a line show its true length?"),
         "a": tr("When the view is taken parallel to the line, which happens when the line is "
                 "parallel to the plane of that view. So a line parallel to VP shows its true length "
                 "in the elevation, and one parallel to HP shows it in the plan.")},
        {"q": tr("What is the difference between the true length and the apparent length?"),
         "a": tr("The true length is the real length of the line in space; the apparent length is the "
                 "length measured in a particular view. Every view except the one parallel to the "
                 "line is foreshortened, so the apparent length is always less than or equal to the "
                 "true length.")},
        {"q": tr("Why does a line perpendicular to HP appear as a point in the elevation?"),
         "a": tr("Because the elevation looks along the direction of the line, so its two ends fall on "
                 "the same projector and coincide. The plan then shows the true length, square to XY.")},
        {"q": tr("In the two-stage construction, why is the plan rotated and not the elevation?"),
         "a": tr("Rotating the plan about a is a rotation about a vertical axis through a, which "
                 "cannot change the height of any point. The elevations therefore stay on their locus "
                 "lines, and the second stage is read off those loci. Rotating the elevation would "
                 "change the heights and destroy the first stage.")},
        {"q": tr("What does the arc in the second stage guarantee?"),
         "a": tr("That the plan length is unchanged: every point on the arc is the same distance from "
                 "a, so the swing turns the plan without stretching it. The true length settled in "
                 "stage 1 is therefore preserved.")},
        {"q": tr("What is a trace of a line?"),
         "a": tr("The point where the line, produced if necessary, meets one of the reference planes. "
                 "The point where it meets HP is the horizontal trace HT and where it meets VP the "
                 "vertical trace VT.")},
        {"q": tr("Which line has no vertical trace, and why?"),
         "a": tr("A line parallel to VP, because it never meets VP however far it is produced; its "
                 "trace is said to be at infinity. In the same way a line parallel to HP has no "
                 "horizontal trace.")},
        {"q": tr("How are the two traces found from the views?"),
         "a": tr("Produce the elevation to cut XY at h' and drop a projector to meet the plan "
                 "produced: that is the HT. Produce the plan to cut XY at v and raise a projector to "
                 "meet the elevation produced: that is the VT.")},
    ]},
]

SOURCES = SOURCES
